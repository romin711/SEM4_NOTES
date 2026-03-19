# data cleaning

import pandas as pd
import numpy as np

data = {
    "name" : ['a' , 'b' , 'c' , 'd' , np.nan],
    "marks" : [85 , np.nan , 78 , 89 , np.nan],
    "city" : ['ahm' , 'delhi' , np.nan , 'mumbai' , np.nan] 
}

df = pd.DataFrame(data)
# print(df)









# print(df.isnull())

# print(df.isna().sum())













# print(df.dropna())

# print(df.dropna(thresh=2)) # must have minimum 2 valid data

# print(df.dropna(how='any'))

# print(df.dropna(how='all'))

# print(df.dropna(subset=['city']))

# print(df.dropna(axis=0))

# print(df.dropna(axis=1))

# print(df)












# print(df.fillna(100))

# print(df['city'].fillna('surat'))

# print(df.drop(index=0)) #print(df.drop(1))

# print(df.drop(columns=['city']))

# print(df.drop("name" , axis=1))













df.loc[5] = ['a' , 85.0 , 'ahm']
# print(df)


# print(df.drop_duplicates(keep='last'))

# print(df.duplicated(keep='last'))












# data sorting
data2 = {
    'name' : ['a' , 'b' , 'c' , 'd'],
    'marks' : [85 , 76 , 45 , 89],
}

df2 = pd.DataFrame(data2)
# print(df2)

# print(df2.sort_values(by='marks' , ascending=False))

# print(df2.sort_index(ascending=False))

# print(df2.sort_index(axis=1))