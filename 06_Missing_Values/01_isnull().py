import pandas as pd

df = pd.DataFrame({
    "name": ["Aman", "Riya", "Karan", "Neha"],
    "age": [21, None, 23, None],
    "city": ["Delhi", "Mumbai", None, "Pune"]
})

# Check missing values
print(df.isnull())
