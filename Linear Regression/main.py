import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


df = pd.read_csv('Linear Regression\homeprice.csv')

plt.figure()
plt.xlabel('area(sqr ft)')
plt.ylabel('price(US$)')

plt.scatter(df.area, df.price, color='red', marker='+')


reg = linear_model.LinearRegression()
reg.fit(df[['area']].values, df.price.values)

ans = reg.predict(3300)

print(ans)
plt.show()