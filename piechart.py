import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("C:\\Users\\ANAND\\OneDrive\\Desktop\\data analytics and big data lab\\DAY 04\\engineering_students.csv")

# Calculate average marks for each subject
average_marks = df[["Maths", "Physics", "Information Security"]].mean()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(average_marks, labels=average_marks.index, autopct="%1.1f%%", startangle=90)
plt.title("Average Marks by Subject")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
