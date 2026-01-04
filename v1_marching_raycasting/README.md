## Version 1 – Marching-Step Raycasting

This version renders a 3D first-person view of a 2D maze by casting
rays from the player’s position and incrementally stepping forward
until a wall cell is encountered.

### Features
- 2D top-down maze representation
- 3D first-person projection
- Ray marching–based collision detection
- Toggle between 2D and 3D views (via the "View" button)

### Limitations
- Fisheye distortion due to uncorrected ray distances
- Less efficient than grid-based ray traversal methods (e.g. DDA)

This version was built as a proof of concept inspired by
early raycasting engines such as **DOOM**.
