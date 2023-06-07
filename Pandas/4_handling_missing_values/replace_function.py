import pandas as pd
import numpy as np


df = pd.read_csv("Pandas\\4_handling_missing_values\\weatherData.csv")


# Replacing single value
new_df = df.replace(-99999, value=np.NaN)

# Replacing list with single value
new_df = df.replace(to_replace=[-99999,-88888], value=0)


# Replacing per column
new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)


# Replacing by using mapping
new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })


# Regex

# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True) 


# Replacing list with another list
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])

