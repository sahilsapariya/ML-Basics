import matplotlib.pyplot as plt

plt.figure()

# Draw pie chart to track down home expenses
exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.pie(exp_vals,labels=exp_labels)


# Draw pie chart as perfect circle
plt.pie(exp_vals,labels=exp_labels, shadow=True)
plt.axis("equal")


# Show percentages for every pie. Specify radius to increase chart size
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5)


# Explode
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2])

# counterclock and angle properties
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2],counterclock=True, startangle=45)



plt.show()



