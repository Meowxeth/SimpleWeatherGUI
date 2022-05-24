import requests

# THIS IS MY OWN API KEY FROM https://openweathermap.org/api
# PLEASE GET YOUR OWN API KEY IF YOU WANT TO HAVE YOUR OWN VERSION OF THE CODE.
# - Ippei
API_KEY = 'a1d9885414880b67aa51b7509784ddc2'


class CheckWeather():

    def __init__(self, current=0, main=0, url='', city_name=''):
        self.current = current
        self.main = main
        self.city_name = city_name
        self.url = url

    def makeUrl(self):
        self.url = (
            f'http://api.openweathermap.org/data/2.5/weather?q={self.city_name}'
            '&units=metric&appid={API_KEY}')

    def callAPI(self):
        # Makes an API call, and puts response in a json file
        r = requests.get(self.url)
        response_dict = r.json()
        if response_dict['cod'] == '404':
            print("City not found.")
            return False
        else:
            print(response_dict)
            self.current = response_dict['main']
            self.main = response_dict['weather']
            return True

    def showStats(self):
        return self.current['temp'], self.current['humidity'], self.current['feels_like']


#test = CheckWeather(city_name='Tokyo')
# test.makeUrl()
# test.callAPI()
# test.define()
