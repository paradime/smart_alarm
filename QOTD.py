import requests

class QOTD:
    def get_info(self):
        quote = "Your quote of the day is."
        response = requests.get('http://quotes.rest/qod')
        quote += response.json()['contents']['quotes'][0]['quote']
        return quote
