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


def get_puzzle_input():
    print(f"Chose an input method: \n"
    "1. Enter the puzzle as a single line.\n"
    "2. Enter the puzzle row by row.\n"
    "3. Choose a preset puzzle.\n")
    input_choice = input("Enter your choice (1-3): ")

    if input_choice == '1':
        return get_input_single_line()
    elif input_choice == '2':
        return get_input_row_by_row()
    elif input_choice == '3':
        return get_preset_puzzle()
    else:
        print("Invalid choice. Please try again.")
        return get_puzzle_input()


# The following function checks if the puzzle is valid before solving it.
def is_puzzle_valid(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num != 0:
                grid[row][col] = 0
                if not is_valid(grid, num, (row, col)):
                    grid[row][col] = num  # Restore the number
                    return False
                grid[row][col] = num  # Restore the number
    return True


# The following function gets the user's input and returns it as a string.
# If the input is not 81 characters long, the function will prompt the user to enter a new input. 
def get_input_single_line():
    user_input = input("Please enter the puzzle in a single line: (Enter '0' for an empty space)\n")
    if len(user_input) != 81 or not user_input.isdigit():
        print("Invalid input. Please enter exactly 81 characters.")
        return get_input_single_line()
    else:
        return user_input

# The following function prompts the user to enter the puzzle row by row.
def get_input_row_by_row():
    input_grid = []
    print("Please enter the puzzle row by row, press Enter for next row: (Enter '0' for an empty space)\n")
    for row in range(9):
        while True:
            user_input = input(f"Row {row+1}: ")
            if len(user_input) != 9 or not user_input.isdigit():
                print("Invalid Input. Please enter exactly 9 digits (0-9).")
            else:
                input_grid.append(user_input)
                break
    return ''.join(input_grid)

# The following function prompts the user to choose a preset puzzle. They can choose from one of three predefined puzzles.   
def get_preset_puzzle():
    puzzles = {

        '1': ('Very Easy Puzzle', '000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
        '2': ('Easy Puzzle', '530070000600195000098000060800060003400803001700020006060000280000419005000080079'),
        '3': ('Medium Puzzle', '006002100900600048070800009300020060000703000040050003200009030810006002007100400'),
        '4': ('Hard Puzzle', '000000907000420180000705026100904000050000040000507009920108000034059000507000000')
    }

    print("Select a preset puzzle:")
    for key, (name, _) in puzzles.items():
        print(f"{key}. {name}")
    choice = input("Enter your choice: ")

    if choice in puzzles:
        return puzzles[choice][1]
    else:
        print("Invalid choice. Please try again.")
        return get_preset_puzzle()


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
def solve_sudoku(grid, start_time, original_grid=None, visualization_speed=0.04):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return True  # Puzzle solved
    else:
        row, col = empty_cell  # Position of empty cell

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            # Visualization
            os.system('cls' if os.name == 'nt' else 'clear')
            elapsed_time = time.time() - start_time
            print_grid(grid, original_grid, (row, col), elapsed_time=elapsed_time)
            time.sleep(visualization_speed)

            if solve_sudoku(grid, start_time, original_grid, visualization_speed):
                return True

            grid[row][col] = 0

            # Visualization after backtracking
            os.system('cls' if os.name == 'nt' else 'clear')
            elapsed_time = time.time() - start_time
            print_grid(grid, original_grid, (row, col), backtracking=True, elapsed_time=elapsed_time)
            time.sleep(visualization_speed)

    return False



# The following function prints the grid with the current number being tried in red,
# the original number in white, and the number placed during solving in blue.
def print_grid(grid, original_grid=None, current_pos=None, backtracking=False, elapsed_time=None):
    # Display elapsed time if provided
    if elapsed_time is not None:
        print(f"Time elapsed: {elapsed_time:.2f} seconds\n")
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
                if backtracking:
                    # Backtracking step in yellow
                    print(f"{YELLOW}{num}{RESET} ", end="")
                else:
                    # Current number being tried in red
                    print(f"{RED}{num}{RESET} ", end="")
            else:
                # Numbers placed during solving in green
                print(f"{GREEN}{num}{RESET} ", end="")
        print()

def get_visualization_speed():
    while True:
        speed_input = input("Enter visualization speed in seconds (e.g., 0.1). Press Enter for default speed (0.04): ")
        if speed_input == '':
            return 0.04  # Default speed
        try:
            speed = float(speed_input)
            if speed >= 0:
                return speed
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    puzzle_input = get_puzzle_input()
    try:
        grid = parse_puzzle(puzzle_input)
    except ValueError as e:
        print(f"Error: {e}")
        return

    original_grid = [row[:] for row in grid]
    if not is_puzzle_valid(grid):
        print("The puzzle is invalid and cannot be solved.")
        return

    visualization_speed = get_visualization_speed()
    start_time = time.time()  # Start timing

    if solve_sudoku(grid, start_time, original_grid, visualization_speed):
        end_time = time.time()  # End timing
        total_time = end_time - start_time
        print("The puzzle has been solved")
        print_grid(grid, original_grid)
        print(f"Time taken to solve: {total_time:.2f} seconds")
    else:
        print("No solution exists for the given puzzle.")


if __name__ == "__main__":
    main()
 
