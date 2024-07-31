import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3,4,5]
y=[5,6,12,13,17]
categories=['A','B','C','D','E']
values=[7,5,4,1,5]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("plot 1")
plt.subplot(1,2,2)
plt.bar(categories,values)
plt.title("plot 2")
plt.show()