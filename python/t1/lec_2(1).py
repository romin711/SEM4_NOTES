# set_index
# reset_index

import pandas as pd

data = {
    'age': [25, 30, 35, 40],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
# print("Original DataFrame:")
# print(df)




# print(df.set_index('age', drop=False))
# print(df.set_index('age', drop=True))



# df.set_index('age', inplace=True)
# print(df)




df.reset_index(inplace=True, drop=True)
print(df)