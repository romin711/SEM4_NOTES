import pandas as pd 

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Los Angeles', 'New York'],
}

df = pd.DataFrame(data)
print(df['city'].unique())
print(df['city'].nunique())
print(df.value_counts())

# print(df)