import random

print("Welcome to Connect Four!")
print("-------------------------")

# Column labels (A to G)
COLUMN_LABELS = ["A", "B", "C", "D", "E", "F", "G"]

ROWS = 6
COLS = 7

# Create empty 6×7 board
board = [["" for _ in range(COLS)] for _ in range(ROWS)]


# ─────────────────────────────────────────────
# PRINT THE BOARD
# ─────────────────────────────────────────────
def print_board():
    print("\n       A    B    C    D    E    F    G")
    for r in range(ROWS):
        print("     +----+----+----+----+----+----+----+")
        print(f"   {r} |", end="")
        for c in range(COLS):
            cell = board[r][c]
            if cell == "":
                print("    |", end="")
            else:
                print(f" {cell} |", end="")
        print()
    print("     +----+----+----+----+----+----+----+")


# ─────────────────────────────────────────────
# DROP A PIECE INTO A COLUMN
# ─────────────────────────────────────────────
def drop_piece(col, piece):
    """
    Takes a column index (0–6) and places the piece in
    the lowest empty row. Returns (row, col) or None if column is full.
    """
    for row in range(ROWS - 1, -1, -1):  # start from bottom row
        if board[row][col] == "":
            board[row][col] = piece
            return (row, col)
    return None  # column full


# ─────────────────────────────────────────────
# CHECK IF THE PLAYER WON
# ─────────────────────────────────────────────
def check_winner(piece):
    # Horizontal win
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (
                board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece
            ):
                return True

    # Vertical win
    for r in range(ROWS - 3):
        for c in range(COLS):
            if (
                board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece
            ):
                return True

    # Diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (
                board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece
            ):
                return True

    # Diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (
                board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece
            ):
                return True

    return False


# ─────────────────────────────────────────────
# CHECK FOR DRAW
# ─────────────────────────────────────────────
def is_draw():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "":
                return False
    return True


# ─────────────────────────────────────────────
# MAIN GAME LOOP
# ─────────────────────────────────────────────
current_player = "🔴"  # red starts first

print_board()

while True:
    print(f"\nPlayer {current_player}, it's your turn!")
    
    # Ask for column input
    move = input("Choose a column (A-G): ").upper()

    # Validate column
    if move not in COLUMN_LABELS:
        print("Invalid input. Choose a letter between A and G.")
        continue

    col = COLUMN_LABELS.index(move)

    # Try placing the piece
    position = drop_piece(col, current_player)

    if position is None:
        print("That column is full. Try another one.")
        continue

    print_board()

    # Check winner
    if check_winner(current_player):
        print(f"\n🎉 Player {current_player} wins! 🎉")
        break

    # Check draw
    if is_draw():
        print("\nIt's a draw! Board is full.")
        break

    # Switch turns
    current_player = "🔵" if current_player == "🔴" else "🔴"
