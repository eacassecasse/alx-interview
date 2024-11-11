# 0x05. N Queens Project

## Overview
The **N Queens** problem is a well-known challenge in computer science and mathematics, where the goal is to place N queens on an N×N chessboard in such a way that no two queens threaten each other. This project requires implementing a solution to this problem using a backtracking algorithm in Python, showcasing problem-solving and algorithmic skills.

## Concepts Needed

### Backtracking Algorithms
The solution involves exploring all possible board configurations by placing queens one by one and backtracking if a configuration does not lead to a valid solution.

- **Key Resource:** [Introduction to Backtracking](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)

### Recursion
The backtracking process is implemented using recursive functions to handle the placement of queens in each row of the board.

- **Key Resource:** [Recursion in Python](https://realpython.com/python-thinking-recursively/)

### List Manipulations in Python
Lists are used to store queen positions on the board. Understanding how to manipulate lists is essential for adding, checking, and removing queens as part of the backtracking process.

- **Key Resource:** [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Python Command Line Arguments
This project handles input from the command line to specify the board size (N). You’ll need to use the `sys` module to handle command-line arguments.

- **Key Resource:** [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

## Additional Resources
- **Mock Interview Practice:** [N Queens Problem Mock Interview](https://www.youtube.com/watch?feature=shared&v=GneS80iYa7I)

## Requirements

### General
- **Editors Allowed:** `vi`, `vim`, `emacs`
- **Environment:** All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- **PEP 8 Compliance:** Code should follow PEP 8 style guidelines (version 1.7.*)
- **Executable Files:** Ensure all files are executable.
- **Mandatory README:** A `README.md` file must be present in the project root.
- **Shebang:** The first line of all files should be `#!/usr/bin/python3`
- **Output Format:** Solutions are printed one per line, formatted as lists of queen positions.

### Tasks

#### 0. N Queens
Implement a program that solves the N Queens problem, adhering to the following guidelines:

- **Usage:** `nqueens N`
- If the program is run with an incorrect number of arguments, it should output:
  ```
  Usage: nqueens N
  ```
  and exit with status `1`.
- **N Validation:**
  - If `N` is not an integer, print:
    ```
    N must be a number
    ```
    and exit with status `1`.
  - If `N` is less than `4`, print:
    ```
    N must be at least 4
    ```
    and exit with status `1`.
- **Output Requirements:**
  - Print each possible solution for the given N.
  - Solutions are output as lists of queen positions for each configuration.
  - There is no specific required order for solutions.
- **Dependencies:** Only the `sys` module is allowed.

#### Example Usage

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
