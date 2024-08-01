import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data={
    'square footage':[1500,1600,1700,1800,1900,2000],
    'num_bedrooms':[3,3,4,1,1,2],
    'price':[30000,32000,34000,36000,38000,40000]
}
df = pd.DataFrame(data)

x=df[['square footage','num_bedrooms']]
y=df['price']
model = LinearRegression()
model.fit(x,y)

predicted_prices=model.predict(x)

print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")