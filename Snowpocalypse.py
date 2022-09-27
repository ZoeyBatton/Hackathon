from bs4 import BeautifulSoup
from requests import get 
url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"


response = get(url)
