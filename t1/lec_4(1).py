import pandas as pd

data = {
    'a' : [10,20,30],
    'b' : [5,15,25]
}

df = pd.DataFrame(data)
# print(df)

# print(df.apply(sum))
# print(df.apply(sum , axis = 1))





# using lambda
# print(df.apply(lambda x:x**2 ))





# using user define function
def square(x):
    return x**2

df['square'] = df['a'].apply(square)
# print(df)




def cube(y):
    return y**3

df['cube'] = df['b'].apply(cube)
# print(df)











# apply function using parameter
def calc(x , a , b):
    return x*(a+b)

df['result'] = df['a'].apply(calc , args = (3,4))
# print(df)











# astype function
df['result'] = df['result'].astype(float)
# print(df)






# replace()
# print(df.replace(10 , 1000))

print(df.replace({
    5:50,
    400:500.0,
    70.0:700
}))