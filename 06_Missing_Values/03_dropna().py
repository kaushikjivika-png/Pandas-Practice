import pandas as pd

# Sample dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Karan"],
    "Age": [21, None, 23, 22, None],
    "City": ["Delhi", "Mumbai", None, "Pune", "Delhi"],
    "Salary": [25000, 30000, None, 28000, 35000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 1. Remove rows containing ANY missing value
df_drop_any = df.dropna()

print("\nAfter dropna():")
print(df_drop_any)


# 2. Remove rows where ALL values are missing
df_drop_all = df.dropna(how="all")

print("\nAfter dropna(how='all'):")
print(df_drop_all)


# 3. Remove rows based on specific columns
df_drop_subset = df.dropna(subset=["Salary"])

print("\nAfter dropping rows with missing Salary:")
print(df_drop_subset)


# 4. Drop columns containing missing values
df_drop_columns = df.dropna(axis=1)

print("\nAfter dropping columns with missing values:")
print(df_drop_columns)
