# decision tree(classification algorithm)

import pandas as pd

df = pd.read_csv('DecisionTreeDataset.csv')
# print(df.head(5))
# print(df.isna().sum())

df = pd.get_dummies(data=df, drop_first=True)
# print(df.head(5))


# print(df.columns)

x = df[['CGPA_Low', 'CGPA_Medium', 'Communication_Good', 'Apptitude_Low',
       'Programming Skill_Good']]    

y = df['Job Offered_Yes']



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)


from sklearn.tree import DecisionTreeClassifier, plot_tree
model = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)

model.fit(x_train, y_train)





y_pred = model.predict(x_test)
# print(y_pred)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
# print(cm)

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

# print('TN:', TN)
# print('FP:', FP)
# print('FN:', FN)
# print('TP:', TP)


# total = TN+TP+FN+FP

# accuracy = (TN+TP)/total
# error_rate = (FP+FN)/total
sensitivity = TP/(TP+FN)
# specificity = TN/(TN+FP)
precision = TP/(TP+FP)
# print(precision)


# print('accuracy:', accuracy)


# print('error_rate:', error_rate)


# print('sensitivity:', sensitivity)


# print('specificity:', specificity)

import matplotlib.pyplot as plt
plot_tree(model)
# plt.show()



from sklearn.metrics import classification_report
# print(classification_report(y_pred,y_test))



from sklearn.metrics import accuracy_score, recall_score
accuracy_1 = accuracy_score(y_test, y_pred)
sensititvity_1 = recall_score(y_test, y_pred)
# print(accuracy_1)
# print(sensititvity_1)