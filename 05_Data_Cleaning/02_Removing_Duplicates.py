# Removing Duplicates in Pandas

import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Jivika", "Rahul", "Jivika", "Priya"],
    "Age": [20, 21, 20, 22]
}

df = pd.DataFrame(data)

# Check duplicate rows
print(df.duplicated())

# Display duplicate rows
print(df[df.duplicated()])

# Remove duplicate rows
df = df.drop_duplicates()

print(df)
