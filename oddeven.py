my_list=[25,43,2,42,8,4,3]
list_odd =[]
list_even =[]

for num in my_list:
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)

print("my_list:",my_list)
print("list_even:",list_even)
print("list_odd:",list_odd)
