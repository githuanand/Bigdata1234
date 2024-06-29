import numpy as np

def input_matrix(n, m):
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    
    matrix = input_matrix(n, m)
    arr = np.array(matrix)
    
    print("Original Array:")
    print(arr)
    
    print("\nMaximum Element:", np.max(arr))
    print("Minimum Element:", np.min(arr))
    
    sorted_arr = np.sort(arr.flatten())
    print("\nSorted Array:")
    print(sorted_arr)
    
    sorted_row_wise = np.sort(arr, axis=1)
    print("\nSorted Row-wise:")
    print(sorted_row_wise)
    
    sorted_col_wise = np.sort(arr, axis=0)
    print("\nSorted Column-wise:")
    print(sorted_col_wise)

if __name__ == "__main__":
    main()
