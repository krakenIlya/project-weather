import requests
from typing import NamedTuple
from datetime import datetime


class WeahterData(NamedTuple):
    description: str
    temp: float  # - 273,15
    wind_speed: float  # * 3.6
    humidity: float  # влажность в процентах
    date: str = "01.01.2001"


class CurrentWeather:  # класс для получения данных о текущей погоде
    def _GetCurrentWeather(self, city: str) -> dict:
        try:
            result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?&appid=e5a82cc25aab76a4a063eaa840c55fbd&q={city}&lang=ru")
            if result.status_code == 200:
                return result.json()
            else:
                raise ValueError("Введенного города нет")
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Нет подключения к интернету")


class CurrentWeatherParser:  # класс для парсинга полученных данных о текущей погоде
    def GetCurrentWeather(self, city: str, WeatherClass) -> WeahterData:
        dict_data = WeatherClass()._GetCurrentWeather(city)
        print(dict_data)
        return WeahterData(
            description=dict_data['weather'][0]['description'],
            temp=round(dict_data['main']['temp'] - 273.15, 1),
            wind_speed=round(dict_data['wind']['speed'] * 3.6, 1),
            humidity=dict_data['main']['humidity'])



class ForecastWeather:  # класс для получения данных о текущей погоде
    def _GetForecastWeather(self, city: str) -> dict:
        try:
            result = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?appid=e5a82cc25aab76a4a063eaa840c55fbd&q={city}&lang=ru")
            if result.status_code == 200:
                return result.json()
            else:
                raise ValueError("Введенного города нет")
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Нет подключения к интернету")


class ForecastWeatherParser:  # класс для парсинга полученных данных о текущей погоде
    def GetForecastWeather(self, city: str, WeatherClass) -> tuple:
        dict_data = WeatherClass()._GetForecastWeather(city)
        current_datetime = str(datetime.now()).split()[0]
        weather_list = [day for day in dict_data['list'] if day['dt_txt'].split()[0] != current_datetime]
        weather_list = [day for day in weather_list if day['dt_txt'].split()[1] == "15:00:00"] 
        print(weather_list)
        return (WeahterData(
            description=dict_data['weather'][0]['description'],
            temp=round(dict_data['main']['temp'] - 273.15, 1),
            wind_speed=round(dict_data['wind']['speed'] * 3.6, 1),
            humidity=dict_data['main']['humidity'],
            date = dict_data['dt_txt'].split()[0]) for dict_data in weather_list)

