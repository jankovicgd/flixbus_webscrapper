import requests
from bs4 import BeautifulSoup
import json

def getFlixCode(city):
    with open('flixbus.json') as f:
        data = json.load(f)

    for element in data:
        if element['city'] == city:
            return str(element['id'])

departureCity = 'Vienna'
arrivalCity = 'Bratislava'
date = '05.09.2018'

URL = 'https://shop.flixbus.at/search?departureCity=' + getFlixCode(departureCity) + \
    '&arrivalCity=' + getFlixCode(arrivalCity) + '&route=' + departureCity + '-' + arrivalCity + '&rideDate=' + \
    date + \
    '&adult=1&_locale=at&'

site_req = requests.get(URL)

soup = BeautifulSoup(site_req.text, 'html.parser')

classNum = soup.select('.num')

list_of_prices = []
for element in classNum:
    try:
        list_of_prices.append(float(element.string[:-2]))
    except Exception as e:
        pass

sum_prices = 0
for price in list_of_prices:
    sum_prices += price

print('Average price for ' + date + ' is ' + str(round(sum_prices / len(list_of_prices), 2)))
