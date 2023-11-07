import requests

# GET YOUR OWN API KEY FROM https://openweathermap.org/api
# PLEASE GET YOUR OWN API KEY IF YOU WANT TO HAVE YOUR OWN VERSION OF THE CODE.
# - Meowxeth
API_KEY = 'YOUR API KEY'


class CheckWeather():

    def __init__(self, current=0, main=0, url='', city_name=''):
        self.current = current
        self.main = main
        self.city_name = city_name
        self.url = url

    def makeUrl(self):
        self.url = (
            f'https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={API_KEY}&units=metric')

    def callAPI(self):
        # Makes an API call, and puts response in a json file
        r = requests.get(self.url)
        response_dict = r.json()
        if response_dict['cod'] == '404':
            return False
        else:
            #print(response_dict)
            self.current = response_dict['main']
            self.main = response_dict['weather']
            return True

    def showStats(self):
        return self.current['temp'], self.current['humidity'], self.current['feels_like']

#testing the api fetch
#test = CheckWeather(city_name='Tokyo')
# test.makeUrl()
# test.callAPI()
# print(test.showStats())
