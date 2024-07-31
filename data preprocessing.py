import pandas as pd
data={
    'A':[1,2,None,3],
    'B':[None,2,4,5],
    'C':[1,None,6,7],
}
df=pd.DataFrame(data)
df_dropped=df.dropna
print("after dropping rows with missing values:\n",df_dropped)

df_dropped_cols=df.dropna(axis=1)
print("after dropping columns with missing values:\n",df_dropped_cols)
