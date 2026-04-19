# Space Invaders

A **SimpleGUI**-style space shooter built for **CodeSkulptor**-compatible APIs: menus, waves of enemies, missiles and lasers, and in-game shops to unlock ships and weapons. Sprites are loaded from remote URLs (see below).

Entry point: **`Game-15.py`**.

## Prerequisites

- **Python 3** (3.8+ recommended)
- **[SimpleGUICS2Pygame](https://pypi.org/project/SimpleGUICS2Pygame/)** — provides `simplegui` locally when [CodeSkulptor’s](https://py3.codeskulptor.org/) browser `simplegui` is not available
- **`Vector.py`** — a 2D vector helper in the same folder as `Game-15.py` (same role as the **Rice University / Interactive Python** `Vector` class: `Vector(x, y)`, `get_p()`, in-place `add`, `copy`, and methods used elsewhere in the game). This repository does **not** ship that file; add your copy next to `Game-15.py` before running.

## Setup

```bash
cd space-invaders
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install SimpleGUICS2Pygame
```

Place **`Vector.py`** in this directory if you have it from the original coursework or equivalent.

## Run

```bash
python Game-15.py
```

The game tries `import simplegui` first (browser/CodeSkulptor), then falls back to **SimpleGUICS2Pygame**.

## Controls

| Keys | Action |
|------|--------|
| **←** / **→** | Move ship |
| **↑** | Action tied to movement / firing context in the game loop |
| **Space** | Fire (missiles / lasers depending on state) |

Use **Play** / **Exit** and the on-screen **Shop** flows for ships, lasers, and rockets.

## Assets and network

Images and sounds are loaded with **`simplegui.load_image(...)`** from `http://personal.rhul.ac.uk/...` URLs. You need a **working network** the first time those assets are fetched (and hosts must still serve the files).

## Project layout

| File | Role |
|------|------|
| `Game-15.py` | Full game: `Game`, UI, entities, `simplegui` frame and main loop |
| `Vector.py` | *(You supply.)* 2D vector math used throughout |

## Stack

- **Language:** Python 3  
- **UI / canvas:** SimpleGUI (CodeSkulptor or **SimpleGUICS2Pygame** + **Pygame**)
