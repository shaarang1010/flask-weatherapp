import requests
import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
from flask_api import status

app = Flask(__name__)
app.config['DEBUG'] = True
# load creds 
creds = load_dotenv(".env")


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={os.getenv('API_KEY')}"
    r = requests.get(url).json()
    return r

@app.route('/', methods=['GET', 'POST'])
def index_get():
    cities = ['Melbourne', 'Sydney', 'Brisbane', 'Darwin', 'Perth', 'Hobart', 'Canberra', 'Newcastle']

    weather_data = []

    for city in cities:
        r = get_weather_data(city)
        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'temperature_min': r['main']['temp_min'],
            'temperature_max': r['main']['temp_max'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data),  status.HTTP_200_OK

if __name__=="__main__":
    app.run(threaded=True, port=5000)
