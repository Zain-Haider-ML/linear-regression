# -*- coding: utf-8 -*-
"""Linear regression for student-performance-factors.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PmaVwlJ6ncMzERrnhea_C-Nim73-q4pw
"""

#!/bin/bash
# !kaggle datasets download lainguyn123/student-performance-factors

# !unzip student-performance-factors.zip

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.datasets import make_regression
from sklearn.feature_selection import mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/StudentPerformanceFactors.csv')
df.head()

df.info()

df.isna().sum()

df.dropna(axis = 0, inplace = True)
df.isna().sum()

len(df)

df.head()

# Define the columns that you want to encode
columns_to_encode = ['Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Motivation_Level', 'Internet_Access',
                     'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence', 'Learning_Disabilities',
                     'Parental_Education_Level', 'Distance_from_Home', 'Gender']  # Add all columns to encode here

# Label encoder object
label_encoder = preprocessing.LabelEncoder()

# Apply label encoding for each column
for col in columns_to_encode:
    df[col] = label_encoder.fit_transform(df[col])

x = df.drop('Exam_Score', axis = 1)
y = df['Exam_Score']
idx = mutual_info_regression(x, y)

cols = idx > 0
columns_to_select = x.columns[cols]
x = x[columns_to_select]

ss = StandardScaler()
x = ss.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.05)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
r2_score(y_test, y_pred)

joblib.dump(model, 'linear_regression_model.pkl')

