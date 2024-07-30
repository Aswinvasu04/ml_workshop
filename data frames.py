import pandas as pd
data={
    'name':['alice','bob','charlie'],
    'age':[23,30,28],
    'city':['new york','los angels','chennai']
}
df=pd.DataFrame(data)
print(df)