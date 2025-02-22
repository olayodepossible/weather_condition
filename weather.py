from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="London"):

    request_url = f'{os.getenv("WEATHER_URL")}{os.getenv("API_KEY")}&q={city}&units={os.getenv("WEATHER_UNIT")}'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city = "London"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
