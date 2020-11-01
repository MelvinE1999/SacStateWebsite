import requests
from urllib.parse import urlencode

start = "3840 Elm St, Sacramento, CA"
destination = "6000 J St, Sacramento, CA"
api_key = ""

def extract_distance(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/directions/{data_type}"
    params = {"origin" : address_or_postalcode,
              "destination" : destination,
              "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    return (r.json()["routes"][0]["legs"][0]["distance"]["value"])

distance = extract_distance(start)
print(str(distance) + "m") #value is in meters
