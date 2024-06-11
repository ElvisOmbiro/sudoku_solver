import sys

def read_file(textfile):
    with open(textfile, 'r') as f:
        next(f)
        i = 0
        matrix = [[0 for _ in range(9)] for _ in range(9)]
        while True:
            j = 0
            char = f.readline()
            for c in char:
                if c.isdigit():  # Ensuring only digits are processed
                    matrix[i][j] = int(c)
                    j += 1
                    if j == 9:
                        i += 1
                        break
            if i == 9:
                break
    return matrix

def check_sudoku(row, column, number, matrix_board):
    for i in range(9):
        if matrix_board[row][i] == number or matrix_board[i][column] == number:
            return False

    start_row, start_col = row - row % 3, column - column % 3
    for i in range(3):
        for j in range(3):
            if matrix_board[start_row + i][start_col + j] == number:
                return False

    return True

class Calls:
    number_of_calls = 0

c = Calls()

def sudoku_solver(matrix):
    c.number_of_calls += 1
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                for num in range(1, 10):
                    if check_sudoku(i, j, num, matrix):
                        matrix[i][j] = num
                        if sudoku_solver(matrix):
                            return True
                        matrix[i][j] = 0
                return False

    print("Naive Backtracking Algorithm Solution: ")
    for row in matrix:
        print(row)
    print("Amount of Recursions:", c.number_of_calls)
    sys.exit(0)

if len(sys.argv) < 2:
    print("Usage: python sudoku.py <input_file>")
    sys.exit(1)

matrix = read_file(sys.argv[1])
sudoku_solver(matrix)

