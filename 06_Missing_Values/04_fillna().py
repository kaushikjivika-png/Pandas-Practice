import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Age": [21, None, 23, None],
    "City": ["Delhi", "Mumbai", None, "Meerut"],
    "Salary": [30000, 40000, None, 50000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values with a fixed value
df["Age"] = df["Age"].fillna(0)

# Fill missing values in City with "Unknown"
df["City"] = df["City"].fillna("Unknown")

# Fill missing Salary with the mean salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nDataFrame after filling missing values:")
print(df)
