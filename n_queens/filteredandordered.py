import time

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def apply_arc_consistency(board, row, col):
    for i in range(col + 1, len(board)):
        if board[row][i] == 0:
            board[row][i] = -1

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True
    
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            apply_arc_consistency(board, row, col)
            if solve_n_queens_util(board, col + 1):
                return True
            board[row][col] = 0
            restore_board(board, row, col)
    
    return False

def restore_board(board, row, col):
    for i in range(col + 1, len(board)):
        if board[row][i] == -1:
            board[row][i] = 0

def print_solution(board):
    for row in board:
        print(" ".join(["♛" if val == 1 else "■" for val in row]))
    print()

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens_util(board, 0) is False:
        print("Solution does not exist.")
        return
    
    print("Solution:")
    print_solution(board)

num_queens = int(input("How many queens: "))

start_time = time.time()
solve_n_queens(num_queens)
end_time = time.time()

print(f"Time taken: {end_time - start_time:.6f} seconds")
