# 📝 Master Prompt Templates for 3D Web Development

Use these battle-tested, copy-pasteable prompt templates to get 10x better code from any AI model.

---

## Template 1: Hero 3D Interactive Canvas Scene

```markdown
You are a Senior 3D Web Developer specializing in Three.js and React Three Fiber (R3F).
Please generate a production-ready R3F Hero Scene component called `HeroExperience.jsx`.

Requirements:
1. **Canvas & Camera**:
   - Set up PerspectiveCamera at position [0, 1.5, 5] with FOV 50.
   - Configure WebGLRenderer with antialias, DPR capped at [1, 2], and outputColorSpace = SRGBColorSpace.
2. **Lighting**:
   - Add ambientLight (intensity: 0.4).
   - Add directionalLight (position: [5, 10, 5], intensity: 1.5, castShadow: true).
   - Set shadow map type to PCFSoftShadowMap.
3. **Interactive 3D Geometry**:
   - Create a floating geometric object (e.g., RoundedBox or Icosahedron) with a MeshPhysicalMaterial (metalness: 0.8, roughness: 0.2, clearcoat: 1.0).
   - Add subtle floating animation on the Y-axis using Math.sin(state.clock.elapsedTime * 1.5) inside useFrame.
   - Add hover state that smoothly scales the object to 1.2x using spring physics (or lerp inside useFrame).
4. **Performance & Memory Protection**:
   - Do NOT call setState inside useFrame.
   - Pre-allocate any Vector3 objects used for lerping outside the frame loop.
   - Implement clean resource disposal on unmount.
```

---

## Template 2: GSAP Scroll-Driven 3D Storytelling

```markdown
You are an expert in GSAP ScrollTrigger and React Three Fiber integration.
Create a multi-step scroll-driven 3D experience component.

Requirements:
1. **Structure**:
   - Wrap the canvas content with @react-three/drei's `<ScrollControls pages={4} damping={0.2}>`.
2. **Keyframe Camera Locations**:
   - Page 0 (Hero): Camera at [0, 2, 6], looking at [0, 0, 0].
   - Page 1 (Features): Camera lerps to [4, 1, 3], looking at [0, 0, 0].
   - Page 2 (Details): Camera lerps to [-3, -1, 4], looking at [0, 0, 0].
   - Page 3 (CTA): Camera lerps back to [0, 0, 5].
3. **Execution**:
   - Use `useScroll()` hook from Drei inside a child component.
   - In `useFrame`, read `scroll.offset` (0 to 1 range) and compute target camera position and rotation.
   - Smoothly interpolate (lerp) camera transform using `THREE.MathUtils.lerp(current, target, delta * 3)`.
4. **HTML Overlay**:
   - Render fixed HTML sections overlaid on top of the canvas that fade in/out based on scroll thresholds.
```

---

## Template 3: Custom GLSL Shader (Wave & Chromatic Aberration)

```markdown
Generate a custom THREE.ShaderMaterial in GLSL for React Three Fiber / Three.js.

Shader Specs:
1. **Vertex Shader**:
   - Displace vertex positions along normals using a 3D Simplex noise function.
   - Drive noise animation with a uniform `uTime` (passed from clock in useFrame).
   - Expose uniform `uAmplitude` and uniform `uFrequency`.
2. **Fragment Shader**:
   - Accept a texture uniform `uTexture` (sampler2D).
   - Calculate distortion offset based on the vertex displacement.
   - Implement chromatic aberration by sampling Red, Green, and Blue channels at slight UV offsets.
3. **Boilerplate**:
   - Provide standard React Three Fiber component wrapper using `extend({ ShaderMaterial })` or `shaderMaterial` from Drei.
```

---

## Template 4: 3D Performance Audit & Garbage Collection Fix

```markdown
Review the following 3D WebGL / R3F code for performance bottlenecks and memory leaks:

Checklist to fix:
1. Are there any `setState` calls inside `useFrame` or animation callbacks? Convert them to `useRef` mutations.
2. Are new geometries, materials, or Vector3 instances created inside the render loop? Pre-allocate them.
3. Are geometries and materials properly disposed when components unmount (`geometry.dispose()`, `material.dispose()`)?
4. Is InstancedMesh used if there are more than 50 repeated objects?
5. Are textures compressed and using `SRGBColorSpace`?

Provide refactored code with explanatory comments detailing every performance improvement made.
```
