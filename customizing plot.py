import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,5,14,16]

plt.plot(x,y,label='prime numbers')
plt.title("line plot with grid and legend")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.show()