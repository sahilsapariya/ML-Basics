import matplotlib.pyplot as plt
plt.figure()

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(x, y, 'b+--')

# Same effect as 'b+' format string
plt.plot(x,y,color='blue',marker='+',linestyle='')

# MarkerSize
plt.plot(x, y, color="blue", marker="+", linestyle='', markersize=20)

# alpha property to control transparency of line chart
plt.plot(x,y,'g<',alpha=0.5) # alpha can be specified on a scale 0 to 1


plt.show()