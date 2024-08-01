import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

square_footage=np.array([1500,1600,1700,1800,1900,2000]).reshape(-1,1)
prices=np.array([30000,32000,34000,36000,38000,40000])

model = LinearRegression()
model.fit(square_footage,prices)

predicted_price=model.predict(square_footage)

plt.scatter(square_footage,prices,color='blue',label='actual prices')
plt.plot(square_footage,predicted_price,color='red',label='predicted prices')
plt.xlabel('square footage')
plt.ylabel('price')
plt.title(' simple Linear Regression')
plt.show()