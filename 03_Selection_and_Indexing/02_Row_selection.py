import pandas as pd

# Sample DataFrame
data = {
    "name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "age": [22, 25, 21, 24, 23],
    "salary": [25000, 35000, 28000, 40000, 30000]
}

df = pd.DataFrame(data)

# 1. Select a row by index
print(df.loc[0])

# 2. Select multiple rows
print(df.loc[0:2])

# 3. Select rows using condition
print(df[df["city"] == "Delhi"])

# 4. Select rows where salary is greater than 30000
print(df[df["salary"] > 30000])

# 5. Select rows using multiple conditions
print(df[(df["city"] == "Mumbai") & (df["salary"] > 30000)])

# 6. Select specific rows and columns
print(df.loc[df["city"] == "Delhi", ["name", "salary"]])

# 7. Select rows by position using iloc
print(df.iloc[0])

# 8. Select first 3 rows
print(df.iloc[0:3])
