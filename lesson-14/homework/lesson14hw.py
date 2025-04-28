import json
import requests


with open('lesson14/students.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
    for info in data['students']:
        print(info)

# ---------------------------------------------------------------------


API_KEY = 'ab14e6e426e81cb76e331b6374391cfd'
CITY = 'Tashkent'
url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(url)
data = json.loads(response.text)

temperature = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['description']


print(f'{CITY} today: {temperature} degrees, the humidity is {humidity} and the sky is {weather}')


# ---------------------------------------------------------------------


# url = 'http://www.omdbapi.com/?i=tt3896198&apikey=8772bb51'

# response = requests.get(url)
# data = json.loads(response.text)
