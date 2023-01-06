from django.shortcuts import render, redirect
from django.contrib import messages
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
    if r:
        print(f"==> SUCCESS!: Here's the weather information for {city}. <==")
    elif city == '':
        messages.info(
            request, f'Please enter a city or country.')
        print(
            f'!!==> ERROR: User submitted an empty field. <==!!')
        return redirect('/')
    else:
        messages.info(
            request, f"'{city}' does not exist! Please check your spelling and try searching for a different city or country.")
        print(
            f"!!==> ERROR: User entered '{city}'. This value does not exist. <==!!")
        return redirect('/')
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    city = res['name']
    country = res['sys']['country']

    day = datetime.date.today()

    return render(request, 'blizzrd/index.html', {'description': description, 'icon': icon, 'temp': temp, 'city': city, 'day': day, 'country': country})
