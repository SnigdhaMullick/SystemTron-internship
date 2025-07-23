import random

# Welcome message
print("Welcome to Connect Four")
print("------------------------")

# Game setup
possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows, cols = 6, 7

# Function to print the game board
def printGameBoard():
    print("\n     A    B    C    D    E    F    G")
    print("   +----+----+----+----+----+----+----+")
    for i in range(rows):
        print(f" {i} |", end="")
        for j in range(cols):
            cell = gameBoard[i][j]
            if cell == "🔵" or cell == "🔴":
                print(f" {cell} |", end="")
            else:
                print("    |", end="")
        print("\n   +----+----+----+----+----+----+----+")
    print()

# Drop piece in the selected column
def dropPiece(col, piece):
    for row in reversed(range(rows)):
        if gameBoard[row][col] == "":
            gameBoard[row][col] = piece
            return True
    return False  # Column full

# Check if input is valid
def isValidInput(inp):
    return inp in possibleLetters

# Main game loop
turnCounter = 0
while True:
    printGameBoard()
    currentPlayer = "Player 1" if turnCounter % 2 == 0 else "Player 2"
    currentPiece = "🔴" if turnCounter % 2 == 0 else "🔵"

    userInput = input(f"{currentPlayer} ({currentPiece}), choose a column (A-G): ").upper()

    if not isValidInput(userInput):
        print("Invalid input. Please choose a column from A to G.")
        continue

    column = possibleLetters.index(userInput)

    if not dropPiece(column, currentPiece):
        print("That column is full. Try another one.")
        continue

    # Optional: Check for win condition here (horizontal, vertical, diagonal)

    turnCounter += 1

    # Optional: Add draw condition
    if turnCounter == rows * cols:
        printGameBoard()
        print("Game Over! It's a draw.")
        break