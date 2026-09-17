import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Age": [21, None, 23, 22],
    "City": ["Delhi", "Noida", None, "Meerut"]
}

df = pd.DataFrame(data)

print(df)

# Check which values are NOT null
print(df.notnull())

# Check a specific column
print(df["Age"].notnull())

# Count non-null values in each column
print(df.notnull().sum())
