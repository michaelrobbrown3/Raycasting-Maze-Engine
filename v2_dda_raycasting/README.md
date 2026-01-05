## Version 2 – DDA Raycasting (No Fisheye)

This version replaces the marching-step raycasting approach with a
Digital Differential Analyzer (DDA) algorithm to traverse the grid
cell-by-cell until a wall is encountered.

By calculating exact grid intersections, this implementation:
- Eliminates fisheye distortion
- Improves performance
- Produces more accurate wall distances

### Key Improvements Over Version 1
- Grid-based DDA ray traversal
- Correct perpendicular wall distance calculation
- Increased ray count with better performance
- Cleaner and more stable 3D projection

### Features
- 2D top-down debug view with ray visualization
- 3D first-person rendering without fisheye distortion
- Smooth player movement and strafing
- Toggle between 2D and 3D views

This implementation is inspired by the raycasting techniques used
in early engines such as **DOOM** and **Wolfenstein 3D**.
