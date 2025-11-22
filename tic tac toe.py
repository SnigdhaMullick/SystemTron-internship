# -----------------------------
# Simple Tic-Tac-Toe (Humanised)
# -----------------------------

# The game board uses 9 slots (1–9 for users)
board = ["-"] * 9
current_player = "X"
winner = None
game_running = True


# Print the board in a friendly format
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


# Ask the current player for a move
def player_move():
    global current_player

    while True:
        try:
            pos = int(input(f"Player {current_player}, choose a position (1–9): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if pos < 1 or pos > 9:
            print("That number is outside the board! Try again.")
        elif board[pos - 1] != "-":
            print("That spot is already taken. Choose another one.")
        else:
            board[pos - 1] = current_player
            break


# --- Checking Game Conditions ---

# Horizontal win
def check_horizontal():
    line1 = board[0] == board[1] == board[2] != "-"
    line2 = board[3] == board[4] == board[5] != "-"
    line3 = board[6] == board[7] == board[8] != "-"
    return line1 or line2 or line3


# Vertical win
def check_vertical():
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    return col1 or col2 or col3


# Diagonal win
def check_diagonal():
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    return diag1 or diag2


def check_win():
    global winner
    if check_horizontal() or check_vertical() or check_diagonal():
        winner = current_player
        return True
    return False


def check_tie():
    return "-" not in board


# Switch turns
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"


# -----------------------------
#          GAME LOOP
# -----------------------------
print("\nWelcome to Tic-Tac-Toe!\n")

while game_running:
    print_board()
    player_move()

    # Check if someone won
    if check_win():
        print_board()
        print(f"🎉 Player {winner} wins! Congratulations!")
        break

    # Check tie
    if check_tie():
        print_board()
        print("It's a tie! No more spaces left.")
        break

    # Switch turn
    switch_player()
