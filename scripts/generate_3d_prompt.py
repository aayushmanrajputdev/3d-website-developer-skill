#!/usr/bin/env python3
"""
3D Web Prompt Generator

Generates optimized AI prompts for 3D web development based on task type
and target AI harness (OpenCode, Claude Code, ChatGPT, Cursor).

Usage:
    python generate_3d_prompt.py --task "hero-scene" --harness "opencode"
"""

import argparse
import sys
from typing import Dict

PROMPT_TEMPLATES = {
    "opencode": {
        "hero-scene": {
            "title": "Hero 3D Interactive Canvas Scene",
            "template": """You are a Senior 3D Web Developer specializing in React Three Fiber (R3F).
Create a production-ready R3F Hero Scene component called HeroScene.jsx.

Requirements:
1. Canvas Setup: dpr={[1,2]}, antialias: true, outputColorSpace: SRGBColorSpace
2. Camera: position [0, 1.5, 5], fov 50
3. Lighting: ambient (0.4) + directional [5,10,5] intensity 1.5
4. Geometry: IcosahedronGeometry (1.5), MeshPhysicalMaterial
5. Animation: useFrame with elapsedTime for float + rotation
6. Hover: scale to 1.1x with spring
7. Memory: dispose in useEffect cleanup"""
        },
        "scaffold": {
            "title": "Full 3D Project Scaffolding",
            "template": """You are the 3D Project Architect. Scaffold a complete Vite + React + Three.js project.

Output directory structure:
- package.json (dependencies: react, three, @react-three/fiber, @react-three/drei, gsap)
- vite.config.js (with GLTF and Draco support)
- tsconfig.json (strict mode enabled)
- src/
  - App.jsx (root with Canvas)
  - components/Scene.jsx (3D scene)
  - hooks/use3DState.ts (Zustand store)
  - styles/globals.css

Write all files. No explanations."""
        }
    },
    "claude": {
        "shader": {
            "title": "Custom GLSL Shader",
            "template": """Build a THREE.ShaderMaterial for water ripple effect.

Vertex requirements:
- 3D Simplex noise function (implement inline)
- Displacement: noise * uAmplitude
- Uniforms: uTime, uAmplitude, uFrequency

Fragment requirements:
- UV distortion with time
- Color blending from #4a90a0 to white
- Optional: chromatic aberration

Output: Working vertex.glsl and fragment.glsl files."""
        }
    },
    "chatgpt": {
        "visual-effect": {
            "title": "Visual Shader Effect Concept",
            "template": """Design a fragment shader for {effect_description}.

Visual requirements:
- Style: {style}
- Inspiration: {inspiration}
- Technique: {technique}

Output GLSL code for fragment shader with uniforms."""
        }
    }
}

def generate_prompt(task: str, harness: str, **kwargs) -> str:
    """Generate a prompt based on task and harness."""
    if harness not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown harness: {harness}. Available: {list(PROMPT_TEMPLATES.keys())}")
    
    if task not in PROMPT_TEMPLATES[harness]:
        raise ValueError(f"Unknown task: {task}. Available for {harness}: {list(PROMPT_TEMPLATES[harness].keys())}")
    
    template = PROMPT_TEMPLATES[harness][task]
    prompt = template['template']
    
    # Fill in any kwargs
    for key, value in kwargs.items():
        prompt = prompt.replace(f"{{{key}}}", str(value))
    
    return f"### {template['title']}\n\n{prompt}"

def main():
    parser = argparse.ArgumentParser(description="Generate AI prompts for 3D web development")
    parser.add_argument('--task', required=True, help='Task name (e.g., hero-scene, shader)')
    parser.add_argument('--harness', required=True, help='AI harness (opencode, claude, chatgpt)')
    parser.add_argument('--effect', help='Visual effect description')
    parser.add_argument('--style', help='Visual style')
    parser.add_argument('--inspiration', help='Inspiration source')
    parser.add_argument('--technique', help='Technique name')
    
    args = parser.parse_args()
    
    kwargs = {
        'effect_description': args.effect,
        'style': args.style,
        'inspiration': args.inspiration,
        'technique': args.technique
    }
    
    try:
        prompt = generate_prompt(args.task, args.harness, **kwargs)
        print(prompt)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()