from importlib.resources import contents
from bs4 import BeautifulSoup
from requests import get 
import os 
os.system('cls')

url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"

response = get(url)


soup = BeautifulSoup(response.text, 'html.parser')


weather = soup.find_all('p', 'forecast-panel-label'), 
day = soup.find_all('h3', 'forecast-panel-title')
for item, items in weather:
    print(item.text)
    if "Snow" in item:
        print("Yes")
    


