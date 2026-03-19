import pandas as pd
import numpy as np


df1 = pd.DataFrame({
    'a' : [1,2],
    'b' : [3,4]
}) 



df2 = pd.DataFrame({
    'a' : [5,6],
    'b' : [7,8]
}) 


# print(df1)
# print(df2)


result1 = pd.concat([df1 , df2] , axis=0)
result2 = pd.concat([df1 , df2] , axis=1)
# print(result2)









# inner --> intersection
# outer --> union


df3 = pd.DataFrame({
    'a' : [1,2],
    'b' : [3,4]
}) 



df4 = pd.DataFrame({
    'a' : [5,6],
    'd' : [7,8]
}) 


result3 = pd.concat([df3 , df4] , join='outer')
# print(result3)



# ignore_index 
result4 = pd.concat([df1 , df2] , ignore_index=False)
# print(result4)



















# label
result5 = pd.concat([df1 , df2] , keys=['RK' , 'IRK'])
# print(result5)




result6 = pd.concat([df1,df2] , keys=['RK' , 'IRK'] , names=['dataset'])
# print(result6)









result7 = pd.concat([df1 , df2] , verify_integrity=False)
# print(result7)








df5 = pd.DataFrame({
    'w' : [1,2],
    'x' : [3,4]
}) 



df6 = pd.DataFrame({
    'v' : [5,6],
    's' : [7,8]
}) 

result8 = pd.concat([df5 , df6] , sort=False)
# print(result8)