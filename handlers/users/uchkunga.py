import requests
from bs4 import BeautifulSoup as BS

import requests
from bs4 import BeautifulSoup as BS

# Bugun ----------------------------------------------------------------------
def bugun(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun1 = soup.find('td').find('strong').text
    # uchkun = soup.select(".weather-row-forecast")[1].text
    return uchkun1
def bugun2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun1 = soup.find('td').find('div').text
    return uchkun1
def Max(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select(".weather-row-forecast")[0].select('.forecast-day')[0].text
    return uchkun

def Min(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select(".weather-row-forecast")[0].select('.forecast-night')[0].text
    return uchkun

def bulut(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".current-forecast-desc")[0].text
    return obhavo
def yongin(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select("tr")[1].select('.weather-row-pop')[0].text
    return uchkun

# Ertaga --------------------------------------------------------------------------

def bugu2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun1 = soup.select('.weather-row-day ')[2].find('strong').text
    return uchkun1
def bugun22(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun1 = soup.select('.weather-row-day ')[2].find('div').text
    return uchkun1
def Max2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select(".weather-row-forecast")[1].select('.forecast-day')[0].text
    return uchkun

def Min2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select(".weather-row-forecast")[1].select('.forecast-night')[0].text
    return uchkun

def bulut2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".weather-row-desc")[2].text
    return obhavo
def yongin2(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select("tr")[1].select('.weather-row-pop')[1].text
    return uchkun