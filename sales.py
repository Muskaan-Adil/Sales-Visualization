# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Sales_Dataset.csv", encoding='ISO-8859-1')

# --- Data Cleaning and EDA Steps ---

# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Check for missing values across all columns
missing_data = df.isnull().sum()
print("Missing Values:\n", missing_data)

# Drop rows where ORDERDATE is missing
df = df.dropna(subset=['ORDERDATE'])

# Check for missing values after dropping ORDERDATE rows
missing_data = df.isnull().sum()
print("\nMissing Values After Cleaning ORDERDATE:\n", missing_data)

# Handle missing values for other columns
# Example: Fill missing sales values with median
df['SALES'] = df['SALES'].fillna(df['SALES'].median())

# --- EDA ---

# Show summary statistics for numeric columns
print("\nSummary Statistics:\n", df.describe())

# Check data types to ensure they're correct
print("\nData Types:\n", df.dtypes)

# --- Seaborn and Matplotlib Visualizations ---

# 1. Sales Over Time (Line Plot with Seaborn)
sales_by_date = df.groupby('ORDERDATE')['SALES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='ORDERDATE', y='SALES', data=sales_by_date, color='blue', marker='o')
plt.title('Sales Over Time', fontsize=16)
plt.xlabel('Order Date', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sales by Product Line (Bar Plot with Seaborn)
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index().sort_values(by='SALES', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='SALES', y='PRODUCTLINE', data=product_sales, palette='Blues_d')
plt.title('Sales by Product Line', fontsize=16)
plt.xlabel('Total Sales', fontsize=12)
plt.ylabel('Product Line', fontsize=12)
plt.tight_layout()
plt.show()

# 3. Monthly Sales Trend (Line Plot with Seaborn)
monthly_sales = df.groupby(['YEAR_ID', 'MONTH_ID'])['SALES'].sum().reset_index()
monthly_sales['YearMonth'] = pd.to_datetime(monthly_sales['YEAR_ID'].astype(str) + '-' + monthly_sales['MONTH_ID'].astype(str))
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='YearMonth', y='SALES', color='orange', marker='o')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.tight_layout()
plt.show()

# 4. Sales Distribution (Histogram with Seaborn)
plt.figure(figsize=(10, 6))
sns.histplot(df['SALES'], bins=30, kde=True, color='green')
plt.title('Sales Distribution', fontsize=16)
plt.xlabel('Sales', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# 5. Correlation Heatmap (Seaborn)
numeric_cols = ['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP']
correlation_matrix = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16)
plt.tight_layout()
plt.show()

# 6. Bubble Chart (Scatter Plot with Seaborn)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PRICEEACH', y='QUANTITYORDERED', size='SALES', data=df, hue='PRODUCTLINE', sizes=(20, 200), palette='Set2', legend=False)
plt.title('Bubble Chart: Price vs Quantity Ordered', fontsize=16)
plt.xlabel('Price Each', fontsize=12)
plt.ylabel('Quantity Ordered', fontsize=12)
plt.tight_layout()
plt.show()

# 7. Outlier Detection (Boxplot for SALES)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['SALES'])
plt.title('Outliers in Sales', fontsize=16)
plt.tight_layout()
plt.show()

# 8. Outlier Detection (Boxplot for QUANTITYORDERED)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['QUANTITYORDERED'])
plt.title('Outliers in Quantity Ordered', fontsize=16)
plt.tight_layout()
plt.show()

# 9. Outlier Detection (Boxplot for PRICEEACH)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['PRICEEACH'])
plt.title('Outliers in Price Each', fontsize=16)
plt.tight_layout()
plt.show()