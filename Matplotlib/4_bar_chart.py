import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# Simple bar chart showing revenues of major US tech companies
company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]

xpos = np.arange(len(company))

plt.bar(xpos, revenue, label="Revenue")

plt.xticks(xpos, company)
plt.ylabel("Revenue(Bln)")
plt.title("US Technology Stocks")

plt.legend()


# Multiple Bars showing revenue and profit of major US tech companies
profit = [40, 2, 34,12]
barwidth = 0.4

plt.bar(xpos - barwidth/2, revenue, width=barwidth, label="Revenue")
plt.bar(xpos + barwidth/2, profit, width=barwidth, label="Profit")

plt.xticks(xpos, company)
plt.ylabel("Revenue(Bln)")
plt.title("US Technology Stocks")

plt.legend()


# Horizontal bar chart using barh function
plt.barh(xpos, revenue, label="Revenue")

plt.yticks(xpos, company)
plt.xlabel("Revenue(Bln)")
plt.title("US Technology Stocks")

plt.show()

