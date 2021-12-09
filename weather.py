#imported required modules
import json

#API Key
api_key = "d36d0dfdf07499efb48dbb4f1217d7bc"

#base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/weather?"

#User inputs city name
city_name = input("Please enter city name: ")

#complete_url variable to store complete url address
complete_url = base_url + "q=" + city_name + "&appid=" + api_key

#get method of requests module
#return response object
response = complete_url

#checking the status code of the request
if response == 200:
    #getting data in json format
    data = response.json()
    #getting the main dict block
    main = data['main']
    #getting temperature
    temperature = main['temp']
    #getting the humidity
    humidity = main['humidity']
    #getting the pressure
    pressure = main['pressure']
    #weather report
    report = data['weather']
    print(f"{city_name: -^30}")
    print(f"Temperature: {temperature}")
    print(f"Humdity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")

else:
    #If there is an error message
    print("Error in the HTTP request")