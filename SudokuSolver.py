import tkinter as tk
from tkinter import messagebox

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == num:
                return True
    return False

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)

def solve_sudoku(grid):
    l = [0, 0]

    if not find_empty_location(grid, l):
        return True

    row, col = l[0], l[1]

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def solve():
    # Convert the entries into a 2D list representing the Sudoku grid
    grid = [[int(entries[i][j].get()) for j in range(9)] for i in range(9)]
    
    # Call the solve_sudoku function to solve the puzzle
    if solve_sudoku(grid):
        # If the puzzle is solved, update the entries with the solution
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, grid[i][j])
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

def clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(root, width=3, justify='center')
        entries[i][j].grid(row=i, column=j)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve)
solve_button.grid(row=9, column=0, columnspan=4, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=9, column=5, columnspan=4, pady=5)

root.mainloop()
