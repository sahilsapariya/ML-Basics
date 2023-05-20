import pandas as pd

df = pd.read_csv('Pandas/2_dataframe_basics/weather_data.csv')
print(df)
#         day  temperature  windspeed  event
# 0  1/1/2017           32          6   Rain
# 1  1/2/2017           35          7  Sunny
# 2  1/3/2017           28          2   Snow
# 3  1/4/2017           24          7   Snow
# 4  1/5/2017           32          4   Rain
# 5  1/6/2017           31          2  Sunny

rows, columns = df.shape
print(rows, columns)  # 6 4

print(df.head(1))
#         day  temperature  windspeed event
# 0  1/1/2017           32          6  Rain

print(df.tail(1))
#         day  temperature  windspeed  event
# 5  1/6/2017           31          2  Sunny

print(df[2:5])
#         day  temperature  windspeed event
# 2  1/3/2017           28          2  Snow
# 3  1/4/2017           24          7  Snow
# 4  1/5/2017           32          4  Rain

print(df.columns)
# Index(['day', 'temperature', 'windspeed', 'event'], dtype='object')

print(df.day) 
# or
print(df['day'])
# 0    1/1/2017
# 1    1/2/2017
# 2    1/3/2017
# 3    1/4/2017
# 4    1/5/2017
# 5    1/6/2017
# Name: day, dtype: object

print(type(df['event']))    # <class 'pandas.core.series.Series'>



# Some operations on dataframe

# Find the maximum temperature from table
print(df['temperature'].max())   # 35

# similarly
# min()
# std()   -> Standard deviation
# .describe()   -> Print the statistics on the columns

print(df.describe())
#        temperature  windspeed
# count     6.000000   6.000000
# mean     30.333333   4.666667
# std       3.829708   2.338090
# min      24.000000   2.000000
# 25%      28.750000   2.500000
# 50%      31.500000   5.000000
# 75%      32.000000   6.750000
# max      35.000000   7.000000

print(df[df.temperature >= 32])
#         day  temperature  windspeed  event
# 0  1/1/2017           32          6   Rain
# 1  1/2/2017           35          7  Sunny
# 4  1/5/2017           32          4   Rain

# df[['list of attributes to display']]["condition"]

# Example
print(df[['day', 'temperature']][df.temperature == df['temperature'].max()])
#         day  temperature
# 1  1/2/2017           35

print(df.index)
# RangeIndex(start=0, stop=6, step=1)