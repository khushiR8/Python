import random

# Function to print the Sudoku board
def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

# Check if the number can be placed in the board at the given position
def is_valid(board, num, pos):
    # Check the row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# Function to solve the Sudoku board using backtracking
def solve(board):
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Function to find the next empty position in the board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Generate a Sudoku puzzle by filling the board randomly
def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    remove_numbers(board)
    return board

# Fill the board with a valid Sudoku solution
def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if not find_empty(board) or fill_board(board):
                            return True
                        board[i][j] = 0
                return False

# Remove numbers to create a puzzle (keep it solvable)
def remove_numbers(board):
    num_to_remove = random.randint(40, 50)
    for _ in range(num_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0

# Sample Sudoku game execution
if __name__ == "__main__":
    board = generate_board()
    print("Sudoku Puzzle:")
    print_board(board)

    if solve(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists.")
