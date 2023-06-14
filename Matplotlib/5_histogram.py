import matplotlib.pyplot as plt

plt.figure()

# We have a sample data of blood sugar level of different patients, 
# we will try to plot number of patients by blood range and try to 
# figure out how many patients are normal, pre-diabetic and diabetic

blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
plt.hist(blood_sugar, rwidth=0.8) # by default number of bins is set to 10


# bins parameter
plt.hist(blood_sugar, rwidth=0.5, bins=4)

# Histogram showing normal, pre-diabetic and diabetic patients distribution
# 80-100: Normal
# 100-125: Pre-diabetic
# 80-100: Diabetic

plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, color='g')


# Mutiple data samples in a histogram
plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women], bins=[80,100,125,150], rwidth=0.95, color=['green','orange'],label=['men','women'])
plt.legend()


# histtype = step
plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,histtype='step')


# horizontal orientation
plt.xlabel("Number Of Patients")
plt.ylabel("Sugar Level")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, orientation='horizontal')


plt.show()
