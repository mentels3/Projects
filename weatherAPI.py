
from pandas import DataFrame
import requests
import json

#Gets the data from the API
response_API = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')

exitCode = 0

print(type(response_API.status_code))

#Check for valid response
if (response_API.status_code >= 400):
    exitCode = exitCode + 1
    print("ERROR: API status response is " + str(response_API.status_code))
else:
    print("API STATUS CODE: " + str(response_API.status_code))

#Organize the data into JSON format
data = response_API.text
parse_json = json.loads(data)

#Print the keys of the JSON file, currently in dictionary format
for k in parse_json.keys():
    print(k)

#Turn the JSON files into a dataframe
weatherData = DataFrame.from_dict(parse_json)

#Save the dataframe as a csv file
path = "C:/Users/Rebecca/Desktop/weatherAPI/weatherReports.csv"
weatherData.to_csv(index=False,path_or_buf=path)
