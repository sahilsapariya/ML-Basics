import pandas as pd

df = pd.read_csv("Pandas\\4_handling_missing_values\\weather_data.csv", parse_dates=["day"])
df.set_index('day',inplace=True)

# filling all the NaN containing cell values with 0 
new_df = df.fillna(0)

# fill the NaN cell of particular columns
new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'no event'
    })


# it will forward fill the NaN values
new_df = df.fillna(method="ffill")


# it will fill the values by appropriate calculations
new_df = df.interpolate(method="time")


# it will drop the rows which have 2 or more None values 
new_df = df.dropna(thresh=2)


dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)
# 	        temperature	windspeed	event
#
# 2017-01-01	32.0	6.0	        Rain
# 2017-01-02	NaN	    NaN	        NaN
# 2017-01-03	NaN	    NaN	        NaN
# 2017-01-04	NaN	    9.0	        Sunny
# 2017-01-05	28.0	NaN	        Snow
# 2017-01-06	NaN	    7.0	        NaN
# 2017-01-07	32.0	NaN	        Rain
# 2017-01-08	NaN	    NaN	        Sunny
# 2017-01-09	NaN	    NaN	        NaN
# 2017-01-10	34.0	8.0	        Cloudy
# 2017-01-11	40.0	12.0	    Sunny