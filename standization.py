import pandas as pd
data={
    'A':[1,2,3],
    'B':[2,4,5],

}
df=pd.DataFrame(data)
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
df_normalized=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print("\n after normalization:\n",df_normalized)