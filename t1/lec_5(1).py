import pandas as pd
import numpy as np

employee = pd.DataFrame( {
    'emp_id' : [1,2,3],
    'name' : ['a' , 'b' , 'c'],
    'dep_id' : [10,20,30]
})

department = pd.DataFrame ({
    'dep_id' : [10,20,40],
    'dep_name' : ['hr' , 'it' , 'finance']
})

# print(pd.merge(employee , department , on='dep_id'))
# print(pd.merge(employee , department , how='outer'))




# how='left'
# print(pd.merge(employee , department , how='left'))






employee1 = pd.DataFrame( {
    'emp_id' : [1,2,3],
    'name' : ['a' , 'b' , 'c'],
    'd_id' : [10,20,30]
})

# print(pd.merge(employee1 , department , left_on='d_id' , right_on='dep_id'))






# merge using index

employee2 = pd.DataFrame( {
    'emp_id' : [1,2],
    'name' : ['a' , 'b'],
    'dep_id' : [10,20]
})

department2 = pd.DataFrame ({
    'd_id' : [10,20],
    'dep_name' : ['hr' , 'it']
})

# print(pd.merge(employee2 , department2 , left_index=True , right_index=True))







# suffixes
employee3 = pd.DataFrame( {
    'emp_id' : [1,2],
    'name' : ['a' , 'b'],
    'dep_id' : [10,20]
})

department3 = pd.DataFrame ({
    'dep_id' : [10,20],
    'dep_name' : ['hr' , 'it'],
    'name' : ['x' , 'y']
})

# print(pd.merge(employee3 , department3 , on='dep_id'))
# print(pd.merge(employee3 , department3 , on='dep_id' , suffixes=('_emp' , '_dept')))
# print(pd.merge(employee , department , how='outer' , indicator=True))





