# Version 2 – DDA Raycasting

This version improves upon the original ray-marching implementation by
using **DDA (Digital Differential Analyzer) raycasting** and correcting
fisheye distortion.

The result is a more accurate, efficient, and visually stable 3D
rendering of the same 2D maze.

---

## Improvements From Version 1

- Grid-based **DDA ray traversal**
- Fisheye distortion correction
- More consistent wall heights across the field of view
- Improved performance compared to marching-step raycasting

---

## How It Works

Each ray advances from grid cell to grid cell using DDA, efficiently
determining horizontal or vertical wall intersections.  
Perpendicular wall distance is calculated to correct fisheye distortion
before projecting wall slices onto the screen.

---

## Remaining Limitations

- Slight wall curvature near the edges of the field of view due to
  equally spaced ray angles mapped to linear screen columns
- Basic lighting and flat shading
- No texture mapping or vertical look



