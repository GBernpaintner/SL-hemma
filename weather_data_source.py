import json
import requests


class WeatherInfo:
    with open('resources/weather_conditions.json', encoding='utf8') as f:
        conditions = json.load(f)


key = '06b0d00b98214b5dae880412202111'


# for additional_params, see Weather API.
# https://www.weatherapi.com/
def request_real_time_forecast(*, site, key, days=3, **additional_params):
    url = 'https://api.weatherapi.com/v1/forecast.json'
    params = dict({
        'key': key,
        'q': site,
        'days': days
    }, **additional_params)
    response = requests.get(url, params)
    forecast = response.json()
    return forecast


def process_forecast(data):
    # Unnests the nested hour lists in forecastday
    return [hour for fcd in data['forecast']['forecastday'] for hour in fcd['hour']]


def get_forecast():
    forecast = request_real_time_forecast(
            site='59.29687,18.051356',
            lang='sv',
            key='06b0d00b98214b5dae880412202111')
    with open("forecast.json", "w", encoding="utf8") as savefile:
        json.dump(forecast, savefile, ensure_ascii=False, indent=4)
    return process_forecast(forecast)

