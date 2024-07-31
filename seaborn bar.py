x=[1,2,3,4,5]
y=[2,4,5,11,7]
import seaborn as sns
import matplotlib.pyplot as plt
categories=['A','B','C','D','E']
values=[1,2,3,4,5]
sns.barplot(x=categories, y=values)
plt.title("bar  plot with seaborn")
plt.show()
