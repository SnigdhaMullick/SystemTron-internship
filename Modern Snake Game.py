from tkinter import *
import random

# Game constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
INITIAL_SPEED = 150
BODY_PARTS = 3
SNAKE_COLOR = "#4CAF50"
FOOD_COLOR = "#F44336"
BG_COLOR = "#1A1A1A"
TEXT_COLOR = "#FFFFFF"

score = 0
direction = "right"
speed = INITIAL_SPEED
game_running = True # Global flag for game state (running/paused)

# Initialize window
window = Tk()
window.title("Modern Snake Game")
window.config(bg=BG_COLOR)
window.resizable(False, False)

# Score Label
score_label = Label(window, text=f"Score: {score}", font=('Helvetica', 20), bg=BG_COLOR, fg=TEXT_COLOR)
score_label.pack(pady=10)

# Canvas for game
canvas = Canvas(window, bg=BG_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT, highlightthickness=0)
canvas.pack()

# Center the window on screen
window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (GAME_WIDTH / 2))
y = int((screen_height / 2) - (GAME_HEIGHT / 2))
window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT+50}+{x}+{y}")

# Snake class
class Snake:
    def __init__(self): # FIX: Changed _init_ to __init__
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.body = []

        for x, y in self.coordinates:
            segment = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, outline="")
            self.body.append(segment)

# Food class
class Food:
    def __init__(self): # FIX: Changed _init_ to __init__
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.food = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, outline="")

# Change direction
def change_direction(new_dir):
    global direction
    # Prevent snake from immediately reversing direction
    opposites = {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
    if new_dir != opposites.get(direction): # Check against current direction's opposite
        direction = new_dir

# Check collisions
def check_collision(snake):
    x, y = snake.coordinates[0] # Head of the snake

    # Check collision with walls
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    # Check collision with its own body
    # Start from the second segment to avoid self-collision with the head itself
    for body_part in snake.coordinates[1:]:
        if [x, y] == body_part:
            return True
    return False

# Game over display
def game_over():
    global game_running
    game_running = False # Stop the game loop
    canvas.delete(ALL) # Clear everything from the canvas
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 20,
                       text="GAME OVER", fill="red", font=('Helvetica', 36, 'bold'))
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 20,
                       text=f"Final Score: {score}", fill="white", font=('Helvetica', 18))
    # Add a restart button
    restart_button = Button(window, text="Restart", command=restart_game, font=('Helvetica', 16), bg="#333333", fg=TEXT_COLOR, relief="raised", bd=3)
    canvas.create_window(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 80, window=restart_button)


# Main game loop
def next_turn(snake, food):
    global score, speed, game_running

    if not game_running: # If game is paused or over, do not proceed
        return

    x, y = snake.coordinates[0] # Get current head coordinates

    # Update head coordinates based on direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head coordinates and create new head segment
    snake.coordinates.insert(0, [x, y])
    segment = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, outline="")
    snake.body.insert(0, segment)

    # Check if snake ate food
    if [x, y] == food.coordinates:
        score += 1
        score_label.config(text=f"Score: {score}")
        canvas.delete(food.food) # Remove old food
        food = Food() # Create new food
        speed = max(50, speed - 5)  # Increase speed, minimum speed is 50ms
    else:
        # If no food eaten, remove the last segment of the snake to simulate movement
        canvas.delete(snake.body[-1])
        del snake.body[-1]
        del snake.coordinates[-1]

    # Check for collisions
    if check_collision(snake):
        game_over()
    else:
        # Schedule the next turn
        window.after(speed, next_turn, snake, food)

# Restart game function
def restart_game():
    global score, direction, speed, game_running, snake, food

    # Reset game variables
    score = 0
    direction = "right"
    speed = INITIAL_SPEED
    game_running = True

    # Clear canvas
    canvas.delete(ALL)

    # Reset score label
    score_label.config(text=f"Score: {score}")

    # Reinitialize snake and food
    snake = Snake()
    food = Food()

    # Start the game loop again
    next_turn(snake, food)

# Pause/Resume
def toggle_pause(event=None):
    global game_running
    if not game_running: # If game was paused, resume
        game_running = True
        next_turn(snake, food)
    else: # If game was running, pause
        game_running = False
        # No need to call next_turn, it will exit early due to game_running flag

# Bind keys
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<space>', toggle_pause)

# Initial setup and start game
snake = Snake()
food = Food()
next_turn(snake, food) # Start the first turn

window.mainloop()
