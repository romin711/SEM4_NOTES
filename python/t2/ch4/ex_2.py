import pandas as pd

df = pd.read_csv("student_scores.csv")
# print(df)


import matplotlib.pyplot as plt
import numpy as np
plt.scatter(df['Hours'] , df['Scores'])
# plt.xlabel('CGPA')
# plt.ylabel('PACKAGE')
# plt.show()

x = df[['Hours']]    # x is 2 dimensional
y = df['Scores']   # y is 1 dimensional


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)





from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)




from sklearn.metrics import mean_squared_error

y_pred = lr.predict(x_test)
print('MSE:', mean_squared_error(y_test, y_pred))
# print(y_pred) 