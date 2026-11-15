# ⚠️ Top 10 Bugs AI Models Make in 3D Web Development (and how to fix them)

When AI tools generate 3D code, they frequently make subtle performance and WebGL bugs. This guide lists the top 10 mistakes and exact instructions to prevent them.

---

### Bug 1: Calling `setState` inside `useFrame`
- **Problem**: Re-renders the entire React component 60 times per second, killing frame rate.
- **Fix**: Mutate refs directly inside `useFrame`.
```javascript
// ❌ WRONG
useFrame(() => setX(x + 0.01));

// ✅ RIGHT
const meshRef = useRef();
useFrame((state, delta) => {
  meshRef.current.position.x += delta;
});
```

---

### Bug 2: Allocating Objects inside Render Loop
- **Problem**: Creates thousands of short-lived objects per second, triggering JavaScript Garbage Collection (GC) stutters.
- **Fix**: Pre-allocate vectors and matrices outside the loop.
```javascript
// ❌ WRONG
useFrame(() => {
  const target = new THREE.Vector3(1, 2, 3); // Allocates memory every frame!
  camera.position.lerp(target, 0.1);
});

// ✅ RIGHT
const target = useMemo(() => new THREE.Vector3(1, 2, 3), []);
useFrame(() => {
  camera.position.lerp(target, 0.1);
});
```

---

### Bug 3: Missing Texture ColorSpace Configuration
- **Problem**: Textures look washed out or overly dark because color space defaults to Linear instead of sRGB.
- **Fix**: Set `colorSpace` explicitly on loaded textures.
```javascript
texture.colorSpace = THREE.SRGBColorSpace;
```

---

### Bug 4: Z-Fighting (Flickering Surfaces)
- **Problem**: Objects coplanar or camera `near` and `far` clipping planes set too wide (e.g. `near: 0.00001, far: 1000000`).
- **Fix**: Keep `near` as high as feasible (e.g., `0.1`) and `far` as low as feasible.

---

### Bug 5: Memory Leaks on Unmount
- **Problem**: Unmounting React components without disposing WebGL buffers causes memory leaks that crash the browser tab after repeated navigation.
- **Fix**: Always call `.dispose()` on geometries, materials, and textures in cleanup hooks.

---

### Bug 6: Overusing Individual Meshes instead of `InstancedMesh`
- **Problem**: Creating 1,000 individual `<mesh>` components generates 1,000 WebGL draw calls, choking the GPU.
- **Fix**: Use `InstancedMesh` to render identical geometries in a single draw call.

---

### Bug 7: Ignoring Device Pixel Ratio (DPR) Cap
- **Problem**: Setting DPR to `window.devicePixelRatio` on 4K / Retina screens causes 4x pixel shading load, dropping frame rates to 15 FPS.
- **Fix**: Always cap DPR at `[1, 2]`: `<Canvas dpr={[1, 2]}>`.

---

### Bug 8: Forgetting `makeDefault` on OrbitControls
- **Problem**: Controls override custom camera animation routines.
- **Fix**: Pass `makeDefault` to `<OrbitControls makeDefault />`.

---

### Bug 9: Unhandled Window Resize
- **Problem**: 3D canvas stretches or distorts on browser window resize.
- **Fix**: Always update camera aspect ratio and call `camera.updateProjectionMatrix()`.

---

### Bug 10: Mixing Up Radians and Degrees
- **Problem**: Rotations applied in degrees cause chaotic visual spinning (Three.js expects radians).
- **Fix**: Convert degrees using `THREE.MathUtils.degToRad(degrees)`.
