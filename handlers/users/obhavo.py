import requests
from aiogram.types import Message

from bs4 import BeautifulSoup as BS
# Tashkent
def harorat(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    max = soup.select('.forecast-day')[0].text
    return max

def min(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    uchkun = soup.select(".weather-row-forecast")[1].select('.forecast-night')[0].text
    return uchkun

def tong(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    tong = soup.select('.forecast')[0].text
    return tong
def kunh(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    kun = soup.select('.col-2 .forecast')[0].text
    return kun

def oqshom(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce,'html.parser')
    oqshom = soup.select('.col-3 .forecast')[0].text
    return oqshom
def kun(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    kun = soup.select(".current-day")[0].text
    return kun

def Viloyat(viloyatt):
    link = f"https://obhavo.uz/{viloyatt}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    viloyat = soup.find("h2").text
    return viloyat

def obhavo(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".current-forecast-desc")[0].text
    return obhavo

def Oy(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    obhavo= soup.select(".col-2")[0].text
    return obhavo

def Namlik(viloyat):
    link = f"https://obhavo.uz/{viloyat}"
    responce = requests.get(link).text
    soup = BS(responce, 'html.parser')
    namlik= soup.select(".col-1")[0].text
    return namlik
