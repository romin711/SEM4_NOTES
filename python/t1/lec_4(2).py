import pandas as pd
import numpy as np

# groupby function
data = {
    'department' : ['it' , 'it' , 'hr' , 'hr' , 'sales'],
    'employee' : ['a' , 'b' , 'c' , 'd' , 'e'],
    'salary' : [50000 , 60000 , 47000 , 48000 , 52000] 

}

df = pd.DataFrame(data)
# print(df)









# grp by department
# print(df.groupby('department'))






# print(df.groupby('department')['salary'].sum())
# print(df.groupby('department')['salary'].mean())
# print(df.groupby('department')['salary'].median())








# aggregation function
# print(df.groupby('department')['salary'].agg(['sum' , 'mean' , 'max']))






# print(df.groupby('department')['salary'].apply(lambda x : x.max() - x.min()))






# print(df.groupby('department').sample(1))






# print(df.groupby('department').size())






# print(df.groupby('department').nth(0))






# print(df.groupby('department').groups)






# print(df.groupby('department').nunique())






