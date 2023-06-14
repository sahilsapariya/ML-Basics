import matplotlib.pyplot as plt

plt.figure()

days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

# Axes labels and chart title
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')


plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")

# Legend
# Show legend
plt.legend(loc="best")

# Legend at different location with shadow enabled and fontsize set to large
plt.legend(loc="upper right", shadow=True, fontsize='large')

# Grid
plt.grid()

plt.show()