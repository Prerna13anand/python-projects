import numpy as np

def get_matrix(prompt):
    print(prompt)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter the matrix values row by row, separated by spaces:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            print("Incorrect number of columns. Please re-enter the row.")
            return get_matrix(prompt)
        matrix.append(row)
    return np.array(matrix)

def print_matrix(mat, label="Result"):
    print(f"\n{label}:")
    for row in mat:
        print(" ".join(f"{val:.2f}" for val in row))

def main():
    print("Matrix Operations Tool (NumPy)")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication (dot product)")
    print("4. Element-wise Multiplication")
    print("5. Transpose")
    print("6. Determinant")
    choice = input("Select operation (1-6): ").strip()

    if choice in ["1", "2", "3", "4"]:
        matrix1 = get_matrix("Enter first matrix:")
        matrix2 = get_matrix("Enter second matrix:")
        if choice == "1":
            if matrix1.shape != matrix2.shape:
                print("Addition requires matrices of the same shape.")
                return
            result = matrix1 + matrix2
            print_matrix(result, "Sum")
        elif choice == "2":
            if matrix1.shape != matrix2.shape:
                print("Subtraction requires matrices of the same shape.")
                return
            result = matrix1 - matrix2
            print_matrix(result, "Difference")
        elif choice == "3":
            if matrix1.shape[1] != matrix2.shape[0]:
                print("Dot product requires the number of columns in the first matrix to equal the number of rows in the second.")
                return
            result = np.dot(matrix1, matrix2)
            print_matrix(result, "Dot Product")
        elif choice == "4":
            if matrix1.shape != matrix2.shape:
                print("Element-wise multiplication requires matrices of the same shape.")
                return
            result = matrix1 * matrix2
            print_matrix(result, "Element-wise Product")
    elif choice == "5":
        matrix = get_matrix("Enter matrix to transpose:")
        result = matrix.T
        print_matrix(result, "Transpose")
    elif choice == "6":
        matrix = get_matrix("Enter square matrix for determinant:")
        if matrix.shape[0] != matrix.shape[1]:
            print("Determinant requires a square matrix.")
            return
        det = np.linalg.det(matrix)
        print(f"\nDeterminant: {det:.2f}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()