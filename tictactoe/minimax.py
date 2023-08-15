import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("---------------------------")
    border = "+---" * 3 + "+"
    print(border)
    for i in range(3):
        for row in zip(*board[i]):
            print("|", end=" ")
            print(" | ".join(row), end=" ")
            print("|")
        print(border)
        if i < 2:
            print("+---" * 3 + "+")

# Function to check if a player has won
def is_winner(board, player):
    # Check rows and columns for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals for a win
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to evaluate the current state of the board
def evaluate(board):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    return 0

# Minimax algorithm to determine the best move
def minimax(board, depth, is_maximizing):
    # Base cases: check for wins or a full board
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        # Try all possible moves and find the best evaluation
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        # Try all possible moves and find the worst evaluation for the opponent
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function for the computer's move using minimax
def computer_move(board):
    best_move = None
    best_eval = -float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_eval = minimax(board, 0, False)
                board[i][j] = ' '
                
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    
    if best_move is not None:
        board[best_move[0]][best_move[1]] = 'X'

# Main game loop
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'O'
    
    while True:
        print_board(board)
        
        if player == 'O':
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
            board[row][col] = 'O'
        else:
            computer_move(board)
        
        if is_winner(board, player):
            print_board(board)
            print(f"{player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        player = 'X' if player == 'O' else 'O'

# Entry point of the program
if __name__ == "__main__":
    main()
