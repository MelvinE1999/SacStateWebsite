import requests


#declaration of global variables
api_key = ""
home = input("Enter your home address\n")
parking_lot = input("Enter the school location\n")
option = input("Please enter your mode of transportation: \n(Bike, Bus, Light "
               "Rail, Walking, and Driving are the options avaliable.)\n")
#Api url for Google Distance Matrix Api
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"


#input: home, parking_lot, and my Api key
#output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
#This method will calculate time for biking from home to parking_lot.
#Calculated by Google Api.
def bicycling_route():
    r = requests.get(url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=bicycling" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#input: home, parking_lot, and my Api key
#output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
#This method will calculate time to take a bus from home to parking_lot.
#Calculated by Google Api.
def bus_route():
    r = requests.get(url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=transit" + "&transit_mode=bus" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#input: home, parking_lot, and my Api key
#output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
#This method will calculate time to drive from home to parking_lot.
#Calculated by Google Api.
def driving_route():
    r = requests.get(url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=driving" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#input: home, parking_lot, and my Api key
#output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
#This method will calculate time to take the light rail,train, or subway from home to parking_lot.
#Calculated by Google Api.
def rail_route():
    r = requests.get(url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=transit" + "&transit_mode=rail" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#input: home, parking_lot, and my Api key
#output: returns the time in seconds of how long it would take to travel from home to parking_lot in best guess.
#This method will calculate time to walk from home to parking_lot.
#Calculated by Google Api.
def walking_route():
    r = requests.get(url + "origins=" + home + "&destinations=" + parking_lot +
                     "&mode=bicycling" + "&key=" + api_key)
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return time

#declaration of try_again is used to validate the lower while loop.
try_again = True
#This while loop will check to make sure the user inputs a valid route option.
#After confirming a valid route option it will store the travel time into the travel_time variable.
while try_again == True:
    if option.lower() == "bike":
        travel_time = bicycling_route()
        try_again = False
    elif option.lower() == "bus":
        travel_time = bus_route()
        try_again = False
    elif option.lower() == "driving":
        travel_time = driving_route()
        try_again = False
    elif option.lower() == "light rail":
        travel_time = rail_route()
        try_again = False
    elif option.lower() == "walking":
        travel_time = walking_route()
        try_again = False
    else:
        print("Sorry that is an invalid option please try again.")
        option = input("\nOptions again are only Bike, Bus, Light Rail, Walking,"
                       " and Driving.\n")
