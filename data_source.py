from stop_view import start_stop_view
import json
from datetime import datetime
import requests


key = "8d8b02694dac481caed6bc9698171fdb"


# for additional_params, see SL Platsuppslag at trafiklab.se.
# https://www.trafiklab.se/api/sl-platsuppslag/dokumentation
def get_stops_matching(*, SearchString, Key, **additional_params):
    url = "https://api.sl.se/api2/typeahead.json"
    params = dict({
        "Key": Key,
        "SearchString": SearchString,
    }, **additional_params)
    response = requests.get(url, params)
    return response.json()


key = "ee24b995666e4dad8cb80dd1f0433822"


# for additional_params, see SL Realtidsinformation 4 at trafiklab.se.
# https://www.trafiklab.se/node/15754/documentation
def get_real_time_departures(*, SiteId, Key, TimeWindow=30, **additional_params):
    url = "https://api.sl.se/api2/realtimedeparturesV4.json"
    params = dict({
        "Key": Key,
        "TimeWindow": TimeWindow,
        "SiteId": SiteId,
    }, **additional_params)
    response = requests.get(url, params)
    departures = response.json()
    # concatenate, turn dates into dates, etc
    return departures


def process_departures_response(response):
    return [
        *response["ResponseData"]["Metros"],
        *response["ResponseData"]["Buses"],
        *response["ResponseData"]["Trains"],
        *response["ResponseData"]["Trams"],
        *response["ResponseData"]["Ships"],
    ]


def get_departures_from(SiteIds):
    departures = []
    for SiteId in SiteIds:
        real_time_departures_response = get_real_time_departures(
                SiteId=SiteId,
                Key="ee24b995666e4dad8cb80dd1f0433822")
        departures += process_departures_response(real_time_departures_response)

    # TODO debug
    with open("departures.json", "w", encoding="utf8") as savefile:
        json.dump(real_time_departures_response, savefile, ensure_ascii=False, indent=4)

    departures.sort(key=lambda x: datetime.fromisoformat(x["ExpectedDateTime"]))
    return departures


def calculate_departures(search_string):
    # Calculate only for specific lines and multiple lines TODO
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


if __name__ == '__main__':
    start_stop_view(get_departures_from)
