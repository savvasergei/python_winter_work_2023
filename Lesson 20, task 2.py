import pandas as pd
dct = {'name':['a','b','c'], id:[1,2,3]}
df = pd.DataFrame(dct)
x = df.sum(numeric_only=True)
print(*x)