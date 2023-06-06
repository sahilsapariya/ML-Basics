import pandas as pd

# using csv files 
df = pd.read_csv('Pandas/2_dataframe_basic/weather_data.csv')

# using excel files
df = pd.read_excel('weather_data.xlsx', 'Sheet1')

# using dictionary
weather_data = {
    "day" : ['1/1/2023', '2/1/2023', '3/1/2023'],
    "temperature": [32, 35, 28],
    'windspeed': [6, 2, 7],
    'event': ["Rain", 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)

# using list of tuples
weather_data = [
    ('1/1/2023', 32, 6, 'Rain'),
    ('2/1/2023', 12, 2, 'Sunny'),
    ('3/1/2023', 28, 7, 'Snow')
]
df = pd.DataFrame(weather_data, columns=['day', 'temperature', 'windspeed', 'event'])

# list of dictionaries
weather_data = [
    {'day': '1/1/2023', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/1/2023', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/1/2023', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'}
]
df = pd.DataFrame(weather_data)