import pandas as pd

data = [
'python',       
'java',
'c++',
'c#',
'css',        
]

series = pd.Series(data, index=['a','b','c','d','e'])
print(series)

#index a b c
