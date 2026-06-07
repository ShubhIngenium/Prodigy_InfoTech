# Sudoku Solver

This is a Python program that automatically solves Sudoku puzzles using a backtracking algorithm.

## Features

- Reads an input puzzle from the user or uses a predefined example
- Uses backtracking to search for valid number placements
- Validates rows, columns, and 3x3 subgrids
- Prints the solved Sudoku grid when a solution is found

## Usage

Run the solver with:

```bash
python SudokuSolver.py
```

The program prompts for manual input first. If you choose not to enter a puzzle manually, it solves a default example.

## Puzzle Format

- Empty cells are represented by `0` or `.`
- Enter one row at a time, with exactly 9 values per row
- Spaces are optional

## Example Output

```text
Unsolved Sudoku:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Solved Sudoku:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Notes

- The solver currently uses a fixed example puzzle, but the grid can be modified directly in `SudokuSolver.py`.
- If no valid solution exists, the program prints a message instead.
