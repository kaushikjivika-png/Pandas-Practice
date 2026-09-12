import pandas as pd

data = {
    "order_id": [101, 102, 103, 102, 104],
    "customer": ["Aman", "Riya", "Rahul", "Riya", "Neha"],
    "sales": [500, 700, 600, 700, 900]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nAfter Removing Duplicates:")
df = df.drop_duplicates()
print(df)
