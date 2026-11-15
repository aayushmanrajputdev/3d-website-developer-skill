# 3D Hero Scene Prompt Templates

## OpenCode - Subagent Delegation

```markdown
You are the Hero 3D Scene Agent. Create a production-ready React Three Fiber component.

Requirements:
1. Canvas Setup: dpr={[1,2]}, antialias: true, outputColorSpace: SRGBColorSpace
2. Camera: position [0, 1.5, 5], fov 50
3. Lighting: ambient (0.4) + directional [5,10,5] intensity 1.5
4. Geometry: IcosahedronGeometry (1.5), MeshPhysicalMaterial
5. Animation: useFrame with elapsedTime for float + rotation
6. Hover: scale to 1.1x with spring
7. Memory: dispose in useEffect cleanup

Output: Complete HeroCanvas.jsx file
```

## ChatGPT - Visual Description

```markdown
Create an interactive 3D hero with a chrome sphere that floats gently up and down.
The sphere should have a mirror-like reflection with subtle environment lighting.
Add soft shadow on ground. Background is dark gradient. Mouse moves it slightly.
Use three.js React fiber syntax. Write complete working component.
```

## Cursor - Inline Optimization

```javascript
// Current: metalness: 0.8, roughness: 0.2
// Optimal for chrome glass: metalness: 0.95, roughness: 0.05
// Add transmission: 0.8, transmissionRoughness: 0.1
```