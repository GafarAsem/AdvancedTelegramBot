import requests


class Weather:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        url = 'http://api.openweathermap.org/data/2.5/weather?lat=LAT&lon=LON&appid=4e3d36f8747c07b49c5dfcd4046d8141'
        url = url.replace('LAT', self.lat)
        url = url.replace('LON', self.lon)
        ###get weather api
        weather = requests.get(url)
        ## Get info from json
        self.nameCity = str(weather.json()['name'])
        self.MainWeather = str(weather.json()['weather'][0]['main'])
        self.tempWeather = str(int(weather.json()['main']['temp'] - 270))
        self.speedWind = str(weather.json()['wind']['speed'])

    # def __init__(self,nameCountry):
    #     self.nameCity=nameCountry
    #     url='http://api.openweathermap.org/data/2.5/weather?q=NAMECOUNTRY&appid=4e3d36f8747c07b49c5dfcd4046d8141'
    #     url=url.replace('NAMECOUNTRY',self.nameCity)
    #     ###get weather api
    #     weather = requests.get(url)
    #     ## Get info from json
    #     self.nameCity = str(weather.json()['name'])
    #     self.MainWeather = str(weather.json()['weather'][0]['main'])
    #     self.tempWeather = str(int(weather.json()['main']['temp'] - 270))
    #     self.speedWind = str(weather.json()['wind']['speed'])
