# -*- coding: utf-8 -*-
"""first_ms_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oj7r-99HuMaTdkQqbajDHqSnTAcvr45E

# Load data
"""

import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
df

"""# Data preparation """

y = df['logS']
y

X = df.drop('logS', axis=1)
X

"""# Data spliting"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

X_test

"""## Model building

# Linear regression
"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

"""# Applying the model to make a prediction"""

y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)

"""# Evaluate model performance"""

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

print('LR MSE (Train):', lr_train_mse)
print('LR R2 (Train): ', lr_train_r2)
print('LR MSE (Test):', lr_test_mse)
print('LR R2 (Test): ', lr_test_r2)

lr_results = pd.DataFrame(['Linear regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Method', 'MSE (Train)', 'R2 (Train)', 'MSE (Test)', 'LR R2 (Test)']
lr_results

"""## Randome Forest

# Train the model
"""

from sklearn.ensemble._hist_gradient_boosting.gradient_boosting import Y_DTYPE
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

rf_results = pd.DataFrame(['Random forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'MSE (Train)', 'R2 (Train)', 'MSE (Test)', 'LR R2 (Test)']
rf_results

"""# Model comparison"""

df_models = pd.concat([lr_results, rf_results], axis=0)

df_models.reset_index(drop=True)

"""## Data visualization of prediction results"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_train, y=y_lr_train_pred, alpha=0.3)

z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train, p(y_train), color='red')
plt.ylabel('Predict logS')
plt.xlabel('Experimental LogS')

