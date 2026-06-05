# ============================================
# PART 5 - DATA VISUALIZATION
# EACH CHART IN SEPARATE WINDOW
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

df = pd.read_csv(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\cleaned_online_retail.csv'
)

sns.set_style("whitegrid")

# ============================================
# 1. SCATTER: LOG PRICE VS LOG QUANTITY
# ============================================

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df.sample(10000, random_state=42),
    x='LogPrice',
    y='LogQuantity',
    alpha=0.3
)

plt.title('Scatter Plot: Log Price vs Log Quantity')
plt.xlabel('Log Price')
plt.ylabel('Log Quantity')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 2. LINE CHART: MONTHLY REVENUE TREND
# ============================================

monthly_revenue = (
    df.groupby('Month')['TotalPrice']
    .sum()
    .reset_index()
)

plt.figure(figsize=(9, 6))

sns.lineplot(
    data=monthly_revenue,
    x='Month',
    y='TotalPrice',
    marker='o'
)

plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 3. LINE CHART: PRICE TREND VS SALES
# ============================================

monthly_price_sales = (
    df.groupby('Month')
    .agg(
        AvgPrice=('UnitPrice', 'mean'),
        TotalQuantity=('Quantity', 'sum')
    )
    .reset_index()
)

fig, ax1 = plt.subplots(figsize=(9, 6))

sns.lineplot(
    data=monthly_price_sales,
    x='Month',
    y='AvgPrice',
    marker='o',
    ax=ax1,
    label='Average Price'
)

ax2 = ax1.twinx()

sns.lineplot(
    data=monthly_price_sales,
    x='Month',
    y='TotalQuantity',
    marker='o',
    ax=ax2,
    label='Total Quantity'
)

ax1.set_title('Price Trend vs Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Average Price')
ax2.set_ylabel('Total Quantity')

fig.tight_layout()
plt.show(block=False)


# ============================================
# 4. BAR CHART: TOP 10 REVENUE PRODUCTS
# ============================================

top_products = (
    df.groupby('Description')['TotalPrice']
    .sum()
    .nlargest(10)
    .reset_index()
)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_products,
    y='Description',
    x='TotalPrice'
)

plt.title('Top 10 Revenue Products')
plt.xlabel('Revenue')
plt.ylabel('Product')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 5. BOXPLOT: QUANTITY OUTLIERS
# ============================================

plt.figure(figsize=(9, 5))

sns.boxplot(
    x=df['Quantity']
)

plt.title('Box Plot: Quantity Outliers')
plt.xlabel('Quantity')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 6. HEATMAP: CORRELATION MATRIX
# ============================================

corr_matrix = df[
    [
        'Quantity',
        'UnitPrice',
        'TotalPrice',
        'LogQuantity',
        'LogPrice'
    ]
].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Matrix')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 7. ELASTICITY HEATMAP BY PRODUCT
# ============================================

product_summary = (
    df.groupby('Description')
    .agg(
        AvgLogPrice=('LogPrice', 'mean'),
        AvgLogQuantity=('LogQuantity', 'mean'),
        TotalQuantity=('Quantity', 'sum')
    )
    .reset_index()
)

product_summary = (
    product_summary[
        product_summary['TotalQuantity'] > 100
    ]
    .sort_values('TotalQuantity', ascending=False)
    .head(10)
)

heatmap_data = product_summary[
    [
        'Description',
        'AvgLogPrice',
        'AvgLogQuantity'
    ]
].set_index('Description')

plt.figure(figsize=(10, 8))

sns.heatmap(
    heatmap_data,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Elasticity Heatmap by Product')

plt.tight_layout()
plt.show(block=False)


# ============================================
# 8. OPTIMAL PRICE CURVE
# ============================================

model = smf.ols(
    'LogQuantity ~ LogPrice',
    data=df
).fit()

elasticity = model.params['LogPrice']

price_change_range = np.linspace(0.7, 1.5, 50)

revenue_simulation = []

for price_change in price_change_range:
    predicted_quantity = (
        df['Quantity']
        *
        (price_change ** elasticity)
    )

    new_price = df['UnitPrice'] * price_change

    new_revenue = (
        new_price
        *
        predicted_quantity
    ).sum()

    revenue_simulation.append(new_revenue)

simulation_df = pd.DataFrame({
    'PriceMultiplier': price_change_range,
    'SimulatedRevenue': revenue_simulation
})

plt.figure(figsize=(9, 6))

sns.lineplot(
    data=simulation_df,
    x='PriceMultiplier',
    y='SimulatedRevenue'
)

plt.axvline(
    x=1.0,
    linestyle='--'
)

plt.title('Optimal Price Curve')
plt.xlabel('Price Multiplier')
plt.ylabel('Simulated Revenue')

plt.tight_layout()
plt.show(block=False)


# ============================================
# KEEP WINDOWS OPEN
# ============================================

input("Press Enter to close all charts...")