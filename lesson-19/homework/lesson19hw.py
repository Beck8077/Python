import pandas as pd
import numpy as np
import pyodbc
import sqlite3

sales_data = pd.read_csv('lesson19/hw/sales_data.csv')
df = pd.DataFrame(sales_data)
# Group the data by the Category column and calculate the following aggregate statistics for each category:
quantity_group = sales_data.groupby('Category')

# Total quantity sold.
# total_quantity_sold = quantity_group['Quantity'].agg('sum')
# print(total_quantity_sold)

# Average price per unit.
# avg_price_per_unit = quantity_group['Price'].agg('mean')
# print(avg_price_per_unit)

# Maximum quantity sold in a single transaction.
# max_sold = quantity_group.agg({'Quantity':'max'})
# print(max_sold)

# Identify the top-selling product in each category based on the total quantity sold.


# Find the date on which the highest total sales (quantity * price) occurred.
# df['Gross'] = df['Quantity'] * df['Price']
# daily_sales = df.groupby('Date')['Gross'].sum()

# highest_sales_date = daily_sales.idxmax()
# highest_sales_value = daily_sales.max()
# print(highest_sales_date, highest_sales_value)


# Homework 2

customer_orders = pd.read_csv('lesson19/hw/customer_orders.csv')
df_cust_ord = pd.DataFrame(customer_orders)
# print(customer_orders)

# Group the data by CustomerID and filter out customers who have made less than 20 orders.
filt = customer_orders.groupby(['CustomerID'], as_index=False)['Quantity'].sum().loc[lambda x: x['Quantity']<28]
# print(filt)

# Identify customers who have ordered products with an average price per unit greater than $120.
filt2 = customer_orders.groupby(['CustomerID'], as_index=False)['Price'].mean().loc[lambda x: x['Price']>120]
# print(filt2)

# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
filt3 = customer_orders.groupby("Product").agg({"Quantity":"sum", "Price":"sum"}).loc[lambda x: x['Quantity'] < 5]
# print(filt3)


# Homework Assignment 3: Population Salary Analysis

conn = sqlite3.connect('lesson19/hw/population.db')

cursor = conn.cursor()
select_sql = 'select * from population'
data = cursor.execute(select_sql)
# print(data.fetchall())

with open('lesson19/hw/population_salary_analysis.xlsx', 'rb') as f:
    data2 = f.read()
    print(data2)

conn.commit()
cursor.close()
conn.close()



# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.