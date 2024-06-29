import numpy as np

rows=int(input("enter the number of rows: "))
cols=int(input("enter the number of columns: "))

arr=np.empty((rows,cols))
print("enter the elements of array: ")
for i in range(rows):
    for j in range(cols):
        arr[i][j]=float(input(f"element at position({i+1},{j+1}): "))

sorted_along_first_axis=np.sort(arr,axis=0)
sorted_along_last_axis=np.sort(arr,axis=1)
sorted_flattened_array=np.sort(arr.flatten())

print("sorted along first axis: ")
print(sorted_along_first_axis)

print("sorted along last axis: ")
print(sorted_along_last_axis)

print("sorted flattened array: ")
print(sorted_flattened_array)





