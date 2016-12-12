import requests

# Pull the quote of the day from the quotes rest api
class QOTD:

    # returns the quote of the day
    def get_info(self):
        quote = "Your quote of the day is."
        response = requests.get('http://quotes.rest/qod')
        quote += response.json()['contents']['quotes'][0]['quote'] # dependent on the structure of the response
        return quote
