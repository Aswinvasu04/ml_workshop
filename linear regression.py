import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

np.random.seed(0)
x= 2* np.random.rand(100,1)
y= 4+3+x + np.random.rand(100,1)

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

plt.scatter(x, y,color='blue')
plt.plot(x,y_pred,color='red')
plt.xlabel('Independent variables')
plt.ylabel('Dependent variables')
plt.title('Linear Regression')
plt.show()