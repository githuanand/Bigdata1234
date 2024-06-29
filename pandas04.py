import pandas as pd
data={'A':10,'B':20,'C':30}
Series=pd.Series(data)
new_index_label=input("enter a new label:")
Series.index=[new_index_label if idx == Series.index[0] else idx for idx in Series.index]
print("series: ")
print(Series)
print()
print("keys:")
print(Series.index)
print()
print("values:")
print(Series.values)
