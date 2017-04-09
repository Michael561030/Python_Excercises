import requests
import json
import urllib.response
def convert_kelvin_celsius(kelvin):
    return float(kelvin-273.15)
while True:
   key='0d9641abe40103a75f9528e8520e96f9'
   city=input("Please enter the name city or id city:  ")

   if city.isalpha():
       url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
       response = requests.get(url)
       content = response.content
   
   elif city.isdigit:
       url = "http://api.openweathermap.org/data/2.5/weather?id="+city+"&appid="+key
       response = requests.get(url)
       content = response.content
 
   data = json.loads(content.decode('utf-8'))
   temp=data['main']['temp']
   tempar=round(convert_kelvin_celsius(temp),2)
   print("Current temp: "+ str(tempar)+"° C")
