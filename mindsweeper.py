import random

# Create a board for the Minesweeper game
size = 8  # Size of the board (8x8)
mines_count = 10  # Number of mines

# Create a blank board
board = [[" " for _ in range(size)] for _ in range(size)]
mines = set()  # To store the positions of the mines

# Randomly place mines on the board
while len(mines) < mines_count:
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    mines.add((row, col))

# Function to count adjacent mines
def count_adjacent_mines(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            r, c = row + i, col + j
            if 0 <= r < size and 0 <= c < size and (r, c) in mines:
                count += 1
    return count

# Function to display the board
def display_board(board):
    print("   " + " ".join([str(i) for i in range(size)]))
    print("  " + "--" * size)
    for i in range(size):
        print(f"{i} | " + " ".join(board[i]))
    print()

# Uncover cells using recursion
def uncover(row, col, revealed):
    if (row, col) in revealed or row < 0 or row >= size or col < 0 or col >= size:
        return
    revealed.add((row, col))
    adjacent_mines = count_adjacent_mines(row, col)
    if adjacent_mines > 0:
        board[row][col] = str(adjacent_mines)
    else:
        board[row][col] = "0"
        # Recursively uncover neighbors if no mines are adjacent
        for i in range(-1, 2):
            for j in range(-1, 2):
                uncover(row + i, col + j, revealed)

# Main game loop
def play_game():
    revealed = set()
    while True:
        display_board(board)
        try:
            row, col = map(int, input("Enter row and column to uncover (e.g., 1 2): ").split())
        except ValueError:
            print("Please enter valid row and column numbers.")
            continue
        
        # Check if the input is within the valid range
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Invalid input. Try again.")
            continue
        
        # Check if the player hit a mine
        if (row, col) in mines:
            print("Game Over! You hit a mine.")
            for r, c in mines:
                board[r][c] = "X"  # Reveal all mines
            display_board(board)
            break
        
        # Uncover the cell if it's not a mine
        uncover(row, col, revealed)
        
        # Check if the player has uncovered all non-mine cells
        if len(revealed) == size * size - mines_count:
            display_board(board)
            print("Congratulations! You won!")
            break

# Start the game
play_game()
