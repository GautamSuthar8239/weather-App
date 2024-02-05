from flask import Flask, render_template, request
import requests
from weather import get_Current_weather
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') #"Hello World"

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = "Ahmedabad"
    weather_data = get_Current_weather(city)
    #City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=5080)
    serve(app,host="0.0.0.0",port=5080)