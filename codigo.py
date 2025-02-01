import pandas as pd

df= pd.DataFrame({'A': [1,2,3,4,5], 'B': [6,7,8,9,10]})
print(df)
print(df.dtypes)
print(df.shape) 

help(pd.merge)