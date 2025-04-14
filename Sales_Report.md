# Detailed Report – Sales Data Cleaning & Preprocessing

---

## 1. **Basic Data Inspection**

To start, I loaded the **Sales Dataset** into a Pandas DataFrame and explored its structure. I printed out the **first and last five rows** to ensure the dataset loaded correctly. Then, I used the `columns` attribute to list all available features:
- `ORDERNUMBER`, `QUANTITYORDERED`, `PRICEEACH`, `ORDERLINENUMBER`, `SALES`, `ORDERDATE`, `STATUS`, `QTR_ID`, `MONTH_ID`, `YEAR_ID`, `PRODUCTLINE`, `MSRP`, `PRODUCTCODE`, `CUSTOMERNAME`, `PHONE`, `ADDRESSLINE1`, `ADDRESSLINE2`, `CITY`, `STATE`, `POSTALCODE`, `COUNTRY`, `TERRITORY`, `CONTACTLASTNAME`, `CONTACTFIRSTNAME`, `DEALSIZE`.

By using `info()`, I examined the data types and checked for any **missing values**. The `describe()` method gave an overview of the **numerical features**, allowing me to see the spread and scale of sales data across different orders.

---

## 2. **Missing Values**

Next, I checked for missing values using `isnull().sum()` and found some **null values in several columns** like `ADDRESSLINE2` and `PHONE`. Since these fields weren't essential for the analysis, I decided to drop rows where the missing values were found in key columns like `SALES` and `ORDERNUMBER`.

To visualize the missing data patterns, I used a **missingno matrix plot**, which offered a clear snapshot of where the missing values were located in the dataset.

---

## 3. **Date Formatting and Cleaning**

The `ORDERDATE` column was originally in string format. I converted it into **datetime format** using `pd.to_datetime()` to allow for time-series operations such as grouping by month or year, and trend analysis over time. This made it easier to analyze the **sales trends** across different periods.

---

## 4. **Removing Duplicates**

I checked for duplicate entries using `duplicated()` and found a few repeated rows in the dataset. To ensure the analysis wasn’t skewed by these duplicates, I used `drop_duplicates()` to remove them from the dataset.

---

## 5. **Inconsistencies & String Cleaning**

I noticed some inconsistencies in the text fields, such as `CITY`, `STATE`, and `COUNTRY`, where extra spaces and inconsistent capitalization appeared. I applied `.str.strip()` and `.str.title()` to ensure **uniform formatting** across these columns. This helped maintain consistency when filtering or grouping data.

---

## 6. **Preprocessing for Analysis**

To prepare the dataset for deeper analysis:
- I calculated total **SALES** by **PRODUCTLINE** to identify which product categories performed best.
- I computed **monthly and quarterly sales totals** to track the sales trends over time.
- I identified the **top 10 customers** based on total sales, which could help in targeted marketing or customer engagement strategies.

---

## 7. **Visualizations**

Using **Seaborn** and **Matplotlib**, I created several visualizations to support the analysis:
- **Line plot** of **sales trends over time**, which shows how sales have evolved across different months.
- **Bar plot** for **top-performing products** based on total sales, helping to identify which product lines contribute most to the revenue.
- **Heatmap** for the **correlation matrix** between different numerical features to understand relationships in the dataset.

These visuals provided valuable insights and confirmed that the cleaning steps were successful.

---

## Final Thoughts

This project emphasized the importance of **data cleaning and preprocessing** before conducting any detailed analysis. Handling issues like **missing values**, **duplicate entries**, and **format inconsistencies** ensured the dataset was ready for meaningful analysis.

The cleaned dataset can now be used for:
- **Sales trend analysis** by month, quarter, or year
- **Product performance analysis** to focus on high-performing product lines
- **Customer analysis** for segmentation and targeted marketing strategies

Moving forward, the data could be leveraged for:
- **Predicting future sales trends** using time-series forecasting
- **Building dashboards** to monitor real-time sales performance across regions and product lines.