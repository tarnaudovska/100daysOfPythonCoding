# 🐍 Snake Game with Python and Turtle 🐢

This is a simple Snake game developed in Python using the `turtle` graphics module. The game allows the user to control a snake and eat food that grows the snake longer. The goal is to avoid hitting the walls or the snake's own body while eating as much food as possible to score points.

## Features
- **Snake Movement**: Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to move the snake around the screen.
- **Scoreboard**: A dynamic scoreboard that updates when the snake eats food.
- **Game Over Conditions**: The game ends when the snake collides with the wall or itself.
- **Food**: Randomly appearing food that the snake eats to grow longer and increase the score.

## How It Works
1. **Setup**:
   The game starts with a black screen of size 600x600 pixels. The game window displays the title "Snake game" and the game area is bounded by walls.
   
2. **Snake**:
   The snake is represented by a collection of segments that move together. Each time the snake eats food, it grows by one segment.
   
3. **Food**:
   Randomly generated food appears on the screen. When the snake’s head collides with the food, it eats the food and grows longer. The score increases accordingly.

4. **Collision Detection**:
   The game checks for collisions with the food, walls, and the snake’s own body. The game ends when any of these collisions occur.

## Installation

To play the game, you need Python installed on your computer. The game relies on the **Turtle** module, which is built into Python, so no additional installations are required.

1. Clone the repository or download the Python files.
2. Run the `main.py` file in your terminal or IDE.