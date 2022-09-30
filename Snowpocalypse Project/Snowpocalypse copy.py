from importlib.resources import contents
from bs4 import BeautifulSoup
from requests import get 
import os 
from twilio.rest import Client

os.system('cls')

url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"

response = get(url)

account_sid = 'AC10e31a7cfcd37aee8370d2bc09468b25'
account_token = '9f588b3eda127e946a95df97e62ef3da'

soup = BeautifulSoup(response.text, 'html.parser')

day = soup.find_all('h3', 'forecast-panel-title')
weather = soup.find_all('p', 'forecast-panel-label')

client = Client(account_sid, account_token)

new_list = [[day[0].text, weather[0].text], [day[1].text, weather[1].text], [day[2].text, weather[2].text], [day[3].text, weather[3].text]]

print(new_list)
def weathers():
    snow_list = []
    if  new_list[0][1] == "Chance Of Showers":
        print("Yes")
        snow_list.append(new_list[0][0])
    if new_list[1][1] == "Chance Of Showers":
        print("Yes")  
        snow_list.append(new_list[1][0])
    if new_list[2][1] == "Chance Of Showers":
        print("Yes")  
        snow_list.append(new_list[2][0])
    if new_list[3][1] == "Chance Of Showers":
        print("Yes")
        snow_list.append(new_list[3][0])
    
    if len(snow_list) >= 1:
        message = client.messages.create(
        messaging_service_sid = 'MGdb54e56bf0ab026edbd4181ec8f08a0c',
        body = f"It will be raining on {(' and '.join(str(x) for x in snow_list))}",
        to = '+13303014724'
        )
        print(message.sid)
    

        
weathers()







print(new_list)



    

            
        

    


