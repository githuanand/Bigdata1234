import numpy as np

identity_matrix = np.identity(4)
print("Identity Matrix:")
print(identity_matrix)


array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [2, 5,7 ,8]])

array2 = np.array([[10, 11, 12, 8],
                   [2, 4, 6, 9],
                   [5, 12, 7, 2],
                   [9, 10, 11, 6]])


sum_arrays = np.add(array1, array2)
print("\nElement-wise Addition of Arrays:")
print(sum_arrays)


transposed_array1 = np.transpose(array1)
print("\nTransposed Matrix:")
print(transposed_array1)

result_matrix = np.dot(transposed_array1, array2)
print("\nResult Matrix (Transpose Matrix multiplied by 2nd Matrix):")
print(result_matrix)
