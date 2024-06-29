import numpy as np


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


matrix = []
print(f"Enter {rows}x{columns} matrix elements:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
matrix = np.array(matrix)

print("\nInitial Matrix:")
print(matrix)


print(f"Enter {rows} elements for the new column:")
new_column = np.array(list(map(int, input().split())))


if len(new_column) == rows:
    matrix_with_new_column = np.column_stack([matrix, new_column])
    print("\nMatrix after adding new column:")
    print(matrix_with_new_column)
else:
    print("Error: Number of elements in the new column must match the number of rows in the matrix.")
