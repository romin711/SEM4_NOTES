import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("RealEstate.csv")

# print(df.head(5))

# print(df.columns)


x = df[['No', 'X1 transaction date', 'X2 house age',
       'X3 distance to the nearest MRT station',
       'X4 number of convenience stores', 'X5 latitude', 'X6 longitude']]

y = df['Y house price of unit area']

# print(df.isna())
# print(df.isna().sum())




from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 110)



from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)



from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


y_pred = lr.predict(x_test)
print(y_pred)
print('MSE:', mean_squared_error(y_test, y_pred))

print('MAE:', mean_absolute_error(y_test, y_pred))

print('R2_SCORE:', r2_score(y_test, y_pred))

# print(y_pred)