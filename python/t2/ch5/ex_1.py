import pandas as pd

df = pd.read_csv('diabetes.csv')
# print(df.head(5))
# print(df.isna().sum())


import numpy as np


# print(df.columns)
x = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]    
y = df['Outcome']  



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)


from sklearn.neighbors import KNeighborsClassifier
# print(614**0.5)

nn = KNeighborsClassifier(n_neighbors=25)

model = nn.fit(x_train, y_train)

y_pred = model.predict(x_test)
# print(y_pred)


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



predict = model.predict([[4,85,55,30,180,29.0,0.5,51]])
print(predict)