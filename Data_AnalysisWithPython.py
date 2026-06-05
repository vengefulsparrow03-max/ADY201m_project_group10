# ============================================
# ONLINE RETAIL - DATA ANALYSIS WITH PYTHON
# ============================================

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# ============================================
# 1. LOAD CLEANED DATASET
# ============================================

df = pd.read_csv(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\cleaned_online_retail.csv'
)

print("Dataset loaded successfully!")
print(df.head())
print(df.info())


# ============================================
# 2. BASIC SALES ANALYSIS
# ============================================

# Top 10 sản phẩm có doanh thu cao nhất
top_revenue_products = (
    df.groupby('Description')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 REVENUE PRODUCTS =====")
print(top_revenue_products)


# Top 10 sản phẩm bán nhiều nhất
top_quantity_products = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 QUANTITY PRODUCTS =====")
print(top_quantity_products)


# Doanh thu theo tháng
monthly_revenue = (
    df.groupby('Month')['TotalPrice']
    .sum()
)

print("\n===== MONTHLY REVENUE =====")
print(monthly_revenue)


# ============================================
# 3. PRICE ELASTICITY MODEL
# ============================================

# OLS model: log(Q) ~ log(P)
# LogQuantity là log(Q), LogPrice là log(P)

model = smf.ols(
    formula='LogQuantity ~ LogPrice',
    data=df
).fit()

print("\n===== OLS MODEL: LOG QUANTITY ~ LOG PRICE =====")
print(model.summary())


# Elasticity = hệ số của LogPrice
elasticity = model.params['LogPrice']

print("\nEstimated Price Elasticity:", elasticity)


# ============================================
# 4. FIXED EFFECTS BY PRODUCT
# ============================================

# Lấy top 50 sản phẩm phổ biến để tránh model quá nặng
top_products = (
    df['Description']
    .value_counts()
    .head(50)
    .index
)

df_fe = df[df['Description'].isin(top_products)]

model_fe = smf.ols(
    formula='LogQuantity ~ LogPrice + C(Description)',
    data=df_fe
).fit()

print("\n===== FIXED EFFECTS MODEL =====")
print(model_fe.summary())

elasticity_fe = model_fe.params['LogPrice']

print("\nFixed Effects Price Elasticity:", elasticity_fe)


# ============================================
# 5. REVENUE SIMULATION
# ============================================

# Giả sử tăng giá 10%
price_increase = 1.10

df['NewPrice'] = df['UnitPrice'] * price_increase

# Dự đoán Quantity mới dựa trên elasticity
df['PredictedQuantity'] = (
    df['Quantity'] *
    (price_increase ** elasticity)
)

df['NewRevenue'] = (
    df['NewPrice'] *
    df['PredictedQuantity']
)

old_revenue = df['TotalPrice'].sum()
new_revenue = df['NewRevenue'].sum()
revenue_change = new_revenue - old_revenue
revenue_change_percent = (revenue_change / old_revenue) * 100

print("\n===== REVENUE SIMULATION =====")
print("Old Revenue:", old_revenue)
print("New Revenue after 10% price increase:", new_revenue)
print("Revenue Change:", revenue_change)
print("Revenue Change (%):", revenue_change_percent)


# ============================================
# 6. SAVE ANALYSIS RESULT
# ============================================

df.to_csv(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\online_retail_python_analysis.csv',
    index=False
)

print("\nPython data analysis completed successfully!")