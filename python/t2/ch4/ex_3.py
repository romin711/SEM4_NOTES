import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("car data.csv")
# print(df.head(5))
# print(df.isna().sum())

df['age'] = 2026 - df['Year']
# print(df.head(5))

df.drop(columns='Year', inplace=True)
df.drop(columns='Car_Name', inplace=True)

df = pd.get_dummies(data=df, drop_first=True)



# print(df.head(5))
# print(df.columns)
x = df[['Present_Price', 'Kms_Driven', 'Owner', 'age',
       'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual',
       'Transmission_Manual']]
y = df['Selling_Price']





from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_test.shape)
# print(x_train.shape)
# print(y_test.shape)
# print(y_train.shape)




from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)
print(lr)


m = lr.coef_ # slope(m)
c = lr.intercept_ # constant(c)

# print('slop: ',m , 'constant: ', c)


y2 = lr.predict([[8.5,45000,0,8,0,1,1,1]])
print(y2)




from sklearn.metrics import mean_squared_error

y_pred = lr.predict(x_test)
print('MSE:', mean_squared_error(y_test, y_pred))
print(y_pred)


# 8 year old
# petrol
# manual 
# 45000 km
# owner 0
# 8.5 lakh
# individual