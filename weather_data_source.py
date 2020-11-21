import json
import requests


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


def get_forecast():
    forecast = request_real_time_forecast(site='Stockholm', key='06b0d00b98214b5dae880412202111')
    with open("forecast.json", "w", encoding="utf8") as savefile:
        json.dump(forecast, savefile, ensure_ascii=False, indent=4)
    return None

