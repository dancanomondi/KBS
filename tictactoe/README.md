# Tic-Tac-Toe with Minimax Algorithm

This repository contains Python implementations of the classic game Tic-Tac-Toe, where you can play against an AI opponent that uses the Minimax algorithm for decision-making. There are two versions available:

1. Basic Minimax Tic-Tac-Toe: An implementation of the game where the AI opponent uses the Minimax algorithm without Alpha-Beta Pruning.
2. Improved Minimax Tic-Tac-Toe: An enhanced version of the game where the AI opponent uses the Minimax algorithm with Alpha-Beta Pruning for more efficient decision-making.

## How to Run

1. Clone the repository or download the relevant files.

2. Open your terminal or command prompt and navigate to the directory containing the downloaded files.

3. Choose the version you want to play:

   - For the basic Minimax version, run the following command:

     ```
     python basic_tic_tac_toe.py
     ```

   - For the improved Minimax version with Alpha-Beta Pruning, run the following command:
     ```
     python improved_tic_tac_toe.py
     ```

4. Follow the on-screen instructions to play the game. You'll be prompted to enter your moves as row and column coordinates (0-2).

## Rules

The game follows the standard rules of Tic-Tac-Toe:

- Players take turns to place their symbol ('X' or 'O') on the board.
- The goal is to get three of your symbols in a row, column, or diagonal.
- If the board is filled without either player achieving a winning combination, the game is a draw.

## Notes

- The AI opponent in the basic Minimax version uses the Minimax algorithm for decision-making, but it may take longer to make moves and is less efficient compared to the improved version.
- The improved Minimax version with Alpha-Beta Pruning enhances the efficiency of the AI opponent's decision-making process, resulting in faster moves and better performance.

Enjoy playing Tic-Tac-Toe against the AI opponent!

---

**Disclaimer:** This implementation serves as a basic demonstration of the Minimax algorithm and Alpha-Beta Pruning in the context of Tic-Tac-Toe. It may not be optimal for other applications or more complex games.
