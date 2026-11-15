# 3D Web Example Projects

## Example Structure

Each example is a complete, runnable project you can copy directly.

```
examples/
├── hero-scene/           # Minimal Hero 3D landing page
│   ├── src/
│   │   ├── App.jsx       # R3F Hero component
│   │   ├── HeroCanvas.jsx
│   │   └── useFloating.ts
│   └── package.json
│
├── scroll-storytelling/  # GSAP Scroll-Driven 3D Experience
│   ├── src/
│   │   ├── ScrollOrchestrator.jsx
│   │   ├── CameraPath.jsx
│   │   └── ModelAnimator.jsx
│   └── index.html
│
├── shader-gallery/       # Custom GLSL Shader Showcase
│   ├── shaders/
│   │   ├── vertex.wgsl
│   │   └── fragment.glsl
│   └── components/
│       └── ShaderPreview.jsx
│
└── product-viewer/       # 3D Product Configurator
    ├── models/
    │   └── chair.glb
    ├── components/
    │   ├── ProductCanvas.jsx
    │   └── ColorSwatch.jsx
    └── store/
        └── useProductStore.ts
```

## Running Examples

```bash
cd examples/hero-scene
npm install
npm run dev
```