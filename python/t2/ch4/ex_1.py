import pandas as pd

df = pd.read_csv("Book1.csv")
# print(df)


import matplotlib.pyplot as plt
import numpy as np
plt.scatter(df['cgpa'] , df['package'])
plt.xlabel('CGPA')
plt.ylabel('PACKAGE')


x = df[['cgpa']]    # x is 2 dimensional
y = df['package']   # y is 1 dimensional

# plt.show()


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_train.shape, x_test.shape, y_train.shape ,y_test.shape)



from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)

m = lr.coef_ # slope(m)
c = lr.intercept_ # constant(c)

# print(m, c)
# print(m*5.65 + c)

y2= lr.predict([[5.65]])
# print(y2)



from sklearn.metrics import mean_squared_error

y_pred = lr.predict(x_test)
print('MSE:', mean_squared_error(y_test, y_pred))
# print(y_pred) 