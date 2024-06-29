import pandas as pd


user_dict = {}
num_elements = int(input("Enter the number of elements in the dictionary: "))

for i in range(num_elements):
    key = input("Enter key {}: ".format(i+1))
    value = input("Enter value for key {}: ".format(key))
    user_dict[key] = value

for key, value in user_dict.items():
    try:
        user_dict[key] = int(value)
    except ValueError:
        try:
            user_dict[key] = float(value)
        except ValueError:
            pass


series = pd.Series(user_dict)


print("\nPandas Series:")
print(series)
