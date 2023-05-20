import pandas as pd

df = pd.read_csv('Pandas\\1_intro\\nyc_weather.csv')
print(df)

print(df['Temperature'].max())  # 50

print(df['EST'][df['Events'] == 'Rain'])
# 8      1/9/2016
# 9     1/10/2016
# 15    1/16/2016
# 26    1/27/2016
# Name: EST, dtype: object

df.fillna(0, inplace=True)
print(df['WindSpeedMPH'].mean())    # 6.225806451612903