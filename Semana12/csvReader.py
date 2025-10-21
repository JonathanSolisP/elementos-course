import pandas as pd

# Read CSV file
df = pd.read_csv('Semana12/products-100000.csv')

# Display the first few rows of the data
print(df.head())

# Display basic statistics about the data
print(df.describe())

# Filter products with price greater than 100
expensive_products = df[df['Price'] > 100]

for product in df['Name'].head(10):
    print(product)
print(f"Number of products with price greater than 100: {len(expensive_products)}")
