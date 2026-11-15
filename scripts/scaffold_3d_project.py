#!/usr/bin/env python3
"""
3D Web Project Scaffolder

Scaffolds a complete 3D web project structure with best-practice configurations,
optimized for AI-assisted development workflows.

Usage:
    python scaffold_3d_project.py --type "react-r3f" --name "my-3d-app"
"""

import argparse
import json
from pathlib import Path

def generate_vite_config(project_name: str) -> str:
    return '''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          'three-js': ['three', '@react-three/fiber', '@react-three/drei'],
          'ui': ['framer-motion', '@react-spring/three']
        }
      }
    }
  }
})
'''

def generate_package_json(project_name: str, use_r3f: bool = True) -> str:
    deps = {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "@vitejs/plugin-react": "^4.2.0",
        "vite": "^5.2.0",
    }

    if use_r3f:
        deps.update({
            "@react-three/fiber": "^8.15.11",
            "@react-three/drei": "^9.106.0",
            "three": "^0.162.0",
            "@react-spring/three": "^9.8.2",
            "gsap": "^3.12.5"
        })

    extras = {
        "eslint": "^8.57.0",
        "eslint-config-prettier": "^9.1.0",
        "prettier": "^3.2.5",
        "@types/react": "^18.2.66",
        "@types/react-dom": "^18.2.22",
        "typescript": "^5.4.5"
    }

    pkg = {"name": project_name, "version": "0.1.0", "private": True, "dependencies": deps, "devDependencies": extras}
    return json.dumps(pkg, indent=2)

def generate_tsconfig() -> str:
    return json.dumps({
        "compilerOptions": {
            "target": "ES2022",
            "useDefineForClassFields": True,
            "module": "ESNext",
            "lib": ["DOM", "DOM.Iterable", "ES2022"],
            "skipLibCheck": True,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": True,
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx",
            "strict": True
        },
        "include": ["src"]
    }, indent=2)

def generate_eslint_config() -> str:
    return '''module.exports = {
  root: true,
  extends: ['eslint:recommended', 'prettier'],
  plugins: [],
  env: { browser: true, es2022: true },
  parserOptions: { ecmaVersion: 2022, sourceType: 'module' },
  rules: {
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }]
  }
}
'''

def generate_package_json_content(project_name: str, use_r3f: bool = True) -> str:
    deps = {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "@vitejs/plugin-react": "^4.2.0",
        "vite": "^5.2.0",
    }

    if use_r3f:
        deps.update({
            "@react-three/fiber": "^8.15.11",
            "@react-three/drei": "^9.106.0",
            "three": "^0.162.0",
            "@react-spring/three": "^9.8.2",
            "gsap": "^3.12.5"
        })

    extras = {
        "eslint": "^8.57.0",
        "eslint-config-prettier": "^9.1.0",
        "prettier": "^3.2.5",
        "@types/react": "^18.2.66",
        "@types/react-dom": "^18.2.22",
        "typescript": "^5.4.5"
    }

    pkg = {
        "name": project_name, 
        "version": "0.1.0", 
        "private": True, 
        "dependencies": deps, 
        "devDependencies": extras
    }
    return json.dumps(pkg, indent=2)

def scaffold_project(project_type: str, project_name: str, output_dir: str):
    """Generate complete project structure."""
    base = Path(output_dir) / project_name

    files = {
        'package.json': generate_package_json_content(project_name, project_type == 'r3f'),
        'vite.config.js': generate_vite_config(project_name),
        'tsconfig.json': generate_tsconfig(),
        '.eslintrc.cjs': generate_eslint_config(),
    }

    for file_path, content in files.items():
        full_path = base / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
        print(f"Created: {full_path}")

    print(f"\n✅ Project '{project_name}' scaffolded successfully!")

def main():
    parser = argparse.ArgumentParser(description="Scaffold 3D web projects")
    parser.add_argument('--type', choices=['r3f', 'vanilla', 'spline'], default='r3f', help='Project type')
    parser.add_argument('--name', default='my-3d-app', help='Project name')
    parser.add_argument('--out', default='.', help='Output directory')

    args = parser.parse_args()
    scaffold_project(args.type, args.name, args.out)

if __name__ == '__main__':
    main()