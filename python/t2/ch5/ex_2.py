import pandas as pd

df = pd.read_csv('PlayTennis.csv')
print(df.head(5))
print(df.isna().sum())



import numpy as np




df = pd.get_dummies(data=df, drop_first=True)
# print(df)

# print(df.columns)

x = df[['windy', 'outlook_rainy', 'outlook_sunny', 'temp_hot', 'temp_mild',
       'humidity_normal']]    
y = df['play_yes']



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)





from sklearn.neighbors import KNeighborsClassifier
# print(11**0.5)

nn = KNeighborsClassifier(n_neighbors=3)

model = nn.fit(x_train, y_train)

y_pred = model.predict(x_test)




from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]




# print('TN:', TN)
# print('FP:', FP)
# print('FN:', FN)
# print('TP:', TP)

total = TN+TP+FN+FP

accuracy = (TN+TP)/total
error_rate = (FP+FN)/total
sensitivity = TP/(TP+FN)
specificity = TN/(TN+FP)

# print('accuracy:', accuracy)
# print('error_rate:', error_rate)
# print('sensitivity:', sensitivity)
# print('specificity:', specificity)




# x = df[['windy', 'outlook_rainy', 'outlook_sunny', 'temp_hot', 'temp_mild', 'humidity_normal']] 
predict = model.predict([[True, True, False, False, False, False]])
print(predict)

# print(df.columns)