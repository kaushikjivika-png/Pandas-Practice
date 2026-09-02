import pandas as pd

# Read Excel file
df = pd.read_excel("sales_data.xlsx")

# Display first 5 rows
print(df.head())

# Display basic information
print(df.info())

# Display column names
print(df.columns)

# Display number of rows and columns
print(df.shape)

# Column names
print(df.columns)

# Data types
print(df.dtypes)

# Statistical summary
print(df.describe())
