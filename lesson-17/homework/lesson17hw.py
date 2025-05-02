import pandas as pd
import numpy as np

# Homework 1:

data = {
        'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 

df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df_rename = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})  # -- rename() func renames columns

# Print the first 3 rows of the DataFrame
print(df_rename.head(3))

# Find the mean age of the individuals
df_mean = df_rename.mean(numeric_only=True)
print(df_mean)

# Select and print only the 'Name' and 'City' columns
print(df[['First Name', 'City']])

# Add a new column 'Salary' with random salary values
df['Salary'] = np.random.randint(300, 2000, df.shape[0])
print(df)

# Display summary statistics of the DataFrame
print(df.info())


# Homework 2:

sales_and_expenses = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

df1 = pd.DataFrame(sales_and_expenses)

# Calculate and display the maximum sales and expenses.
print(df1['Sales'].max(), df1['Expenses'].max())

# Calculate and display the minimum sales and expenses.
print(df1['Sales'].min(), df1['Expenses'].min())

# Calculate and display the average sales and expenses.
print(df1['Sales'].mean(), df1['Expenses'].mean())



# Homework 3:

expenses = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 160],
    'April': [1500, 250, 350, 180]
}

df3 = pd.DataFrame(expenses)
df3_indexed = df3.set_index('Category')

# Calculate and display the maximum expense for each category.
max_exp = df3_indexed.max(axis=1)
print(max_exp)

# Calculate and display the minimum expense for each category.
min_exp = df3_indexed.min(axis=1)
print(min_exp)

# Calculate and display the average expense for each category.
mean_exp = df3_indexed.mean(axis=1)
print(mean_exp)