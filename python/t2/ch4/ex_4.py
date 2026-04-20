import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("winequality.csv")


df.drop(columns='Id', inplace=True)

# print(df.head(5))

# print(df.columns)
x = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]
y = df[ 'quality']


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
# print(x_test.shape)
# print(x_train.shape)
# print(y_test.shape)
# print(y_train.shape)


from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)

m = lr.coef_ # slope(m)
c = lr.intercept_ # constant(c)

# print('slop: ',m , 'constant: ', c)

y2 = lr.predict([[8, 0.4, 0.40, 15, 0.048, 40, 150, 0.99, 3, 0.45, 10.5]])
print(y2)




from sklearn.metrics import mean_squared_error

y_pred = lr.predict(x_test)
print('MSE:', mean_squared_error(y_test, y_pred))
# print(y_pred)