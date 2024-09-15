import time
import os

# Program Description:
# This program solves Sudoku puzzles by backtracking through the grid and checking if the puzzle is solvable.

# Below are two examples of solvable and unsolvable puzzles:
# Example input for solvable puzzle:   530070000600195000098000060800060003400803001700020006060000280000419005000080079
# Example input for unsolvable puzzle: 530570000600195000098000060800060003400803001700020006060000280000419005000080079

# Defining the ANSI color codes:
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

# The following function gets the user's input and returns it as a string.
# If the input is not 81 characters long, the function will prompt the user to enter a new input. 
def get_puzzle_input():
    user_input = input("Please enter the puzzle in a single line: (Enter '0' for an empty space)\n")
    if len(user_input) != 81:
        print("Invalid input. Please enter exactly 81 characters.")
        return get_puzzle_input()
    else:
        return user_input

# The following function parses the user's input into a 9x9 grid.
def parse_puzzle(puzzle_input):
    grid = []

    for i in range(0,81,9):
        row_string = puzzle_input[i:i+9]
        row = []
        for char in row_string:
            row.append(int(char))
        grid.append(row)
    return grid

# The following function finds the next empty cell in the grid.
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row,col)
    return None

# The following function checks if the number is valid in the grid at the given position.
# It checks if the number is already in the row, column, or subgrid.
def is_valid(grid,num,pos):
    # check the row for any matching numbers except itself
    for col in range(9):
        if grid[pos[0]][col] == num and pos[1] != col:
            return False
    # check the col for any matching numbers except itself
    for row in range(9):
        if grid[row][pos[1]] == num and pos[0] != row:
            return False

    # Determine the subgrid we are in
    box_row_start = (pos[0] // 3) * 3
    box_col_start = (pos[1] // 3) * 3

    # check for matching numbers in the subgrid by position
    for row in range(box_row_start, box_row_start + 3):
        for col in range(box_col_start, box_col_start +3):
            if grid[row][col] == num and (row,col) != pos:
                return False
    return True

# The following function solves the Sudoku puzzle by backtracking through the grid and checking if the puzzle is solvable.
# If the puzzle is solvable, the function returns True. Otherwise, it returns False.
def solve_sudoku(grid, original_grid=None):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return True  # Puzzle solved
    else:
        row, col = empty_cell # Position of empty cell

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            # Visualization
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the console depending on OS
            print_grid(grid, original_grid, (row, col)) 
            time.sleep(0.01) # Sleep for 0.01 seconds to create animation
            if solve_sudoku(grid, original_grid):
                return True

            grid[row][col] = 0
            # Visualization after backtracking
            os.system('cls' if os.name == 'nt' else 'clear')
            print_grid(grid, original_grid, (row, col))
            time.sleep(0.01)

    return False

# The following function prints the grid with the current number being tried in red,
# the original number in white, and the number placed during solving in blue.
def print_grid(grid, original_grid=None, current_pos=None):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 25)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            num = grid[row][col]
            if num == 0:
                print(". ", end="")
            elif original_grid and original_grid[row][col] == num:
                # Original number in white
                print(f"{WHITE}{num}{RESET} ", end="")
            elif current_pos and (row, col) == current_pos:
                # Current number being tried in red
                print(f"{RED}{num}{RESET} ", end="")
            else:
                # Numbers placed during solving in green
                print(f"{GREEN}{num}{RESET} ", end="")
        print()


def main():

    puzzle_input = get_puzzle_input()
    try:
        grid = parse_puzzle(puzzle_input)
    except ValueError as e:
        print(f"Error: {e}")
        return

    original_grid = [row[:] for row in grid]


    if solve_sudoku(grid, original_grid):
        print("The puzzle has been solved")
        print_grid(grid, original_grid)
    else:
        print("The puzzle cannot be solved")
    

if __name__ == "__main__":
    main()
 
