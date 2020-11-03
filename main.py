Start = "621 Capitol Mall, Sacramento, CA 95814"
End = "6000 J St, Sacramento, CA 95819"


distance = 4500
biking_time = 4000
walking_time = 1000
car_time = 3600
bus_time = 10500

def Car_cost(distance):
    print(f"The monitary cost for car transport is $" + str((distance/25) * 4.3)
          + " in gas per trip and an average of $3.25 in maintenance\n")

def Bus_cost():
    print("Daily bus fare costs $7, yearly bus fare costs $100, and a UTAPS student buspass costs $40\n")

def Walking_cost():
    print("Walking is free!\n")

def carTime(car_time):
    if car_time/60 >= 60:
        time = (((car_time/60)/60))
        time = (str(int(time)) + " hour(s) and " + str(int(((time-int(time)) * 60))) + " minutes\n")
    else:
        time = car_time/60
        time = (str(int(time)) + " minutes\n")
    return time

def CO2Cost_car(distance):
    return(8887/(distance/25))

def CO2Cost_bus(distance):
    return(10180/(distance/25))


Car_cost(distance)
Bus_cost()
Walking_cost()

print("Driving will take " + carTime(car_time))
print("The buss will take " + carTime(bus_time))
print("Walking will take " + carTime(walking_time))
print("Biking will take " + carTime(biking_time))

print("A car will produce " + str(int(CO2Cost_car(distance))) + " grams of CO2 per gallon of gasoline\n")
print("A bus will produce " + str(int(CO2Cost_bus(distance))) + " grams of CO2 per gallon of gasoline\n")

