import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Check inconsistent values
print(df.head())
print(df.info())

# Remove extra spaces
df["column_name"] = df["column_name"].str.strip()

# Make text consistent
df["column_name"] = df["column_name"].str.lower()

# Check unique values
print(df["column_name"].unique())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
