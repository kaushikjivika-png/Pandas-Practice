import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "city": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"],
    "sales": [1500, 3000, 5000, 2000, 4000]
})

# AND condition
print(df[(df["city"] == "Delhi") & (df["sales"] > 2000)])

# OR condition
print(df[(df["city"] == "Delhi") | (df["city"] == "Mumbai")])

# Multiple conditions using AND
print(df[(df["sales"] > 2000) & (df["sales"] < 5000)])
