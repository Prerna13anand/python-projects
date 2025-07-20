# Matrix Operations Tool

A command-line tool for performing basic matrix operations using Python and NumPy.

## Features
- Matrix addition
- Matrix subtraction
- Matrix multiplication (dot product and element-wise)
- Matrix transpose
- Determinant calculation

## Requirements
- Python 3.7+
- NumPy

## Setup
1. (Optional) Create and activate a virtual environment:
   ```shell
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```
2. Install dependencies:
   ```shell
   pip install -r requirements.txt
   ```

## Usage
Run the script and follow the prompts:
```shell
python matrix_operations.py
```

## Example
```
Matrix Operations Tool (NumPy)
Available operations:
1. Addition
2. Subtraction
3. Multiplication (dot product)
4. Element-wise Multiplication
5. Transpose
6. Determinant
Select operation (1-6): 1
Enter first matrix:
Enter number of rows: 2
Enter number of columns: 2
Enter the matrix values row by row, separated by spaces:
Row 1: 1 2
Row 2: 3 4
Enter second matrix:
Enter number of rows: 2
Enter number of columns: 2
Enter the matrix values row by row, separated by spaces:
Row 1: 5 6
Row 2: 7 8

Sum:
6.00 8.00
10.00 12.00
```

## License
MIT