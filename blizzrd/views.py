from django.shortcuts import render
from dotenv import load_dotenv
import requests
import datetime
import os

# Create your views here.


def configure():
    load_dotenv()


def index(request):
    configure()
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Miami'

    appid = os.getenv('OPEN_WEATHER_API_KEY')
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'imperial'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    city = res['name']
    country = res['sys']['country']

    day = datetime.date.today()

    return render(request, 'blizzrd/index.html', {'description': description, 'icon': icon, 'temp': temp, 'city': city, 'day': day, 'country': country})
