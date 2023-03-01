import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finance_liquor_sales (1).csv")

# Task 1: Filter data between 2016 and 2019
df = df[(df['date'] >= '2016-01-01') & (df['date'] < '2020-01-01')]

# Task 2: Get the most popular item sold based on zip code
# Group data by zip_code and item_description and sum the bottles_sold
grouped = df.groupby(['zip_code', 'item_description'])['bottles_sold']
grouped = grouped.aggregate(np.sum)

# Find the item with the maximum total bottles sold
most_popular_item = grouped.groupby('zip_code').idxmax()
print(f"The most popular item by zip code: {most_popular_item}")
print()

# Task 3: Find the percentage of sales per store
# Group data by store_name and sum the sale_dollars
sales_by_store = df.groupby('store_name')['sale_dollars']
sales_by_store = sales_by_store.aggregate(np.sum)

# Calculate the total sales for all stores
total_sales = sales_by_store.sum()

# Calculate the percentage of sales for each store
sales_percentages = (sales_by_store / total_sales) * 100
print(f"The percentage of sales per each store: {sales_percentages}")


# Task 4: Using Matplotlib visualize a scatter plot with x-axis zip_code and y-axis bottles_sold
# Get data for the scatter plot
scatter_data = df.groupby('zip_code')['bottles_sold'].sum()

# Create scatter plot
plt.scatter(scatter_data.index, scatter_data.values)

plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')

plt.show()