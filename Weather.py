import pyowm
from Configuration import Configuration

class Weather:
    def __init__(self):
        config = Configuration().weather
        self.owm = pyowm.OWM(config['api-key'])
        self.location = config['zipcode']+','+config['countrycode']
        self.units = config['units']

    def get_temperature(self):
        obs = self.owm.weather_at_place(self.location)
        w = obs.get_weather()
        return w.get_temperature(self.units)['temp']

    def get_weather(self):
        fc = self.owm.daily_forecast(self.location, limit=1)
        f = fc.get_forecast()
        return f.get_weathers()[0]

    def get_high(self):
        return self.get_weather().get_temperature(self.units)['max'] 

    def get_low(self):
        return self.get_weather().get_temperature(self.units)['min'] 

    def get_status(self):
        return self.get_weather().get_detailed_status()

    def get_info(self):
        report = str.format("The current temperature is {} degrees Fahrenheit. The forecast for today is {}, with a high of {}, and a low of {}.", int(self.get_temperature()), self.get_status(), int(self.get_high()), int(self.get_low()))
        return report

