# ============================================
# Data Understanding and data pre_processing 
# ============================================

# ============================================
# 1. IMPORT LIBRARIES
# ============================================

# pandas: xử lý dữ liệu
import pandas as pd

# numpy: tính toán toán học
import numpy as np

# seaborn + matplotlib: vẽ biểu đồ
import seaborn as sns
import matplotlib.pyplot as plt

# os: kiểm tra thư mục hiện tại
import os


# ============================================
# 2. CHECK CURRENT DIRECTORY
# ============================================

print("===== CURRENT DIRECTORY =====")
print(os.getcwd())

print("\n===== FILES IN CURRENT DIRECTORY =====")
print(os.listdir())


# ============================================
# 3. LOAD DATASET
# ============================================

df = pd.read_excel(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\Online Retail.xlsx'
)

print("\nDataset loaded successfully!")


# ============================================
# 4. UNDERSTANDING THE DATA
# ============================================

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())


# ============================================
# 5. CHECK MISSING VALUES
# ============================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# ============================================
# 6. DATA CLEANING
# ============================================

df = df.dropna()

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

print("\nData cleaning completed!")


# ============================================
# 7. CONVERT DATA TYPES
# ============================================

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

print("\nDatetime conversion completed!")


# ============================================
# 8. FEATURE ENGINEERING
# ============================================

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("\nTotalPrice feature created!")


# ============================================
# 9. LOG TRANSFORMATION
# ============================================

df['LogQuantity'] = np.log1p(df['Quantity'])

df['LogPrice'] = np.log1p(df['UnitPrice'])

print("\nLog transformation completed!")


# ============================================
# 10. SEASONALITY FEATURES
# ============================================

df['Month'] = df['InvoiceDate'].dt.month

df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()

df['Hour'] = df['InvoiceDate'].dt.hour

print("\nSeasonality features created!")


# ============================================
# 11. CATEGORICAL ENCODING
# ============================================

# Country được dùng làm channel proxy
# Chuyển Country thành dạng số bằng One-Hot Encoding

df_encoded = pd.get_dummies(
    df,
    columns=['Country']
)

print("\nCategorical encoding completed!")
print(df_encoded.head())


# ============================================
# 12. CREATE LAG FEATURES
# ============================================

daily_sales = df.groupby(
    df['InvoiceDate'].dt.date
)['TotalPrice'].sum()

daily_sales = daily_sales.reset_index()

daily_sales.columns = ['Date', 'TotalSales']

daily_sales['Lag_1_Day'] = (
    daily_sales['TotalSales'].shift(1)
)

print("\n===== DAILY SALES WITH LAG FEATURE =====")
print(daily_sales.head())


# ============================================
# 13. OUTLIER DETECTION
# ============================================

plt.figure(figsize=(8, 5))

sns.boxplot(x=df['Quantity'])

plt.title('Boxplot of Quantity')

plt.show(block=False)


plt.figure(figsize=(8, 5))

sns.boxplot(x=df['UnitPrice'])

plt.title('Boxplot of UnitPrice')

plt.show()


# ============================================
# 14. FINAL DATASET INFO
# ============================================

print("\n===== FINAL DATASET INFO =====")
print(df_encoded.info())

print("\n===== FINAL DATASET HEAD =====")
print(df_encoded.head())


# ============================================
# 15. SAVE CLEANED DATASET
# ============================================

df_encoded.to_csv(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\cleaned_online_retail.csv',
    index=False
)

print("\nData preprocessing completed successfully!")

print(
    "Cleaned dataset saved as 'cleaned_online_retail.csv'"
)