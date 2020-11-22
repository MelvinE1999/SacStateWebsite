import requests
from urllib.parse import urlencode

# declaration of global variables
api_key = ""
# Api url for Google Distance Matrix Api
d_Matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
# Api url for Google Geocoding Api. Used to validate address.
geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?"


# input: address_or_postalcode, data_type
# output: returns a distance measured in meters.
# This method send API request to Google Maps in order to find the distance between a user's address, and the Sacramento State campus.
def extract_distance(address, destination, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/directions/{data_type}"
    params = {"origin" : address,
              "destination" : destination,
              "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    return (r.json()["routes"][0]["legs"][0]["distance"]["value"])

# input: home, parking_lot, and my Api key
# output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
# This method will calculate time for biking from home to parking_lot.
# Calculated by Google Api.
def bicycling_route(home, destination):
    r = requests.get(d_Matrix_url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=bicycling" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time


# input: home, parking_lot, and my Api key
# output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
# This method will calculate time to take a bus from home to parking_lot.
# Calculated by Google Api.
def bus_route(home, destination):
    r = requests.get(d_Matrix_url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=transit" + "&transit_mode=bus" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#input: The only input is an address from the user.
#output: This function will return a valid address to be used for calculations.
#All this method does is check that there is somewhere in the US with the provided address.
#Has a preference for the area from Placerville,CA to San Fransisco,CA.
def check_address(home, destination):
    home_check = input("Enter your home address\n")
    r = requests.get(geocode_url + "address=" + home_check + "&bound= 37.7749,122.4194|"
                             "38.7296,120.17985&components=country:US&key=" + api_key)
    if r.json()["status"] != "OK":
        print("Please try again. I couldn't find that address.")
        home_check = check_address()
    return home_check

# input: home, parking_lot, and my Api key
# output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
# This method will calculate time to drive from home to parking_lot.
# Calculated by Google Api.
def driving_route(home, destination):
    r = requests.get(d_Matrix_url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=driving" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time


# input: home, parking_lot, and my Api key
# output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
# This method will calculate time to take the light rail,train, or subway from home to parking_lot.
# Calculated by Google Api.
def rail_route(home, destination):
    r = requests.get(d_Matrix_url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=transit" + "&transit_mode=rail" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time


# input: home, parking_lot, and my Api key
# output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
# This method will calculate time to walk from home to parking_lot.
# Calculated by Google Api.
def walking_route(home, destination):
    r = requests.get(d_Matrix_url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=bicycling" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

def get_travel_time_and_distance():
    home = check_address()
    parking_lot = input("Enter the Parking lot you are going to:\n")
    option = input("Please enter your mode of transportation: \n(Bike, Bus, Light "
                "Rail, Walking, and Driving are the options available.)\n")
    distance = extract_distance(home, parking_lot)
    # declaration of try_again is used to validate the lower while loop.
    try_again = True
    # This while loop will check to make sure the user inputs a valid route option.
    # After confirming a valid route option it will store the travel time into the travel_time variable.
    while try_again:
        if option.lower() == "bike":
            travel_time = bicycling_route(home, parking_lot)
            try_again = False
        elif option.lower() == "bus":
            travel_time = bus_route(home, parking_lot)
            try_again = False
        elif option.lower() == "driving":
            travel_time = driving_route(home, parking_lot)
            try_again = False
        elif option.lower() == "light rail":
            travel_time = rail_route(home, parking_lot)
            try_again = False
        elif option.lower() == "walking":
            travel_time = walking_route(home, parking_lot)
            try_again = False
        else:
            print("\nSorry that is an invalid option please try again.")
            option = input("Options again are only Bike, Bus, Light Rail, Walking,"
                        " and Driving.\n")

    return distance, travel_time, option
