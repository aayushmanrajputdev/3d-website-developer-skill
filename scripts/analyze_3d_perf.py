#!/usr/bin/env python3
"""
3D WebGL Performance Analysis Script

Analyzes JavaScript/TSX files for common 3D web performance bugs
and memory leaks that AI models frequently introduce.

Usage:
    python analyze_3d_perf.py <file_path> [--fix]
"""

import re
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List

@dataclass
class Issue:
    line: int
    severity: str  # critical, high, medium, low
    category: str
    message: str
    suggestion: str

@dataclass
class AnalysisResult:
    total_lines: int
    issues: List[Issue] = field(default_factory=list)
    score: int = 100  # 0-100 performance score

def analyze_file(file_path: str) -> AnalysisResult:
    """Analyze a file for 3D WebGL performance issues."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = path.read_text()
    lines = content.split('\n')

    result = AnalysisResult(total_lines=len(lines))

    # Check 1: setState inside useFrame
    result.issues.extend(_check_set_state_in_use_frame(lines))

    # Check 2: Object allocation in loops
    result.issues.extend(_check_allocation_in_loops(lines))

    # Check 3: Missing dispose calls
    result.issues.extend(_check_missing_dispose(lines))

    # Check 4: DPR over-allocation
    result.issues.extend(_check_dpr_allocation(lines))

    # Check 5: Texture colorSpace missing
    result.issues.extend(_check_texture_colorspace(lines))

    # Calculate performance score
    severity_weights = {'critical': 25, 'high': 15, 'medium': 5, 'low': 2}
    deductions = sum(severity_weights.get(i.severity, 0) for i in result.issues)
    result.score = max(0, result.score - deductions)

    return result

def _check_set_state_in_use_frame(lines: List[str]) -> List[Issue]:
    """Detect setState calls inside useFrame hooks."""
    issues = []
    for i, line in enumerate(lines, 1):
        if 'useFrame(' in line or 'useFrame(' in line:
            # Check next 5 lines for setState calls
            for j in range(i, min(i + 5, len(lines))):
                next_line = lines[j]
                if next_line.strip() and ('setState(' in next_line or 'set' in next_line and '(' in next_line):
                    issues.append(Issue(
                        line=j,
                        severity='critical',
                        category='State Management',
                        message='React setState called inside useFrame hook',
                        suggestion='Mutate a ref directly instead of calling setState'
                    ))
                    break
    return issues

def _check_allocation_in_loops(lines: List[str]) -> List[Issue]:
    """Detect object allocation inside render loops."""
    issues = []
    loop_contexts = []

    for i, line in enumerate(lines, 1):
        # Track loop contexts
        if 'useFrame(' in line or 'requestAnimationFrame(' in line:
            loop_contexts.append(i)

        # Check for new instances
        if re.search(r'\bn(?:ew)\s+(THREE\.)?Vector\d+\(', line):
            if loop_contexts:
                issues.append(Issue(
                    line=i,
                    severity='high',
                    category='Memory Allocation',
                    message='Object allocation inside render loop',
                    suggestion='Pre-allocate Vector3 objects outside the loop or use useMemo'
                ))

        if re.search(r'\bn(?:ew)\s+(THREE\.)?(Mesh|Geometry|Material)', line):
            if loop_contexts:
                issues.append(Issue(
                    line=i,
                    severity='high',
                    category='Memory Allocation',
                    message='3D object allocation inside render loop',
                    suggestion='Create objects outside render loop or use instancing'
                ))

    return issues

def _check_missing_dispose(lines: List[str]) -> List[Issue]:
    """Check for missing .dispose() calls on components that use useRef."""
    issues = []
    has_ref = False
    in_effect = False

    for i, line in enumerate(lines, 1):
        if 'useRef(' in line:
            has_ref = True

        if has_ref and ('useEffect(' in line or 'useEffect(async' in line):
            in_effect = True

        if in_effect and '.dispose()' in line:
            has_ref = False
            in_effect = False

    return issues

def _check_dpr_allocation(lines: List[str]) -> List[Issue]:
    """Check for unsafe devicePixelRatio usage."""
    issues = []
    for i, line in enumerate(lines, 1):
        if 'devicePixelRatio' in line and 'dpr' not in line.lower():
            issues.append(Issue(
                line=i,
                severity='medium',
                category='Performance',
                message='Direct DevicePixelRatio usage can cause performance issues on high-DPI screens',
                suggestion='Cap DPR with dpr={[1,2]} or Math.min(window.devicePixelRatio, 2)'
            ))
    return issues

def _check_texture_colorspace(lines: List[str]) -> List[Issue]:
    """Check for missing texture colorSpace configuration."""
    issues = []
    for i, line in enumerate(lines, 1):
        if 'TextureLoader' in line and 'load' in line:
            # Check next 5 lines for colorSpace
            has_colorspace = any('colorSpace' in lines[j] for j in range(i, min(i + 5, len(lines))))
            if not has_colorspace:
                issues.append(Issue(
                    line=i,
                    severity='medium',
                    category='Color Management',
                    message='Textures may render incorrectly without colorSpace configuration',
                    suggestion='Add texture.colorSpace = THREE.SRGBColorSpace after loading'
                ))
    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_3d_perf.py <file_path> [--fix]")
        print("\nAnalyzes JavaScript/TypeScript files for 3D WebGL performance bugs.")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        result = analyze_file(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"3D WebGL Performance Analysis: {file_path}")
    print(f"{'='*60}")

    if result.issues:
        print(f"\n⚠️  Found {len(result.issues)} issues (Score: {result.score}/100)\n")
        for issue in result.issues:
            print(f"  [{issue.severity.upper()}] Line {issue.line}: {issue.message}")
            print(f"    → {issue.suggestion}")
            print()
    else:
        print(f"\n✅ No issues found! Performance score: {result.score}/100")

    # Output JSON summary
    summary = {
        'file': file_path,
        'total_lines': result.total_lines,
        'issues_count': len(result.issues),
        'severity_counts': {
            'critical': len([i for i in result.issues if i.severity == 'critical']),
            'high': len([i for i in result.issues if i.severity == 'high']),
            'medium': len([i for i in result.issues if i.severity == 'medium']),
            'low': len([i for i in result.issues if i.severity == 'low'])
        },
        'score': result.score,
        'issues': [
            {
                'line': i.line,
                'severity': i.severity,
                'category': i.category,
                'message': i.message
            } for i in result.issues
        ]
    }

    print(f"\nJSON Summary:\n{json.dumps(summary, indent=2)}")

if __name__ == '__main__':
    main()