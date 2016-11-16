import pyowm
location = '14623,us'
units = 'fahrenheit'

class Weather:
    def __init__(self):
        self.owm = pyowm.OWM(api)
        self.location = location
        self.units = units

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
        report = str.format("The current temperature is {} degrees Fahrenheit. The forecast for today is {}, with a high of {}, and a low of {}.", self.get_temperature(), self.get_status(), self.get_high(), self.get_low())
        return report

