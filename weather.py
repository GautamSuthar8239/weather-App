from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_Current_weather(city="Ahmedabad"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\n Please Enter a city name: ")
    #checks for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "Ahmedabad"
   
    weather_data = get_Current_weather(city)
    print("\n")
    pprint(weather_data)