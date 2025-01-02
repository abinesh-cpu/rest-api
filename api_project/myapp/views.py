from django.shortcuts import render
import requests
import math
import datetime

# Create your views here.
def index(request):
    city_name='kochi'
    if request.method=='POST':
        city_name=request.POST['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=360e4bc3865e745ec844bd7ec054ca11'
    data = requests.get(url)
    weather_data = data.json()
    dt_object = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    dt_object1 = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])

    data = {
            'date': dt_object.strftime('%d-%m-%y'),
            'city': city_name,
            'weather_description': weather_data['weather'][0]['description'],
            'temperature_kelvin': weather_data['main']['temp'],
            'temperature_celsius': math.floor(weather_data['main']['temp'] - 273.15),  # Convert to Celsius
            'humidity': weather_data['main']['humidity'],
            'temp_min_celsius': math.floor(weather_data['main']['temp_min'] - 273.15),  # Convert to Celsius
            'temp_max_celsius': math.floor(weather_data['main']['temp_max'] - 273.15),  # Convert to Celsius
            'sunrise': dt_object.strftime('%H:%M:%S'),
            'sunset': dt_object1.strftime('%H:%M:%S'),
            'visibility': math.floor(weather_data['visibility'] / 1000),  # Convert meters to kilometers
            'cloud': weather_data['clouds']['all'],
            'wind': weather_data['wind']['speed'],
            'pressure': math.floor((weather_data['main']['pressure'] / 1013.25) * 100),  # Convert to hPa
            'feel_temp': math.floor(weather_data['main']['feels_like'] - 273.15),  # Convert to Celsius
            'sea_level': weather_data['main'].get('sea_level'),  # Check for missing data
            'grnd_level': weather_data['main'].get('grnd_level'),  # Check for missing data
        }    

    return render(request, 'index.html', {'data': data})
def contact(request):
    return render(request,'contact.html')
def livecameras(request):
    return render(request,'livecameras.html')
def news(request):
    return render(request,'news.html')
def photos(request):
    return render(request,'photos.html')
def single(request):
    return render(request,'single.html')