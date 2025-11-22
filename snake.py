# ************************************
# Python Snake Game (Humanised Version)
# ************************************

from tkinter import *
import random

# Game settings
GAME_WIDTH = 700
GAME_HEIGHT = 700

# SPEED controls how fast the snake moves.
# Higher value = slower speed.
SPEED = 120        # Reduced from 50 → 120 to slow down the snake

SPACE_SIZE = 50    # Size of each block/square
BODY_PARTS = 3     # Starting length of the snake

SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


# -----------------------------
# Snake Class
# -----------------------------
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Start all body parts at (0,0)
        for _ in range(self.body_size):
            self.coordinates.append([0, 0])

        # Draw each block of the snake on the canvas
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


# -----------------------------
# Food Class
# -----------------------------
class Food:

    def __init__(self):
        # Random food position inside the grid
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Draw food on the canvas
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )


# -----------------------------
# Game Loop - Moves the Snake
# -----------------------------
def next_turn(snake, food):

    x, y = snake.coordinates[0]  # Head of the snake

    # Move direction logic
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head position
    snake.coordinates.insert(0, [x, y])
    new_square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE,
        fill=SNAKE_COLOR
    )
    snake.squares.insert(0, new_square)

    # Food collision check
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")

        canvas.delete("food")
        food = Food()

    else:
        # Remove last block of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        snake.squares.pop()

    # Check for collisions
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


# -----------------------------
# Change Direction
# -----------------------------
def change_direction(new_direction):
    """Ensures snake cannot reverse into itself."""
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


# -----------------------------
# Collision Check
# -----------------------------
def check_collisions(snake):

    x, y = snake.coordinates[0]

    # Border collision
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Self collision
    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True

    return False


# -----------------------------
# Game Over Screen
# -----------------------------
def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=('consolas', 70),
        text="GAME OVER",
        fill="red",
        tag="gameover"
    )


# ---------------------------------------
# Window Setup
# ---------------------------------------
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center the window on the screen
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Keyboard controls
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Start the game
snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
