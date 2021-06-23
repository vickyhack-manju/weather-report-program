import requests
from datetime import datetime
api_key = 'ed2c6d49778334caa0d39973bec1d55c'
location = input("Enter the city name:  ")
fileName = input("Enter the file To be saved for output:") + ".txt"
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
myfile = open(fileName,'w')
print("-------------------------------------------------------------", file = myfile)
print("Weather Stats for - {}  || {}".format(location.upper(), date_time), file = myfile)
print("-------------------------------------------------------------", file = myfile)

print("Current temperature is: {:.2f} deg C".format(temp_city), file = myfile)
print("Current weather desc  :", weather_desc, file = myfile)
print("Current Humidity      :", hmdt, '%', file = myfile)
print("Current wind speed    :", wind_spd, 'kmph', file = myfile)
myfile.close()
