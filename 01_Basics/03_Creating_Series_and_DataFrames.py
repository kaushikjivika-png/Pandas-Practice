# Creating Series and DataFrame

import pandas as pd

# Creating a Series from a list

marks = pd.Series([85, 90, 78, 92])

print("Series:")
print(marks)


# We can also provide our own index labels.

marks = pd.Series(
    [85, 90, 78, 92],
    index=["Maths", "Science", "English", "Computer"]
)

print("\nSeries with custom index:")
print(marks)

# Creating a DataFrame using a dictionary

data = {
    "Name": ["Jivika", "Rahul", "Priya"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# We can access individual columns from a DataFrame.

print("\nNames:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])
