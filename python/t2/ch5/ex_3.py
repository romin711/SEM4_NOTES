
# Given the Breast Cancer Wisconsin (Diagnostic) dataset, the objective is to build a kNN classification model that accurately 
# predicts whether a tumor is benign or malignant based on the diagnostic features provided. The model should be trained on a 
# portion of the dataset and evaluated on another portion to assess its performance. The ultimate goal is to create a reliable 
# classifier that can assist healthcare professionals in diagnosing breast cancer accurately and early. Use cancer.csv file for 
# dataset.


import pandas as pd

df = pd.read_csv('data_breast_cancer.csv')
# print(df.head(5))
# print(df.isna().sum())

df.drop(columns='Unnamed: 32', inplace=True)
df.drop(columns='id', inplace=True)


# print(df.columns)

x = df[['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']]    

y = df['diagnosis']


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_train.shape)




from sklearn.neighbors import KNeighborsClassifier
# print(455**0.5)

nn = KNeighborsClassifier(n_neighbors=21)

model = nn.fit(x_train, y_train)

y_pred = model.predict(x_test)
# print(y_pred)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)


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


# print(df.head(1))
# predict = model.predict([[4,85,55,30,180,29.0,0.5,51]])
# print(predict)