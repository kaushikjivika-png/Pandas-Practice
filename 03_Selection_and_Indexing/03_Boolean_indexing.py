import pandas as pd

# Sample DataFrame
data = {
    "name": ["Aman", "Riya", "Rahul", "Sneha", "Arjun"],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "sales": [12000, 8000, 15000, 6000, 20000]
}

df = pd.DataFrame(data)

print(df)

# Boolean Indexing Examples

# 1. Customers from Delhi
print(df[df["city"] == "Delhi"])

# 2. Sales greater than 10000
print(df[df["sales"] > 10000])

# 3. Multiple conditions
print(df[(df["city"] == "Mumbai") & (df["sales"] > 10000)])
