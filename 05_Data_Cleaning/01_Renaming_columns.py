import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Jivika", "Rahul", "Priya"],
    "Age": [20, 22, 21],
    "City": ["Delhi", "Mumbai", "Pune"]
})

# Original DataFrame
print("Original DataFrame:")
print(df)


# Rename a single column
df.rename(columns={"Name": "Customer_Name"}, inplace=True)

print("\nAfter renaming Name column:")
print(df)


# Rename multiple columns
df.rename(columns={
    "Age": "Customer_Age",
    "City": "Customer_City"
}, inplace=True)

print("\nAfter renaming multiple columns:")
print(df)
