import matplotlib.pyplot as plt 
import pandas as pd


data = pd.read_csv('C:\\Users\\ANAND\\OneDrive\\Desktop\\data analytics and big data lab\\DAY 04\\people1.csv')

plt.figure()

df = pd.DataFrame(data) 
  
X = list(df.iloc[:, 0]) 
Y = list(df.iloc[:, 1]) 
  
# Plot the data using bar() method 
plt.bar(X, Y, color='g') 
plt.title("Marks of Students") 
plt.xlabel("Name") 
plt.ylabel("Subjects") 
  
# Show the plot 
plt.show() 
