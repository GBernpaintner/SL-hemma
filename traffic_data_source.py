import json
from datetime import datetime
import requests


key = "8d8b02694dac481caed6bc9698171fdb"


# for additional_params, see SL Platsuppslag at trafiklab.se.
# https://www.trafiklab.se/api/sl-platsuppslag/dokumentation
def request_stops_matching(*, SearchString, Key, **additional_params):
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
def request_real_time_departures(*, SiteId, Key, TimeWindow=30, **additional_params):
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


def process_departures(response):
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
        real_time_departures = request_real_time_departures(
                SiteId=SiteId,
                Key="ee24b995666e4dad8cb80dd1f0433822")
        departures += process_departures(real_time_departures)

    with open("departures.json", "w", encoding="utf8") as savefile:
        json.dump(departures, savefile, ensure_ascii=False, indent=4)

    departures.sort(key=lambda x: datetime.fromisoformat(x["ExpectedDateTime"]))
    return departures

