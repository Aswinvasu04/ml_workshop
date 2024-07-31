import pandas as pd
from sklearn.preprocessing import StandardScaler

data={
    'A':[1,2,None,3],
    'B':[None,2,4,5],
    'C':[1,None,6,7],
}
df=pd.DataFrame(data)

scaler=StandardScaler()
df_standardized=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print("\n after standardization:\n",df_standardized)