# test_sudoku_solver.py

import unittest
from sudoku_solver import parse_puzzle, is_puzzle_valid, is_valid, find_empty, solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_parse_puzzle_valid_input(self):
        """Test parsing a valid puzzle input string."""
        puzzle_input = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(puzzle_input)
        self.assertEqual(len(grid), 9)
        for row in grid:
            self.assertEqual(len(row), 9)
        # Check specific cell values
        self.assertEqual(grid[0][0], 5)
        self.assertEqual(grid[0][1], 3)
        self.assertEqual(grid[0][4], 7)
        self.assertEqual(grid[8][8], 9)

    def test_parse_puzzle_invalid_input(self):
        """Test parsing invalid puzzle inputs."""
        # Input too short
        short_input = '1234'
        with self.assertRaises(ValueError):
            parse_puzzle(short_input)

        # Input with invalid characters
        invalid_chars_input = 'x' * 81
        with self.assertRaises(ValueError):
            parse_puzzle(invalid_chars_input)

    def test_is_puzzle_valid_valid_puzzle(self):
        """Test is_puzzle_valid with a valid puzzle."""
        puzzle_input = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(puzzle_input)
        self.assertTrue(is_puzzle_valid(grid))

    def test_is_puzzle_valid_invalid_puzzle(self):
        """Test is_puzzle_valid with an invalid puzzle."""
        # Duplicate number in a row
        invalid_puzzle_row = '530570000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(invalid_puzzle_row)
        self.assertFalse(is_puzzle_valid(grid))

        # Duplicate number in a column
        invalid_puzzle_col = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(invalid_puzzle_col)
        grid[0][1] = 6  # Place a duplicate '6' in column 1
        self.assertFalse(is_puzzle_valid(grid))

        # Duplicate number in a box
        grid = parse_puzzle(invalid_puzzle_col)
        grid[1][1] = 5  # Place a duplicate '5' in the top-left box
        self.assertFalse(is_puzzle_valid(grid))

    def test_is_valid(self):
        """Test the is_valid function."""
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        # Test valid placements
        self.assertTrue(is_valid(grid, 2, (0, 2)))
        self.assertTrue(is_valid(grid, 1, (2, 2)))
        # Test invalid placements
        self.assertFalse(is_valid(grid, 3, (0, 2)))  # Duplicate in row
        self.assertFalse(is_valid(grid, 6, (0, 2)))  # Duplicate in column
        self.assertFalse(is_valid(grid, 9, (0, 2)))  # Duplicate in box

    def test_find_empty(self):
        """Test the find_empty function."""
        grid_full = [[1]*9 for _ in range(9)]
        self.assertIsNone(find_empty(grid_full))
        grid_with_empty = [[1]*9 for _ in range(9)]
        grid_with_empty[4][5] = 0
        self.assertEqual(find_empty(grid_with_empty), (4, 5))

    def test_solve_sudoku_valid_puzzle(self):
        """Test solving a valid puzzle."""
        puzzle_input = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(puzzle_input)
        original_grid = [row[:] for row in grid]
        start_time = 0  # Not used in testing
        visualization_speed = 0  # No delay during testing
        result = solve_sudoku(grid, start_time, original_grid, visualization_speed)
        self.assertTrue(result)
        # Check that the grid is fully solved (no zeros)
        for row in grid:
            self.assertNotIn(0, row)
        # Check that the solution is valid
        self.assertTrue(is_puzzle_valid(grid))

    def test_solve_sudoku_invalid_puzzle(self):
        """Test attempting to solve an invalid puzzle."""
        puzzle_input = '530570000600195000098000060800060003400803001700020006060000280000419005000080079'
        grid = parse_puzzle(puzzle_input)
        original_grid = [row[:] for row in grid]
        start_time = 0
        visualization_speed = 0
        result = solve_sudoku(grid, start_time, original_grid, visualization_speed)
        self.assertFalse(result)

    def test_solve_sudoku_hard_puzzle(self):
        """Test solving a hard puzzle."""
        puzzle_input = '000000907000420180000705026100904000050000040000507009920108000034059000507000000'
        grid = parse_puzzle(puzzle_input)
        original_grid = [row[:] for row in grid]
        start_time = 0
        visualization_speed = 0
        result = solve_sudoku(grid, start_time, original_grid, visualization_speed)
        self.assertTrue(result)
        # Check that the grid is fully solved (no zeros)
        for row in grid:
            self.assertNotIn(0, row)
        # Check that the solution is valid
        self.assertTrue(is_puzzle_valid(grid))

if __name__ == '__main__':
    unittest.main()
