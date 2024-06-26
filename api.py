import requests
import json



url="https://api.weatherapi.com/v1/current.json?key=638ba7c08aa4460794393515231104&q="
url= url + input("dear user plz enter your region")



data=requests.get(url)

data=json.loads(data.content)

print(data["location"]["region"])
print(data["current"]["temp_c"])
