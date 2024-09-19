import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess the dataset
data = pd.read_csv(r"C:\Users\pavni\Downloads\index (1).csv")

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

### 1. Time Series Analysis ###

# Aggregate daily sales
daily_sales = data.groupby('date')['money'].sum()

# Aggregate weekly sales
weekly_sales = data.resample('W-Mon', on='date')['money'].sum()

# Aggregate monthly sales
monthly_sales = data.resample('M', on='date')['money'].sum()

# Plot daily sales
plt.figure(figsize=(10, 5))
plt.plot(daily_sales, label='Daily Sales', color='blue')
plt.title('Daily Coffee Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.show()

# Plot weekly sales
plt.figure(figsize=(10, 5))
plt.plot(weekly_sales, label='Weekly Sales', color='green')
plt.title('Weekly Coffee Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.show()

# Plot monthly sales
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales, label='Monthly Sales', color='red')
plt.title('Monthly Coffee Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.show()

### 2. Customer Purchase Patterns ###

# Group by 'card' (customer ID) to find total and average money spent per customer
customer_spending = data.groupby('card')['money'].agg(['sum', 'mean', 'count']).reset_index()
customer_spending.columns = ['Customer ID', 'Total Spend', 'Average Spend', 'Purchase Count']

# Top 10 customers based on total spend
top_customers = customer_spending.sort_values(by='Total Spend', ascending=False).head(10)

# Display top 10 customers
print("Top 10 Customers by Total Spend:")
print(top_customers)

# Analyze coffee preferences by customer
coffee_preferences = data.groupby(['card', 'coffee_name']).size().unstack(fill_value=0)

# Top 10 customers coffee preferences
top_customers_prefs = coffee_preferences.loc[top_customers['Customer ID']]
print("\nCoffee Preferences of Top 10 Customers:")
print(top_customers_prefs)

# Visualize coffee preferences for the top customers
top_customers_prefs.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Top 10 Customers Coffee Preferences')
plt.ylabel('Number of Purchases')
plt.xlabel('Customer ID')
plt.xticks(rotation=45)
plt.legend(title='Coffee Type')
plt.show()
