# snake.py
By Andrew Bostrom

The game snake written in Python.
A 200x200 pixel canvas is created along with a 20x20 square that is the snake. A circular pellet with a diameter of 20 is randomly spawned on the canvas and the goal is for the user to move the snake into the pellet using the arrow keys. When the snake hits the pellet it "eats" it and becomes 1 segment longer (adding another 20x20 square to the snake body), after this another pellet is randomly spawned on the canvas. The player loses when the head of the snake hits a segment of the snake or one of the edges of the canvas.
