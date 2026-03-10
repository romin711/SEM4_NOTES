import pandas as pd
import numpy as np
# \\192.168.101.51

# create dataframe by using dictionary
data = {
    "romin" : ['a' , 'b' , 'c'],
    "marks" : [85 , 90 , 74],
    "city" : ["ahm" , "surat" , "vadodara"]
    }

# key name --> columns name

df = pd.DataFrame(data)
# print(df)




# create dataframe by using list
data1 = [
    ['a' , 80],
    ['b' , 89],
    ['c' , 70]
]
df1 = pd.DataFrame(data1 , columns=['name' , "marks"] , index=[1,2,3])
# print(df1)





# create dataframe by using list of dictionary
data2 = [
    {'name' : 'a' , 'marks' : 80},
    {'name' : 'b' , 'marks' : 89},
]
df2 = pd.DataFrame(data2)
# print(df2)





# create dictionary by using pandas series
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
df3 = pd.DataFrame({'col1' : s1, 
                    'col2' : s2})

# print(df3.set_index('col1'))





# read csv file 
df4 = pd.read_csv("auto-mpg.csv")

# print(df4)
# print(df4.head())
# print(df4.head(10))
# print(df4.tail(10))
# print(df4.columns)
# print(df4.shape)





# loc function

# print(df4.loc[0:11])
# print(df4[['mpg']])
# print(df4[['mpg' , 'cylinders' , 'weight']])

# print(df4[['weight','acceleration','model year' , 'origin' , 'car name']].tail(5))
# print(df4[['weight','acceleration','model year' , 'origin' , 'car name']].loc[199:207])





# iloc


print(df4.iloc[ 11:33:3 , 3:10:2 ]) # [row , column]