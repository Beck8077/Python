import matplotlib.pyplot  as plt
import numpy as np
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
df1['Averade Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)
# print(df1['Averade Grade'])

# Exercise 2: Find the student with the highest average grade.
max_avg_grade = df1.iloc[df1['Averade Grade'].idxmax()]
# print(max_avg_grade)

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
# print(df1[['Student_ID', 'Total']])

# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
bar_chart = df1.plot.bar(x='Student_ID', y='Averade Grade', rot=0)
# print(bar_chart)


# Homework 2

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
df2['Total Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
# print(df2)

# Exercise 2: Find the date with the highest total sales.
max_sales = df2.iloc[df2['Total Sales'].idxmax()]
# print(max_sales)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
perc_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
# print(perc_change)

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.



# Homework 3


data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)



# Exercise 1: Calculate the average salary for each department.
grouped_dept = df3.groupby('Department')
avg_sal = grouped_dept.agg({'Salary': 'mean'})
# print(avg_sal)

# Exercise 2: Find the employee with the most experience.
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
# print(most_experienced)

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_sal = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_sal) / min_sal * 100).round(2)
# print(df3)

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
bar_chart3 = df3.plot.bar(x='Department', y='Salary', rot=0)
# print(bar_chart3)


# Homework 4

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)


# Exercise 1: Calculate the total revenue from all orders.
df4['Total_Revenue'] = df4['Quantity'] * df4['Total_Price']
# print(df4)

# Exercise 2: Find the most ordered product.
sum_order = df4.groupby('Product')['Quantity'].sum()
most_order_quantity = sum_order.max()
most_order_product = sum_order.idxmax()
# print(most_order_product, most_order_quantity)

# Exercise 3: Calculate the average quantity of products ordered.
avg_order = df4.groupby('Product')['Quantity'].mean()
# print(avg_order)

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
