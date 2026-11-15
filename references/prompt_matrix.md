# 📊 AI Model & Harness Matrix for 3D Web Development

This matrix maps specific 3D web development tasks to the best AI harness (OpenCode, Claude Code, ChatGPT/Codex, Cursor) and defines the exact prompting strategy required.

---

## 🔀 Comparison Summary

| Feature / Task | OpenCode | Claude Code | ChatGPT (Codex) | Cursor / Windsurf |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Strength** | Subagent orchestration & parallel tools | Precise multi-file diffs & deep logic | Shader math, creative prompts | Inline completion & fast iterations |
| **Context Handling** | Workspace-wide code mode | Large context window terminal agent | Single file focus / Canvas mode | Focused file diffs |
| **Best 3D Task** | Project scaffolding & build auditing | Complex state management & GSAP bindings | Custom GLSL shaders & particle math | Material tweaks & property tuning |
| **Recommended Prompt Type** | Task-based with subagent specs | Step-by-step technical spec | Mathematical & visual description | Inline code comments |

---

## 🎯 Task Routing Guide

### Task 1: Building Full Project Scaffolding
- **Best Tool**: **OpenCode**
- **Why**: OpenCode can spawn subagents to simultaneously write Vite configs, setup React Three Fiber canvas, generate component trees, and establish Tailwind styles.
- **Prompt Strategy**: Use high-level task delegation with explicit file output paths.

### Task 2: Custom GLSL Shaders & Raymarching
- **Best Tool**: **ChatGPT (Codex)**
- **Why**: ChatGPT excels at mathematical reasoning and converting artistic visual descriptions into raw GLSL code (noise functions, chromatic aberration, raymarching distance functions).
- **Prompt Strategy**: Provide math formulas or physical movement descriptions (e.g., "sine wave water ripple with normal mapping").

### Task 3: Complex State & GSAP Scroll Integration
- **Best Tool**: **Claude Code**
- **Why**: Claude Code handles structural refactoring and multi-hook synchronization exceptionally well without introducing subtle state bugs.
- **Prompt Strategy**: Provide strict step-by-step specs: "Create a Zustand store for camera targets, then hook GSAP ScrollTrigger to update targets smoothly in useFrame."

### Task 4: Fine-Tuning 3D Lights & Materials
- **Best Tool**: **Cursor / Windsurf**
- **Why**: Instant inline auto-completion lets you tweak roughness, metalness, shadow map resolutions, and vector coordinates in real-time.
- **Prompt Strategy**: Inline comments: `// Tweak directional light position and intensity for physical realism`.
