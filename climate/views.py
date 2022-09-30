from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def index(request):
    if request.method == 'POST':
        city = request.POST['q']
        units = request.POST['units']
        apiKey = os.environ['API_KEY']
        
        # pull JSON data from API
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': apiKey, 'units': units}
        source = requests.get(url=url, params=params)
        
        # convert JSON data to a dictionary
        dataList = source.json()
        print(dataList)

        # data for variable dataList
        data = {
            'country_code': dataList['sys']['country'],
            'city': dataList['name'],
            'temp': dataList['main']['temp'],
            'description': dataList['weather'][0]['description'],
            'pressure': dataList['main']['pressure'],
            'humidity': dataList['main']['humidity'],
            'icon': dataList['weather'][0]['icon'],
        }
        print(data)
    else:
        data ={}
    return render(request, 'climate/index.html', data)