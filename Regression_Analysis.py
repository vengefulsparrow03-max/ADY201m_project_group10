# ============================================
# PART 6 - REGRESSION ANALYSIS
# ============================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ============================================
# LOAD DATA
# ============================================

df = pd.read_csv(
    r'C:\Users\ADMIN\Downloads\ADY201m_project\cleaned_online_retail.csv'
)

# ============================================
# MODEL 1
# SIMPLE REGRESSION
# ============================================

Y = df['LogQuantity']

X = df[
    [
        'LogPrice'
    ]
]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    Y_train
)

Y_pred = model.predict(X_test)

print("\n===== SIMPLE REGRESSION =====")

print("Intercept:")
print(model.intercept_)

print("\nCoefficient:")
print(model.coef_)

r2 = r2_score(
    Y_test,
    Y_pred
)

mae = mean_absolute_error(
    Y_test,
    Y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        Y_test,
        Y_pred
    )
)

print("\nR² =", r2)
print("MAE =", mae)
print("RMSE =", rmse)

print(
    "\nElasticity =",
    model.coef_[0]
)

# ============================================
# MODEL 2
# MULTIPLE REGRESSION
# ============================================

Y = df['LogQuantity']

X = df[
    [
        'LogPrice',
        'Month',
        'Hour'
    ]
]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

multi_model = LinearRegression()

multi_model.fit(
    X_train,
    Y_train
)

Y_pred_multi = multi_model.predict(
    X_test
)

print("\n")
print("===== MULTIPLE REGRESSION =====")

print("Intercept:")
print(
    multi_model.intercept_
)

print(
    "\nCoefficients:"
)

for col, coef in zip(
    X.columns,
    multi_model.coef_
):
    print(
        col,
        "=",
        coef
    )

r2_multi = r2_score(
    Y_test,
    Y_pred_multi
)

mae_multi = mean_absolute_error(
    Y_test,
    Y_pred_multi
)

rmse_multi = np.sqrt(
    mean_squared_error(
        Y_test,
        Y_pred_multi
    )
)

print("\nR² =", r2_multi)
print("MAE =", mae_multi)
print("RMSE =", rmse_multi)