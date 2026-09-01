import pandas as pd

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print(df.info())

# Display number of rows and columns
print(df.shape)
