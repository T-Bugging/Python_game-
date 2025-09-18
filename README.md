
A simple 2D dodge game built with Python and Pygame.  
The player controls a green block and must avoid falling stars as long as possible.  
Difficulty increases over time as more stars spawn faster.

---

##  Gameplay

- Use **← Left Arrow** and **→ Right Arrow** keys to move.  
- Survive as long as you can while avoiding the falling white stars.  
- Once hit, the game displays **GAME OVER** with your survival time.  

---

## 🛠 Features

- Real-time game loop with 60 FPS cap  
- Randomized star spawning  
- Increasing difficulty over time  
- Collision detection with `pygame.Rect`  
- Timer to track survival duration  
- Game over screen with reset delay  

---

##  Files

- `main.py` → main game script  
- `542443.jpg` → background image (replace with any 1920×875 image you like)  

---

##  How to Run

1. Install Python 3.x.  
2. Install dependencies:  
   ```bash
   pip install pygame
