import matplotlib.pyplot as plt

plt.figure()

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]

plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels,radius=2, autopct='%0.1f%%', explode=[0,0.1,0.1,0,0])
plt.savefig("piechart.jpg", bbox_inches="tight", pad_inches=1, transparent=True)


# You can also save in pdf format and to a different location on your computer 
# by specifying absolute path

plt.pie(exp_vals,labels=exp_labels,radius=2, autopct='%0.1f%%', explode=[0,0.1,0.1,0,0])
plt.savefig("piechart.pdf", bbox_inches="tight", pad_inches=10, transparent=True)


plt.show()