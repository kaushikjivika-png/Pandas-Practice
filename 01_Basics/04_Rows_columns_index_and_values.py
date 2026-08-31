# Rows, Columns & Index

In Pandas, rows, columns, and index are used to access and work with specific parts of a DataFrame.

## 1. Selecting Columns

A single column can be selected using its column name.

### Example
df["Name"]

1. To select multiple columns:

df[["Name", "Age"]]

2. Selecting Rows

# Rows can be selected using loc or iloc.

1. Using loc

# loc selects rows and columns using labels.

df.loc[0]

2. Using iloc

# iloc is used for position-based selection.

Select a single row
df.iloc[0]

