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
        
        if units == 'imperial':
            unit_flag = 'F'
        else:
            unit_flag = 'C'

        # pull JSON data from API
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': apiKey, 'units': units}
        
        try:  
            source = requests.get(url=url, params=params)
        except requests.exceptions.RequestException:
            print('oops')
        
        if source:
            # convert JSON data to a dictionary
            dataList = source.json()
            #print(dataList)

            data = {
                'country_code': dataList['sys']['country'],
                'city': dataList['name'],
                'temp': round(dataList['main']['temp']), 
                'units': unit_flag,
                'max': round(dataList['main']['temp_max']),
                'min': round(dataList['main']['temp_min']),
                'description': dataList['weather'][0]['description'],
                'pressure': dataList['main']['pressure'],
                'humidity': dataList['main']['humidity'],
                'icon': dataList['weather'][0]['icon'],
                'error': False,
            }
        else:
            data = {
                'error': True
            }
    else:
        data = {}

    #print(data)
    
    return render(request, 'climate/index.html', data)