# Pandas - Selecting Single and Multiple Rows/Columns

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "name": ["Aman", "Riya", "Rahul", "Priya"],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "sales": [10000, 15000, 8000, 20000]
})

# 1. Selecting a Single Column

print(df["name"])

# Output:
# 0     Aman
# 1     Riya
# 2    Rahul
# 3    Priya

# 2. Selecting Multiple Columns

print(df[["name", "sales"]])

# 3. Selecting a Single Row using loc

print(df.loc[0])

# 4. Selecting Multiple Rows using loc

print(df.loc[[0, 2]])

# 5. Selecting Rows by Position using iloc

print(df.iloc[0])

# 6. Selecting Multiple Rows using iloc

print(df.iloc[[0, 2]])

# 7. Selecting Specific Rows and Columns using loc

print(df.loc[0:2, ["name", "sales"]])

# 8. Selecting Specific Rows and Columns using iloc

print(df.iloc[0:3, [0, 2]])
