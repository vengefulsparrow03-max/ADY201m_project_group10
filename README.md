# 📊 ADY201M Project - Online Retail Data Analysis

## 🎯 Project Overview

This project analyzes the Online Retail dataset using Python, statistical analysis, data visualization, and regression techniques to understand customer purchasing behavior, product performance, and price elasticity.

The project follows a complete data analytics workflow:

* Data Understanding
* Data Cleaning & Pre-processing
* Feature Engineering
* Data Visualization
* Exploratory Data Analysis (EDA)
* Regression Analysis
* Revenue Simulation

---

## 📁 Project Structure

```text
ADY201m_project/
│
├── Data_Understanding_and_Pre_processing.py
├── Data_visualization.py
├── Data_AnalysisWithPython.py
├── Regression_Analysis.py
├── Online Retail.xlsx
├── README.md
└── .gitignore
```

---

## 📦 Dataset

Dataset Used:

```text
Online Retail.xlsx
```

The dataset contains transactional records from an online retail store, including:

* Invoice Number
* Product Description
* Quantity Purchased
* Unit Price
* Customer ID
* Invoice Date
* Country

The dataset is used to analyze purchasing patterns, sales performance, and pricing effects on demand.

---

## 🧹 Data Understanding & Pre-processing

### Main Tasks

* Load and inspect dataset
* Check dataset information
* Explore statistical summaries
* Identify missing values
* Remove invalid records
* Convert date-time variables
* Feature engineering
* Log transformation
* Seasonal feature extraction
* One-Hot Encoding
* Lag feature creation
* Outlier detection

### Features Created

| Feature     | Description               |
| ----------- | ------------------------- |
| TotalPrice  | Quantity × UnitPrice      |
| LogQuantity | Log-transformed Quantity  |
| LogPrice    | Log-transformed UnitPrice |
| Month       | Transaction Month         |
| DayOfWeek   | Day Name                  |
| Hour        | Transaction Hour          |
| Lag_1_Day   | Previous Day Sales        |

### Data Cleaning Steps

* Removed missing values
* Removed negative quantities
* Removed zero or negative prices
* Converted InvoiceDate to datetime format

---

## 📊 Data Visualization

The project includes multiple visualization techniques to better understand customer behavior and sales performance.

### 1. Scatter Plot

Visualization of:

* LogPrice
* LogQuantity

Purpose:

* Explore relationship between price and demand
* Identify demand elasticity patterns

---

### 2. Monthly Revenue Trend

Line chart showing:

* Monthly sales revenue

Purpose:

* Detect seasonality
* Observe revenue fluctuations over time

---

### 3. Price Trend vs Sales

Comparison between:

* Average Product Price
* Total Quantity Sold

Purpose:

* Analyze relationship between pricing and sales volume

---

### 4. Top 10 Revenue Products

Bar chart displaying:

* Highest revenue-generating products

Purpose:

* Identify best-performing products
* Understand revenue concentration

---

### 5. Quantity Outlier Detection

Boxplot visualization of:

* Quantity

Purpose:

* Detect extreme purchase quantities
* Identify unusual transactions

---

### 6. Correlation Heatmap

Heatmap displaying correlations among:

* Quantity
* UnitPrice
* TotalPrice
* LogQuantity
* LogPrice

Purpose:

* Discover relationships between key variables

---

### 7. Product Elasticity Heatmap

Heatmap comparing:

* Average LogPrice
* Average LogQuantity

For top-selling products.

Purpose:

* Evaluate product-level price sensitivity

---

## 📈 Data Analysis

### Revenue Analysis

Performed analysis on:

* Top 10 Revenue Products
* Top 10 Best-Selling Products
* Monthly Revenue Performance

Insights generated include:

* Most profitable products
* Highest demand products
* Seasonal sales trends

---

### Price Elasticity Analysis

Model Used:

```text
LogQuantity ~ LogPrice
```

Purpose:

* Estimate demand sensitivity to price changes

Output:

* Elasticity coefficient
* OLS regression summary

---

### Fixed Effects Model

Model Used:

```text
LogQuantity ~ LogPrice + C(Description)
```

Purpose:

* Control for product-specific characteristics
* Improve elasticity estimation accuracy

Output:

* Fixed Effects Elasticity
* Product-specific effects

---

## 📉 Regression Analysis

### Model 1: Simple Linear Regression

Target Variable:

```text
LogQuantity
```

Independent Variable:

```text
LogPrice
```

Evaluation Metrics:

* R² Score
* MAE
* RMSE

Purpose:

* Measure direct effect of price on quantity demanded

---

### Model 2: Multiple Linear Regression

Target Variable:

```text
LogQuantity
```

Independent Variables:

```text
LogPrice
Month
Hour
```

Evaluation Metrics:

* R² Score
* MAE
* RMSE

Purpose:

* Measure combined influence of price and seasonality factors on demand

---

## 💰 Revenue Simulation

A pricing simulation is performed by increasing product prices by 10%.

### Simulation Process

1. Increase UnitPrice by 10%
2. Predict new demand using elasticity
3. Calculate new revenue
4. Compare old and new revenue

### Outputs

* Predicted Quantity
* New Revenue
* Revenue Difference
* Revenue Growth Percentage

Purpose:

* Support pricing strategy decisions
* Evaluate potential revenue impact

---

## 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statsmodels
* Scikit-Learn

### Techniques

* Data Cleaning
* Feature Engineering
* One-Hot Encoding
* Log Transformation
* Exploratory Data Analysis
* Data Visualization
* OLS Regression
* Linear Regression
* Revenue Simulation

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn openpyxl
```

### Run Data Pre-processing

```bash
python Data_Understanding_and_Pre_processing.py
```

### Run Data Visualization

```bash
python Data_visualization.py
```

### Run Data Analysis

```bash
python Data_AnalysisWithPython.py
```

### Run Regression Analysis

```bash
python Regression_Analysis.py
```

---

## 📊 Expected Outputs

The project generates:

* Cleaned Dataset
* Statistical Summaries
* Revenue Analysis Reports
* Data Visualizations
* Elasticity Estimates
* Regression Performance Metrics
* Revenue Simulation Results

---

## 👨‍🎓 Course Information

**Course:** ADY201M

**Project Title:** Online Retail Data Analysis

**Project Type:** Data Analytics & Business Intelligence

**Tools:** Python, Statistics, Data Visualization, Machine Learning

---

## 📌 Project Objective

The main objective of this project is to analyze online retail transactions, understand customer purchasing behavior, estimate price elasticity, and provide data-driven insights that support business decision-making and pricing strategies.
