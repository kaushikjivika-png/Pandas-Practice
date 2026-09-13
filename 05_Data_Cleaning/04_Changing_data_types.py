import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Aman', 'Riya', 'Rahul'],
    'Age': ['21', '22', '20'],
    'Salary': ['25000', '30000', '28000']
}

df = pd.DataFrame(data)

print("Before changing data types:")
print(df.dtypes)

# Changing data types
df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(float)

print("\nAfter changing data types:")
print(df.dtypes)

print("\nUpdated DataFrame:")
print(df)
