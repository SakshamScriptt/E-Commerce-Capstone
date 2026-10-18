import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start='2026-01-01', periods=500, freq='D')

data = {
    'OrderID': np.arange(1001, 1501),
    'OrderDate': dates,
    'Category': np.random.choice(['Electronics', 'Fashion', 'Home & Kitchen', 'Beauty', 'Sports'], 500),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 500),
    'PaymentMethod': np.random.choice(['Credit Card', 'UPI', 'Net Banking', 'Cash on Delivery'], 500),
    'Price': np.random.randint(500, 15000, 500),
    'Quantity': np.random.randint(1, 6, 500),
    'CustomerAge': np.random.randint(18, 65, 500)
}

df = pd.DataFrame(data)
df['Revenue'] = df['Price'] * df['Quantity']

# Introduce Missing Values & Duplicates for Data Cleaning Task
df.loc[10:20, 'CustomerAge'] = np.nan
df.loc[40:45, 'PaymentMethod'] = np.nan
df = pd.concat([df, df.iloc[0:5]], ignore_index=True) # Adding 5 duplicates
df.loc[100, 'Revenue'] = 500000 # Adding an outlier

df.to_csv('retail_sales_data.csv', index=False)
print("Success: 'retail_sales_data.csv' created!")