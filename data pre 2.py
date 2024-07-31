import pandas as pd
from sklearn.impute import SimpleImputer

data={
    'A':[1,2,None,3],
    'B':[None,2,4,5],
    'C':[1,None,6,7],
}
df=pd.DataFrame(data)

imputer=SimpleImputer(strategy='mean')
df=imputed=pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
print("\nafter imputing missing values:\n",df_imputed)
