from importlib.resources import contents
from bs4 import BeautifulSoup
from requests import get 
import os 

os.system('cls')

url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"

response = get(url)


soup = BeautifulSoup(response.text, 'html.parser')

day = soup.find_all('h3', 'forecast-panel-title')
weather = soup.find_all('p', 'forecast-panel-label')
# extra = soup.find('h2', '#text')
# print(extra.text)
# def weathers():
#     for item, items in zip (weather, day):
#         new = (item.text, items.text)
#         print(new)
#         if "Mostly Sunny" in item:
#             new_list = ['']
#             new_list.append('')
            
# for item, items in zip (weather, day):
#     print(item.text, items.text)
#     if 


    

            
        

    
# weathers()

