from stop_model import *
from stop_view import start_stop_view
import json
from datetime import datetime


def argers(**kwargs):
    return dict({"a":3, "B":"not wow"}, **kwargs)
#print(argers(A="r", B="wow", Cx=54))


def calculate_departures(search_string):
    stops_response = get_stops_matching(SearchString=search_string, Key="8d8b02694dac481caed6bc9698171fdb", MaxResults=1)
    SiteId = stops_response["ResponseData"][0]["SiteId"]
    real_time_departures_response = get_real_time_departures(SiteId=SiteId, Key="ee24b995666e4dad8cb80dd1f0433822")

    with open("savefile.json", "w", encoding="utf8") as savefile:
        json.dump(real_time_departures_response, savefile, ensure_ascii=False, indent=2)

    departures = [
        *real_time_departures_response["ResponseData"]["Metros"],
        *real_time_departures_response["ResponseData"]["Buses"],
        *real_time_departures_response["ResponseData"]["Trains"],
        *real_time_departures_response["ResponseData"]["Trams"],
        *real_time_departures_response["ResponseData"]["Ships"],
    ]

    with open("departures.json", "w", encoding="utf8") as savefile:
        json.dump(real_time_departures_response, savefile, ensure_ascii=False, indent=2)

    departures.sort(key=lambda x: datetime.fromisoformat(x["ExpectedDateTime"]))
    return departures


start_stop_view(calculate_departures)
