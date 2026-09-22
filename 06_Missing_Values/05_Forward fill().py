import pandas as pd

# Create sample DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "Marks": [85, None, 78, None, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Forward fill missing values
df["Marks"] = df["Marks"].ffill()

print("\nDataFrame after Forward Fill:")
print(df)
