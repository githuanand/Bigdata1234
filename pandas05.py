import pandas as pd

data=pd.read_csv("samplecsv.csv")

print("All data:")
print(data)

print("\nFirst 3 rows:")
print(data.head(3))

print("\nLast 3 rows of the first column:")
print(data.iloc[-3:, [0, -2, -1]])
