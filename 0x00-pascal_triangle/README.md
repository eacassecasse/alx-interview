# 0x00. Pascal's Triangle

## Description

This project focuses on creating a Python function that generates Pascal's Triangle up to a specified number of rows. Pascal’s Triangle is a triangular array of numbers, where each number is the sum of the two numbers directly above it.

The project serves as a practical exercise for working with Python lists, loops, conditional statements, and potentially recursion. It helps reinforce important Python programming concepts while exploring a mathematical structure.

## Learning Objectives

By the end of this project, you will be able to:

- Explain what Pascal’s Triangle is.
- Implement Python functions to generate Pascal’s Triangle.
- Utilize Python lists and list comprehensions effectively.
- Understand and apply loops and conditional statements.
- Consider the time and space complexity of your solution.
- Optionally, explore recursive approaches and handle potential errors efficiently.

## Requirements

- All Python files will be interpreted/compiled on **Ubuntu 18.04 LTS** using Python 3.8.x.
- All code should follow the **PEP 8** style guide.
- A `README.md` file at the root of the project folder is **mandatory**.
- You must use the `py` extension for Python files.
- Your code will be tested using Python’s unittest framework.
- You must export and import all functions used.

## Concepts to Review

To successfully complete this project, it's essential to revise the following Python concepts:

### 1. Lists and List Comprehensions
- Learn how to create, access, modify, and iterate over lists.
- Use list comprehensions for concise code, especially when generating rows of Pascal’s Triangle.

### 2. Functions
- Define and call functions, pass parameters, and return values.
- Implement a function that returns a list of lists representing Pascal’s Triangle.

### 3. Loops
- Use `for` loops to iterate through sequences.
- Use nested loops for generating each row and calculating values.

### 4. Conditional Statements
- Apply `if`, `elif`, and `else` conditions, ensuring edge values are always 1 in Pascal’s Triangle.

### 5. Arithmetic Operations
- Use addition for calculating each element in Pascal’s Triangle.

### 6. Indexing and Slicing
- Access elements and slices of lists for identifying and summing the correct values when constructing the triangle.

### 7. Optional Topics
- **Recursion**: Understand how recursion can be applied to Pascal’s Triangle.
- **Error and Exception Handling**: Handle errors such as invalid input types or negative values.
- **Efficiency and Optimization**: Evaluate the complexity of your solution and apply any possible optimizations.

## Task

### 0. Pascal's Triangle (Mandatory)
Write a Python function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s Triangle of `n` rows.

- The function should return an empty list if `n <= 0`.
- You can assume `n` will always be an integer.

#### Example:
```python
>>> pascal_triangle(5)
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```

## Setup

1. Install Python 3.8.x (if not installed).
2. Create the function `pascal_triangle` in a Python file (e.g., `pascal.py`).
3. Test your code using Python’s unittest framework.

## Resources

- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?feature=shared&v=0iMtlus-afo)
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)
- [Mock Technical Interview](https://www.youtube.com/watch?v=1qw5ITr3k9E)

## How to Test

To test your Pascal’s Triangle function, you can write unittests in a separate file:

```python
import unittest
from pascal import pascal_triangle

class TestPascalTriangle(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(pascal_triangle(0), [])
        self.assertEqual(pascal_triangle(1), [[1]])

    def test_normal_cases(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])

if __name__ == "__main__":
    unittest.main()
```

Run the tests with:
```bash
$ python3 -m unittest test_pascal.py
```

## Author
- **Edmilson Cassecasse** - [GitHub Profile](https://github.com/eacassecasse)
