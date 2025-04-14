# Sales Dataset – Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing a retail sales dataset containing customer orders, sales values, product lines, and geographical data. The main goal is to prepare this dataset for effective analysis by addressing missing values, handling duplicates, cleaning inconsistent entries, and formatting dates.

This project demonstrates the essential steps involved in preparing real-world business data for insights, reporting, or advanced analysis like forecasting and segmentation.

---

## Key Features

- **Data Inspection**: Reviewed the dataset structure, checked column data types, and identified missing or inconsistent entries.
- **Missing Value Handling**: Located and handled missing values appropriately by either removing irrelevant rows or keeping essential ones.
- **Duplicate Handling**: Identified and removed duplicate rows that could bias future analysis.
- **Data Consistency Checks**: Cleaned inconsistencies in categorical/text fields such as `City`, `Country`, and `State`.
- **Date Formatting**: Converted order dates to standard datetime format for accurate time-series analysis.
- **Trend Visualizations**: Visualized monthly and product-wise sales trends using bar plots, line charts, and heatmaps.
- **Customer Insights**: Identified top customers and regions contributing to revenue.

---

## Dataset Information

- **Source**: A classic retail dataset simulating customer orders and product sales globally.
- **Columns**:
  - `ORDERNUMBER`: Unique ID for each order.
  - `QUANTITYORDERED`: Units of product ordered.
  - `PRICEEACH`: Price per unit.
  - `ORDERLINENUMBER`: Line item number within an order.
  - `SALES`: Total sale value of each line item.
  - `ORDERDATE`: Date the order was placed.
  - `STATUS`: Status of the order (e.g., Shipped, Cancelled).
  - `QTR_ID`, `MONTH_ID`, `YEAR_ID`: Time-based identifiers.
  - `PRODUCTLINE`: Category of the product.
  - `MSRP`: Manufacturer’s suggested retail price.
  - `PRODUCTCODE`: Unique product ID.
  - `CUSTOMERNAME`, `PHONE`, `ADDRESSLINE1/2`, `CITY`, `STATE`, `POSTALCODE`, `COUNTRY`, `TERRITORY`: Customer and address info.
  - `CONTACTLASTNAME`, `CONTACTFIRSTNAME`: Contact details of the customer.
  - `DEALSIZE`: Size category of the customer deal (e.g., Small, Medium, Large).

---

## Data Cleaning and Preprocessing Steps

### Loading the Dataset
- Loaded the dataset using pandas and confirmed the data was correctly loaded with `head()` and `tail()`.

### Inspecting the Data
- Used `df.info()` to check data types and find null values.
- Used `df.describe()` to get statistical insights on numerical columns like `SALES`, `QUANTITYORDERED`, and `PRICEEACH`.

### Handling Missing Values
- Used `df.isnull().sum()` to detect missing values.
- Removed rows with critical null values in columns such as `ORDERNUMBER` or `SALES`.
- Retained rows with missing secondary fields like `ADDRESSLINE2`.

### Removing Duplicates
- Checked for and removed duplicate records using `df.duplicated()` and `df.drop_duplicates()`.

### Ensuring Data Consistency
- Cleaned text fields using `.str.strip()` and `.str.title()`.
- Standardized values across city, country, and status fields.

### Date Formatting
- Converted `ORDERDATE` to datetime format using `pd.to_datetime()` to allow for time-series analysis.

### Data Transformation
- Grouped data to calculate total sales per month, quarter, and year.
- Computed total sales per `PRODUCTLINE` and by `COUNTRY`.
- Identified top 10 customers by total revenue.

### Data Visualizations
- Created:
  - Line plots of monthly sales trends.
  - Bar plots for top-performing product lines.
  - Heatmaps for correlation between features like `SALES`, `MSRP`, and `QUANTITYORDERED`.

---

## Report

For a more detailed analysis of the dataset and the steps taken during data cleaning and preprocessing, please refer to **[Sales_Report.md](Sales_Report.md)**.
