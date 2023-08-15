import random

def print_board(board):
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

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def evaluate(board):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    return 0

def alphabeta(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = alphabeta(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = alphabeta(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def computer_move(board):
    best_move = None
    best_eval = -float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_eval = alphabeta(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    
    if best_move is not None:
        board[best_move[0]][best_move[1]] = 'X'

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

if __name__ == "__main__":
    main()
