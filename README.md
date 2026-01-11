# Doom-Style Raycasting Maze Engine

## Overview
This project explores how a 2D grid-based world can be rendered as a 3D first-person view
using raycasting techniques inspired by early games like DOOM.

The project started as a simple marching-step raycaster and was later upgraded
to a DDA-based approach to remove fisheye distortion and improve accuracy.

---

## Preview (Version 2 – DDA Raycasting)

| 2D Map View | 3D First-Person View |
|------------|----------------------|
| ![](screenshots/v2_2D_View.png) | ![](screenshots/v2_3D_View.png) |

---

## Project Evolution

### Version 1 – Marching Step Raycasting
- Basic ray marching
- Demonstrates 2D → 3D projection
- Suffers from fisheye distortion
- Uses a simple but inefficient raycasting approach
- Built quickly as a proof of concept

### Version 2 – DDA Raycasting (In Progress)
- Uses Digital Differential Analysis (DDA)
- Corrects fisheye distortion
- More accurate wall distance calculation
- Closer to classic DOOM-style rendering

---

## Controls
- W / S – Move forward / backward
- A / D – Strafe left / right
- Left / Right Arrow – Rotate
- Click “View” – Toggle 2D / 3D view

---

## Requirements

- Python 3.x
- Pygame

Install dependencies:
```bash
pip install pygame

---

## How to Run

```bash

# Version 1 – Marching Step Raycasting
python marching_raycast.py

# Version 2 – DDA Raycasting
python DDA_raycast.py

