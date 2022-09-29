from django.shortcuts import redirect, render
# import requests
import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
# def index(request):
    
#     num = 2 + 3
#     # query = request.body.q
#     # units = req.body.units
#     city = 'Paris'
#     units = 'imperial'
#     apiKey = os.environ['API_KEY']
#     # url = 'https://api.openweathermap.org/data/2.5/weather?q=${query}&units=${units}&appid=${apiKey}'
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'appid': apiKey, 'units': units}

#     r = requests.get(url=url, params=params)
#     res = r.json()
#     description = res['weather'][0]['description']
#     icon = res['weather'][0]['icon']
#     temp = res['main']['temp']

#     return render(request, 'climate/index.html', {
#         'description': description,
#         'icon': icon,
#         'temp': temp,
#     })

def index(request):
    if request.method == 'POST':
        city = request.POST['q']
        units = request.POST['units']
        # city = 'Paris'
        # units = 'imperial'
        apiKey = os.environ['API_KEY']
        
        # source contain JSON data from API
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': apiKey, 'units': units}
        source = request.get(url=url, params=params)
        
        # source = urllib.request.urlopen(
        #     'http://api.openweathermap.org/data/2.5/weather?q=' 
        #             + city + '&units=' + units + '&appid=' + apiKey).read()
  
        # converting JSON data to a dictionary
        # list_of_data = json.loads(source)
        list_of_data = source.json()

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data ={}
    return render(request, "climate/index.html", data)   