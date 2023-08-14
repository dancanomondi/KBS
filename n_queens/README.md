# N-Queens Problem Solver

This is a Python program that solves the N-Queens problem using different techniques. It aims to find a placement of N queens on an NxN chessboard such that no two queens threaten each other. The program employs basic backtracking, arc consistency filtering, and heuristic ordering to explore the solution space and efficiently solve the problem.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository or download the `n_queens` folder.

2. Open a terminal and navigate to the `n_queens` directory.

3. Run each version of the program by executing the following command:

   ```bash
   python3 backtracking.py
   python3 filteredandordered.py
   Enter the number of queens (N) when prompted.
   ```

The programs will attempt to find solutions and display the chessboard with the queens' placements if successful. Otherwise, they will indicate that no solution exists.

Approach
Basic Backtracking (backtracking.py)
Place queens one by one in each column, starting from the leftmost column.
Check if the current placement is safe (no queens threaten each other).
If safe, move to the next column and repeat steps 1-2.
If a solution is not possible in the current configuration, backtrack and explore other possibilities.
Filtering and Ordering (filteredandordered.py)
Place queens one by one in each column, starting from the leftmost column.
Apply arc consistency filtering to eliminate unsafe positions for subsequent queens in the same column.
Use heuristic ordering to prioritize safe positions for queens.
If a safe position is found, move to the next column and repeat steps 2-3.
If a solution is not possible in the current configuration, backtrack and explore other possibilities.
File Descriptions
backtracking.py: The main Python script that implements the N-Queens problem solver using basic backtracking.

filteredandordered.py: The main Python script that implements the N-Queens problem solver using backtracking, arc consistency filtering, and heuristic ordering.

Examples
Here are some example solutions for different N values:

yaml
Copy code
How many queens: 4
Solution:
■ ♛ ■ ■
■ ■ ■ ♛
♛ ■ ■ ■
■ ■ ♛ ■

How many queens: 5
Solution does not exist.

Time taken: 0.001234 seconds (for each version)
Contributions
Contributions, bug reports, and feedback are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.
