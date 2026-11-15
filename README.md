# 🚀 3D Website Developer AI Skill (OpenCode, Claude Code, ChatGPT)

[![OpenCode Compatible](https://img.shields.io/badge/OpenCode-Compatible-brightgreen.svg)](https://opencode.ai)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-blue.svg)](https://anthropic.com)
[![ChatGPT Compatible](https://img.shields.io/badge/ChatGPT%20Codex-Compatible-teal.svg)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/aayushmanrajputdev/3d-website-developer-skill?style=social)](https://github.com/aayushmanrajputdev/3d-website-developer-skill)
[![NPM Downloads](https://img.shields.io/npm/dt/three.js.svg)](https://www.npmjs.com/package/three)

> **The #1 AI Skill for 3D Website Developer, React Three Fiber skill, WebGL AI skill, GSAP ScrollTrigger prompt, and Three.js performance optimization.**
> Designed for **OpenCode**, **Claude Code**, **ChatGPT (Codex)**, **Cursor**, and **Windsurf**.

---

## 🌟 Overview: The Definitive 3D Website Developer Skill

The **3D Website Developer AI Skill** transforms AI coding assistants into expert 3D web architects and creative developers. Whether you are building immersive 3D landing pages, interactive product configurators, scroll-driven WebGL narratives, or high-performance WebGPU shaders, this skill equips your AI harness with battle-tested workflows, prompt engineering templates, anti-pattern detectors, and performance optimization rules.

### Why This Skill Outperforms Generic AI Prompts:

- **Harness-Aware Prompting**: Custom prompts optimized for OpenCode subagents, Claude Code terminal workflows, and ChatGPT Codex visual coding.
- **Zero-Jank Guarantee**: Built-in rules preventing common AI WebGL mistakes (memory leaks, render-loop re-renders, un-disposed geometries).
- **Multi-Library Synthesis**: Seamless integration across Three.js, React Three Fiber (R3F), Drei, GSAP ScrollTrigger, Lenis smooth scroll, Motion, and Spline.
- **Automated Performance Audit**: Includes static analysis scripts to verify 60 FPS performance budgets before deployment.

---

## 🎯 Target Keywords & SEO Rank Targets

This skill is optimized to rank #1-#3 for:

- **"3D website developer"** - Primary keyword
- **"React Three Fiber skill"** - High-value technical keyword
- **"WebGL AI skill"** - Emerging AI coding market
- **"GSAP ScrollTrigger prompt"** - Specialized animation keyword
- **"Three.js performance optimization"** - Developer-focused keyword

---

## 📦 Quick Installation

### Option 1: OpenCode / Agent Harness
Clone or add this repository into your OpenCode skills folder:
```bash
# Local installation for OpenCode
git clone https://github.com/aayushmanrajputdev/3d-website-developer-skill.git ~/.config/opencode/skills/3d-website-developer
```

### Option 2: Claude Code CLI
Add to your project's custom instructions or system prompt:
```bash
# Load SKILL.md directly in your terminal context
claude --prompt "Load skill from https://raw.githubusercontent.com/aayushmanrajputdev/3d-website-developer-skill/main/SKILL.md"
```

### Option 3: Cursor Extension
Install as a Cursor extension from the marketplace:
1. Go to `cursor.com/marketplace`
2. Search for "3D Website Developer"
3. Install and enable the extension
4. The skill will load automatically when needed

### Option 4: Agensi Marketplace
Install with one click from Agensi:
```bash
# Using Agensi tool
agensi get_skill 3d-website-developer
```

---

## 🧠 AI Harness Prompting Matrix for 3D Web Development

Different AI harnesses excel at different aspects of 3D development. Use this matrix to route tasks to the best model:

| AI Harness | Best For | Key Advantage | Recommended Task |
| :--- | :--- | :--- | :--- |
| **OpenCode** | Multi-file Scaffolding & Subagents | Parallel tool calls, workspace context | Full 3D app structure, R3F setup, build audits |
| **Claude Code** | Architecture & Refactoring | Precise diffs, step-by-step logic | Complex 3D state management, GSAP binding |
| **ChatGPT (Codex)** | Shader Math & Visual Styling | Creative math, instant visual feedback | Custom GLSL vertex & fragment shaders, particle physics |
| **Cursor / Windsurf** | In-line Auto-complete & Tweaks | Fast inline code completions | Tuning lighting, materials, and camera vectors |

---

## 💡 Top Master Prompt Templates

### 1. Hero 3D Interactive Scene Scaffolder (React Three Fiber skill)
```markdown
You are an expert 3D Web Developer specializing in React Three Fiber (R3F) and Three.js. 
Create an interactive 3D Hero scene for a web application with the following requirements:
1. Setup PerspectiveCamera with responsive aspect ratio handling.
2. Use ambientLight + directionalLight with soft shadows (PCFSoftShadowMap).
3. Create a floating, interactive 3D model with subtle float animation (sin wave on position.y in useFrame).
4. Add hover & click interaction with spring physics (react-spring or motion-framer-3d).
5. Ensure strict resource disposal on unmount to prevent memory leaks.
6. Target 60 FPS on mobile and desktop.
```

### 2. GSAP Scroll-Driven 3D Storytelling Prompt (WebGL AI skill)
```markdown
Build a multi-section scroll-driven 3D experience using React Three Fiber, @react-three/drei (ScrollControls), and GSAP ScrollTrigger.
- Section 1: Hero view (Camera pos: [0, 2, 5], Model rotation: [0, 0, 0])
- Section 2: Feature breakdown (Camera smoothly transitions to [3, 0, 2], Model rotates 180deg)
- Section 3: Exploded 3D view (Model parts separate along local axes based on scroll progress)
- Link scroll offset directly to camera interpolation (lerp) for silky smooth transitions.
- Ensure no layout shift (CLS) and keep frameloop="always" or scrubbed lerp.
```

### 3. GSAP ScrollTrigger prompt for 3D Parallax
```markdown
Create a GSAP ScrollTrigger-driven 3D parallax effect where:
- Multiple layers scroll at different speeds (parallax intensity)
- Objects rotate on scroll with easing functions
- Use scroller: "body" and clear() for smooth resets
- Implement scrub: true for continuous animation tied to scroll
```

### 4. Custom GLSL Shader Generator Prompt (Three.js performance optimization)
```markdown
Write a custom THREE.ShaderMaterial in GLSL (vertex & fragment shaders) for a liquid distortion wave effect:
- Vertex Shader: Deform geometry vertices using a 3D Simplex/Perlin noise function driven by uTime.
- Fragment Shader: Sample a color texture and apply chromatic aberration based on vertex displacement.
- Uniforms required: uTime (float), uNoiseFrequency (float), uNoiseAmplitude (float), uTexture (sampler2D).
- Must run cleanly on WebGL 2.0 without precision artifact stutter.
- Use Three.js performance optimization: pre-allocate Vector3, avoid setState in loops, dispose resources.
```

---

## 🛠️ Performance & Anti-Pattern Protection (Three.js performance optimization)

This skill enforces strict 3D Web Guidelines:

- ❌ **NEVER call `setState` inside `useFrame`** (causes frame drops, breaks Three.js performance optimization)
- ❌ **NEVER instantiate new `THREE.Vector3` or geometries inside render loops** (memory leaks, GC pressure)
- ❌ **NEVER omit resource disposal** (memory leaks, GPU memory bloat)
- ✅ **ALWAYS set `texture.colorSpace = THREE.SRGBColorSpace`** (PBR rendering correctness)
- ✅ **ALWAYS use `InstancedMesh`** for rendering hundreds of repeated 3D objects (WebGL AI skill optimization)

---

## 🔧 Three.js Performance Optimization Techniques

### Memory Management
```javascript
// Resource disposal pattern for Three.js performance optimization
useEffect(() => {
  return () => {
    geometry.dispose();
    material.dispose();
    texture.dispose();
  };
}, []);
```

### Efficient Animation Loop
```javascript
// useFrame optimization - never call setState
useFrame((state, delta) => {
  // Mutate refs directly for Three.js performance optimization
  ref.current.position.lerp(targetPosition, delta * 4);
});
```

### Pre-allocation Pattern
```javascript
// Pre-allocate Vector3 for Three.js performance optimization
const tempVector = new THREE.Vector3();
const startAnimation = () => {
  // Reuse pre-allocated objects instead of creating new ones
  tempVector.copy(position).add(offset);
};
```

---

## 📁 Repository Structure

```
3d-website-developer-skill/
├── SKILL.md                     # Core AI Agent Skill Instructions
├── README.md                    # Project Documentation & Usage Guide (SEO Optimized)
├── references/
│   ├── prompt_matrix.md         # Detailed Harness Comparison (OpenCode, Claude Code, ChatGPT)
│   ├── prompt_templates.md      # Ready-to-use Master Prompts
│   ├── 3d_stack_guide.md        # Stack Decision Matrix (Three.js vs R3F vs WebGPU)
│   └── common_ai_3d_pitfalls.md # Top 10 WebGL AI Bugs & Fixes
├── scripts/
│   ├── analyze_3d_perf.py       # Python AST Performance & Memory Leak Auditor
│   ├── generate_3d_prompt.py    # CLI Prompt Generator for any 3D task
│   └── scaffold_3d_project.py   # Vite + React + Three.js Project Generator
└── assets/
    ├── prompts/                 # Modular Prompt Library
    └── examples/                # Production Boilerplates (R3F + GSAP + Shaders)
```

---

## 🤝 Contributing

Contributions are welcome! If you have optimized prompts, shader code snippets, or bug prevention rules for 3D web development, feel free to submit a Pull Request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

Developed with ❤️ by [Aayushman Rajput](https://github.com/aayushmanrajputdev).

---

## 🔍 Search Engine Optimization

This README is structured with SEO-optimized headers and keywords to achieve high rankings for 3D web development skills:

- **Primary Keywords**: "3D website developer", "React Three Fiber skill", "WebGL AI skill"
- **Secondary Keywords**: "GSAP ScrollTrigger prompt", "Three.js performance optimization", "R3F performance", "WebGL shaders"
- **Semantic Headers**: H1, H2, H3 tags structured for featured snippets
- **Code Blocks**: Include keywords in code examples for technical SEO