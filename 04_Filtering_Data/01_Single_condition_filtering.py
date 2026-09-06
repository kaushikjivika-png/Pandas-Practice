# Single Condition Filtering in Pandas

import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Filter rows where sales are greater than 5000
filtered_data = df[df["sales"] > 5000]

print(filtered_data)
