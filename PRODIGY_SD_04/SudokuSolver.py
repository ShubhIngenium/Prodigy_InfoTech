def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid(grid, row, col, value):
    if value in grid[row]:
        return False

    for r in range(9):
        if grid[r][col] == value:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == value:
                return False

    return True


def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True

    row, col = empty
    for value in range(1, 10):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False


def parse_puzzle_line(line):
    cleaned = line.replace(" ", "").replace(".", "0")
    if len(cleaned) != 9 or any(ch not in "0123456789" for ch in cleaned):
        raise ValueError("Each row must contain exactly 9 digits or '.' characters.")
    return [int(ch) for ch in cleaned]


def read_puzzle_from_input():
    print("Enter the Sudoku puzzle row by row.")
    print("Use 0 or . for empty cells; spaces are optional.")

    puzzle = []
    while len(puzzle) < 9:
        row_number = len(puzzle) + 1
        row_value = input(f"Row {row_number}: ").strip()
        if not row_value:
            print("Row cannot be empty. Please enter 9 values.")
            continue
        try:
            puzzle.append(parse_puzzle_line(row_value))
        except ValueError as exc:
            print(exc)
            continue

    return puzzle


def main():
    print("Sudoku Solver")
    use_manual = input("Enter puzzle manually? [Y/n]: ").strip().lower()

    if use_manual in ("", "y", "yes"):
        puzzle = read_puzzle_from_input()
    else:
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    print("\nUnsolved Sudoku:")
    print_grid(puzzle)
    print()

    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        print_grid(puzzle)
    else:
        print("No valid solution exists for this puzzle.")


if __name__ == "__main__":
    main()
