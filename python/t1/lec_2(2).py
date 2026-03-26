import pandas as pd

df = pd.read_csv('ipl-matches.csv')

# print(df.head())
# print(df.dtypes)
# print(df.sample(3))
# print(df.size)
# print(df.ndim)
# print(df.index
# print(df.values)

data = {
    'age': [25, 30, 35, 40],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
# print(df.loc[0:1])
# print(df[["name" , "city"]].loc[0:1])
# print(df[['age' , 'city']].loc[0::2])

df.loc[1, 'city'] = 'San Francisco'
# print(df)

df.loc[:, 'ratings'] = [4.5, 4.0, 3.5, 5.0]
# print(df)

df.loc[5] = [45, 'Eve', 'Seattle', 4.8]
# print(df)


# print(df.iloc[::-1 , ::-1])

df.iloc[1,1] = 'Bob Smith'
# print(df)

# print(df.info())

print(df.describe(include='all'))