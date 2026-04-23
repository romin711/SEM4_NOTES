import pandas as pd

df = pd.read_csv('windpower.csv')
# print(df.head(5))
# print(df.isna().sum())
df.dropna(inplace=True)
# print(df.isna().sum())





print(df.columns)
x = df[['Wind speed (m/s)']]    
y = df['Power (kW)']  



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)




from sklearn.preprocessing import PolynomialFeatures 

list = [3,4,5,6]

from sklearn.linear_model import LinearRegression

for i in list:
    poly = PolynomialFeatures(degree=i)
    x_train_poly_1 = poly.fit_transform(x_train)

    lr = LinearRegression()
    model = lr.fit(x_train_poly_1, y_train)

    x_train_poly_2 = poly.transform(x_test)
    y_pred = model.predict(x_train_poly_2)

