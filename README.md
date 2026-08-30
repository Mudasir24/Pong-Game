# 🏓 Pong Game

A feature-rich take on classic Pong, built with Python and Pygame — full menu system,
multiple game modes, paddle customization, sound effects, and a persistent local
leaderboard.

<!-- 🖼️ IMAGE NEEDED #1: A screenshot of the main menu (the screen with Play/Options/Exit).
     Save as: docs/screenshot-menu.png -->
<p align="center">
  <img src="docs/screenshot-menu.png" alt="Main menu" width="500"/>
</p>

<!-- 🖼️ IMAGE NEEDED #2: A screenshot of actual gameplay (mid-match, both paddles and ball visible).
     Save as: docs/screenshot-gameplay.png -->
<p align="center">
  <img src="docs/screenshot-gameplay.png" alt="Gameplay" width="500"/>
</p>

<!-- 🖼️ IMAGE NEEDED #3 (optional): A screenshot of the leaderboard screen.
     Save as: docs/screenshot-leaderboard.png -->

---

## ✨ Features

- **Single-player and two-player modes**
- **Three game modes:**
  - **Classic** — first to a target score wins
  - **Timer** — score as much as possible before time runs out
  - **Survival** — limited lives (hearts); the ball speeds up over time
- **Selectable target score** (5 / 10 / 15) for Classic mode
- **Paddle color customization** (red / green / blue / white)
- **Persistent leaderboard** — top scores are saved locally between sessions
- **Sound effects and background music** (paddle hits, scoring, game over)
- **Full menu system** with hover states on every button

---

## 🗂 Project Structure

```
Pong-Game/
├── src/
│   ├── main.py              # The full game — menus, modes, rendering, everything
│   ├── leaderboard.json     # Saved local high scores (created/updated at runtime)
│   └── assets/               # Images, sounds, and the window icon
│
├── early-prototype/
│   └── pong_prototype.py    # The very first version — bare-bones two-paddle pong,
│                             # no menus, no sound. Kept to show how the project grew.
│
├── docs/
│   ├── Project Expo Summary.pdf
│   └── pong.docx
│
└── requirements.txt
```

---

## 🚀 How to Run

```bash
git clone https://github.com/Mudasir24/Pong-Game.git
cd Pong-Game
pip install -r requirements.txt
python src/main.py
```

The leaderboard file (`src/leaderboard.json`) is created automatically the first
time you play if it doesn't already exist, and updates as new high scores are set.

---

## 🎮 Controls

| Player | Move Up | Move Down |
|---|---|---|
| Left paddle | `W` | `S` |
| Right paddle | `↑` (Up Arrow) | `↓` (Down Arrow) |

---

## 🛠 Tech Stack

Python + [Pygame](https://www.pygame.org/) — no other dependencies.

---

## 📄 Project Docs

Additional writeups from when this was built as an expo project are in
[`docs/`](./docs): a project summary PDF and a Word doc with more detail.
