from importlib.resources import contents
from bs4 import BeautifulSoup
from requests import get 
import os 
import smtplib

EMAIL_ADRESS = os.environ,get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo

    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this saturday?'

    msg = f'subject: {subject}\n\n{body}'

smtp.sendmail(EMAIL_ADRESS, 'Hoodiescool@icloud.com', msg)
os.system('cls')

url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"

response = get(url)


soup = BeautifulSoup(response.text, 'html.parser')

day = soup.find_all('h3', 'forecast-panel-title')
weather = soup.find_all('p', 'forecast-panel-label')



new_list = [[day[0].text, weather[0].text], [day[1].text, weather[1].text], [day[2].text, weather[2].text], [day[3].text, weather[3].text]]

print(new_list)
for item in new_list:
    if "Partly Sunny" in item:
        print("Yes")

        
    else:
     print("No")


    




    

            
        

    


