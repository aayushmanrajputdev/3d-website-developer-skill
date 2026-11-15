# Scroll-Driven 3D Experience Prompts

## OpenCode - Multi-Agent Coordination

```markdown
You are the Scroll Animation Specialist. Create scroll-linked 3D camera animation.

Implementation:
1. Use @react-three/drei <ScrollControls pages={4}>
2. Create camera keyframes at each page:
   - Page 0: [0, 1.5, 5] - Hero view
   - Page 1: [4, 2, 3] - Features
   - Page 2: [-3, 0, 4] - Details
   - Page 3: [0, 1, 6] - CTA

3. In useFrame:
   const t = scroll.offset
   camera.position.lerp(targetPos, delta * 3)
   camera.lookAt(0, 0, 0)

4. Model animations:
   - Scale with scroll
   - Rotate based on progress

Output: ScrollOrchestrator.jsx + CameraPath.js + useScrollAnimation.js
```

## ChatGPT - Math for Scroll Interpolation

```markdown
Generate smooth scroll interpolation for camera movement from [0,1,5] to [4,2,3] over 500px scroll distance.
Use THREE.MathUtils.lerp(a, b, t) where t = clamped(scrollY / 500).
Also provide easing function for smooth acceleration.
```

## Cursor - Inline Performance

```javascript
// ISSUE: Scrub value too high causes lag
scrub: 2

// FIX: Optimal scrub for smooth but responsive
scrub: 0.8
```