# pandas series : 1d data

import pandas as pd
import numpy as np


marks = [78 , 89 , 55 , 90]
name = ["maths" , "physics" , "chemistry" , "english"]

s = pd.Series(marks, index=name)
# print("using list: " + s)






# create series by uisng tupple
marks1 = (78 , 89 , 55 , 90)
name1 = ["maths" , "physics" , "chemistry" , "english"]

s1 = pd.Series(marks1, index=name1)
# print("using tupple: " + s1)






# create series by using dictionary
marks2 = {'a' : 10,
          'b' : 20,
          'c' : 30
          }

# print("using dictionary: " + pd.Series(marks2))






# create series by using array
a = np.array([40 , 50 , 60 , 70])
print("using array:\n" , pd.Series(a))