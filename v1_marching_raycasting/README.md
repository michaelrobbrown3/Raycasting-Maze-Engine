## Version 1 – Marching-Step Raycasting

This project demonstrates how a 2D maze can be rendered as a 3D
first-person view using a marching-step raycasting technique.

Inspired by early engines such as **DOOM**, the world is stored as a
2D grid and rays are cast from the player’s position to determine
visible walls.

---

## Features

- 2D top-down maze view
- 3D first-person projection
- Marching-step raycasting
- Toggle between 2D and 3D views
- Basic collision detection

---

## How It Works

Rays are cast from the player at equally spaced angles across the field
of view. Each ray advances forward in small steps until it hits a wall.
The distance to the wall is then used to draw a vertical slice on the
screen, creating a 3D effect.

---

## Limitations

- **Fisheye distortion** due to uncorrected ray distances
- **Slight wall curvature near the screen edges** caused by using
  equally spaced ray angles with linear screen columns
- Ray marching is less efficient than grid-based methods (e.g. DDA)


