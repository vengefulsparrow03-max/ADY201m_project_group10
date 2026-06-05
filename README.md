# 📈 Price Elasticity Analysis in Omnichannel Retail

## 🎯 Project Overview

This project investigates price elasticity in an omnichannel retail environment using transactional retail data. The objective is to understand how customer demand responds to price changes and how pricing strategies influence sales performance and revenue.

By applying data preprocessing, statistical modeling, visualization, and regression analysis, this project provides data-driven insights that can support pricing decisions and business strategy development.

The project covers the complete analytics workflow:

* Data Understanding
* Data Cleaning & Pre-processing
* Feature Engineering
* Data Visualization
* Exploratory Data Analysis (EDA)
* Price Elasticity Analysis
* Regression Modeling
* Revenue Simulation

---

## 📁 Project Structure

```text
Price-Elasticity-Analysis-in-Omnichannel-Retail/
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

The dataset contains online retail transaction records including:

* Invoice Number
* Product Description
* Quantity Purchased
* Unit Price
* Customer ID
* Invoice Date
* Country

The data is used to evaluate customer purchasing behavior, product demand, and price sensitivity across retail transactions.

---

## 🧹 Data Understanding & Pre-processing

### Main Tasks

* Dataset inspection
* Missing value detection
* Data cleaning
* Data type conversion
* Feature engineering
* Log transformation
* Seasonal feature extraction
* Categorical encoding
* Lag feature generation
* Outlier detection

### Features Created

| Feature     | Description                |
| ----------- | -------------------------- |
| TotalPrice  | Quantity × UnitPrice       |
| LogQuantity | Log-transformed Quantity   |
| LogPrice    | Log-transformed Unit Price |
| Month       | Transaction Month          |
| DayOfWeek   | Transaction Day            |
| Hour        | Transaction Hour           |
| Lag_1_Day   | Previous Day Sales         |

### Data Cleaning

The preprocessing stage includes:

* Removing missing values
* Removing negative quantities
* Removing invalid prices
* Converting InvoiceDate to datetime format
* Creating additional analytical variables

---

## 📊 Data Visualization

Several visualizations are developed to explore retail sales patterns and pricing behavior.

### Scatter Plot

Relationship between:

* LogPrice
* LogQuantity

Purpose:

* Explore demand response to pricing changes.

---

### Monthly Revenue Trend

Visualization of revenue over time.

Purpose:

* Identify seasonal sales patterns.
* Observe revenue fluctuations.

---

### Price Trend vs Sales

Comparison between:

* Product prices
* Quantity sold

Purpose:

* Analyze pricing effects on demand.

---

### Top Revenue Products

Bar charts displaying:

* Top 10 revenue-generating products

Purpose:

* Identify high-performing products.

---

### Quantity Outlier Detection

Boxplot analysis for:

* Quantity

Purpose:

* Detect abnormal purchasing behavior.

---

### Correlation Analysis

Heatmap displaying relationships among:

* Quantity
* UnitPrice
* TotalPrice
* LogQuantity
* LogPrice

Purpose:

* Identify important business relationships.

---

### Product Elasticity Heatmap

Comparison of:

* Average LogPrice
* Average LogQuantity

Purpose:

* Explore product-level price sensitivity.

---

## 📈 Price Elasticity Analysis

### Ordinary Least Squares (OLS)

Model:

```text
LogQuantity ~ LogPrice
```

Purpose:

* Estimate demand elasticity with respect to price.

Output:

* Elasticity coefficient
* Statistical significance
* Model diagnostics

---

### Fixed Effects Model

Model:

```text
LogQuantity ~ LogPrice + C(Description)
```

Purpose:

* Control for product-specific characteristics.
* Improve elasticity estimation accuracy.

Output:

* Fixed Effects Elasticity
* Product-level controls

---

## 📉 Regression Analysis

### Model 1 – Simple Linear Regression

Target Variable:

```text
LogQuantity
```

Predictor:

```text
LogPrice
```

Evaluation Metrics:

* R² Score
* MAE
* RMSE

Purpose:

* Measure the direct relationship between price and demand.

---

### Model 2 – Multiple Linear Regression

Target Variable:

```text
LogQuantity
```

Predictors:

* LogPrice
* Month
* Hour

Evaluation Metrics:

* R² Score
* MAE
* RMSE

Purpose:

* Evaluate combined effects of pricing and temporal factors on demand.

---

## 💰 Revenue Simulation

A pricing simulation is conducted by increasing prices by 10%.

### Simulation Process

1. Increase UnitPrice by 10%.
2. Estimate new demand using elasticity.
3. Calculate projected revenue.
4. Compare projected revenue with current revenue.

### Outputs

* Predicted Quantity
* New Revenue
* Revenue Difference
* Revenue Growth Percentage

Purpose:

* Support strategic pricing decisions.
* Evaluate revenue impact of price adjustments.

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

### Analytical Techniques

* Data Cleaning
* Feature Engineering
* One-Hot Encoding
* Log Transformation
* Exploratory Data Analysis (EDA)
* Data Visualization
* OLS Regression
* Linear Regression
* Fixed Effects Modeling
* Revenue Simulation

---

## 🚀 How to Run

### Install Required Packages

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
* Descriptive Statistics
* Data Visualizations
* Revenue Analysis
* Price Elasticity Estimates
* Regression Evaluation Metrics
* Revenue Simulation Results

---

## 🎓 Course Information

**Course:** ADY201M

**Project Title:** Price Elasticity Analysis in Omnichannel Retail

**Project Type:** Data Analytics & Business Intelligence

**Tools:** Python, Statistics, Data Visualization, Machine Learning

---

## 📌 Project Objective

The primary objective of this project is to estimate price elasticity in an omnichannel retail environment and evaluate how pricing changes affect customer demand and overall revenue performance.

The findings provide valuable insights that can support pricing strategy, revenue optimization, and data-driven business decision-making.
