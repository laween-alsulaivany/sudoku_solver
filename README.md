# **Sudoku Solver**

A command-line Sudoku solver written in Python, utilizing a backtracking algorithm with visualization. The program allows users to input Sudoku puzzles in various ways and provides a step-by-step visual representation of the solving process.

## **Table of Contents**

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Methods](#input-methods)
- [Project Structure](#project-structure)


---

## **Features**

- **Multiple Input Methods:**
  - Enter the puzzle as a single line.
  - Enter the puzzle row by row.
  - Choose from preset puzzles (Easy, Medium, Hard, Very Easy).
- **Visualization:**
  - Step-by-step visualization of the solving process in the console.
  - Adjustable visualization speed.
  - Color-coded output:
    - **White**: Original numbers.
    - **Green**: Numbers placed during solving.
    - **Red**: Current number being tried.
    - **Yellow**: Backtracking steps.
- **Puzzle Validation:**
  - Validates the input puzzle for correctness before attempting to solve.
- **Time Tracking:**
  - Displays the elapsed time during the solving process.
  - Shows total time taken to solve the puzzle upon completion.

## **Requirements**

- Python 3.x

## **Installation**

 **Clone the Repository:**

   ```bash
   git clone https://github.com/laween-alsulaivany/sudoku-solver.git
   cd sudoku-solver
   ```

## **Usage**

1. **Running the Program**

To run the Sudoku solver, execute the following command in your terminal:

   ```bash
    python sudoku_solver.py
```

## **Input Methods**
Upon running the program, you will be prompted to choose an input method:

###  1. Enter the puzzle as a single line: 

- Input 81 digits in a single line, using 0 or . for empty cells.
- Example:

    ```bash
    530070000600195000098000060800060003400803001700020006060000280000419005000080079
    ```

### 2. Enter the puzzle row by row:

- Input the puzzle one row at a time, entering 9 digits per row.
- Use 0 or . for empty cells.
- Example:
```bash
Row 1: 530070000
Row 2: 600195000
...
```

### 3. Choose a preset puzzle:

Select from predefined puzzles:
- Easy Puzzle
- Medium Puzzle
- Hard Puzzle
- Very Easy Puzzle (for quick testing)

## **Project Structure**

```bash
sudoku-solver/
├── sudoku_solver.py        # Main program file
├── test_sudoku_solver.py   # Unit tests
├── README.md               # Project documentation

```

## **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the Repository

    Click the "Fork" button at the top right of the repository page.

2. Clone Your Fork

    ```bash
        git clone https://github.com/laween-alsulaivany/sudoku-solver.git
        cd sudoku-solver
    ```
3. Create a Feature Branch

    ```bash
        git checkout -b feature/your-feature-name
    ```
4. Make Your Changes

- Implement new features or fix bugs.
- Write or update tests as necessary.

5. Commit and Push

    ```bash
    git add .
    git commit -m "Description of your changes"
    git push origin feature/your-feature-name
    ```

6. Create a Pull Request

- Go to your fork on GitHub.
- Click "Compare & pull request" and submit your PR.
