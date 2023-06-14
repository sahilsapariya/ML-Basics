import matplotlib.pyplot as plt

plt.figure()

x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]

plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(x, y, color="green", linewidth=2, linestyle='dotted')
plt.show()