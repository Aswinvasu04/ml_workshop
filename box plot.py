
import seaborn as sns
import matplotlib.pyplot as plt
data=[1,2,3,4,5,7,6,6,6]
tips=sns.load_dataset('tips')
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("box plot with seaborn")
plt.show()
