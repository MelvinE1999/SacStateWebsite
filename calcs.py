# TODO: problems may occur when trying to access calculations such as emissions, time, costs outside of their
#  respective functions. This will be important when determining the best possible route for a student.
#  This is something I will fix/figure out later.

# These values are based on the ones given in the PowerPoint provided in class.
average_car_mpg = 25
average_bus_mpg = 7
average_motorcycle_mpg = 44


# TODO: Convert time that is above 60 minutes into a format of "__hrs and __minutes" for all time functions
# Outputs the travel time when driving with your own vehicle.
def output_vehicle_travel_time(time):
    time = int(time / 60)  # Converts the time provided by the Google API from seconds to minutes
    print("Travelling to campus by car/motorcycle would take about " + str(time) + " minutes. ")
    print("It's important to note that the time of day could have an impact on traffic conditions.")
    print("We suggest visiting Google Maps and using their feature that allows you to experiment with traffic"
          "\nconditions during different times of the day.")


# Outputs travel time when taking the bus.
def output_bus_travel_time(time):
    time = int(time / 60)
    print("Travelling to campus by a bus would take about " + str(time) + " minutes. ")


# Outputs travel time for riding a bike.
def output_biking_travel_time(time):
    time = int(time / 60)
    print("Travelling to campus by a bike would take about " + str(time) + " minutes. ")


# Calculates a light vehicle's emissions based on the average mpg rating
def calc_car_emissions(dist):
    emissions = int(((8887 / average_car_mpg) * dist) / 454)  # Divide by 454 to convert from grams to pounds
    print("The average carbon footprint of a car, based on the distance of " + str(dist) + " miles is about "
          + str(emissions) + " pounds of CO2.")
    print("This can be mitigated by carpooling with a friend, since that would mean one less vehicle on the road.")


# Calculates a bus's emissions based on the average mpg rating
def calc_bus_emissions(dist):
    emissions = int(((8887 / average_bus_mpg) * dist) / 454)
    print("The average carbon footprint of a bus, based on the distance of " + str(dist) + " miles is about "
          + str(emissions) + " pounds of CO2.")
    print("Although this seems like a large value, it's important to consider that the advantage from traveling by"
          "\nbus is especially beneficial when many people are going by bus, since this reduces the amount of cars on"
          "\nthe road.")


# Calculates a motorcycle's emissions based on the average mpg rating
def calc_motorcycle_emissions(dist):
    emissions = int(((8887 / average_motorcycle_mpg) * dist) / 454)
    print("The average carbon footprint of a motorcycle, based on the distance of " + str(dist) + " miles is about "
          + str(emissions) + " pounds of CO2.")


# Calculates the carbon footprint of bicycling.
def calc_bicycle_emissions(dist):
      emissions = int(26 * dist) / 454
      print("Although it may come as a surprise, bicycling does leave a carbon footprint as well. The CO2 emissions of"
            "\nbicycling depend on your diet. A diet that is reliant on meat will leave a higher carbon footprint"
            "\n(about 16g of CO2 for every km, which is about 26g per mile). Once again, this will vary depending"
            "\non the kinds of foods you eat.")
      print("\nFor your route, your carbon footprint from bicycling is about " + str(emissions) + " pounds of CO2.")


# TODO: Input validation to ensure the number that is entered is not less than 0 or is a non-numerical value.
# Calculates the costs of driving a personal vehicle to campus.
def output_vehicle_costs():
    monthly_vehicle_payment = int(input("Enter your monthly vehicle payment: "))
    monthly_insurance = int(input("Enter your monthly insurance payment: "))
    monthly_gas = int(input("Enter your monthly gas expenditures: "))

    car_parking_permit = 178
    motorcycle_parking_permit = 44

    total = monthly_vehicle_payment + monthly_insurance + monthly_gas

    print("\nThe total amount you pay every month for your vehicle is about $" + str(total) + ".\n")

    print("This does not include several other expenses, such as maintenance fees (oil changes, brakes, "
          "\nmulti-point inspections, etc.) that may be necessary over time or the yearly registration fees.")

    print("\nYou will also need to purchase a parking permit, which currently costs $" + str(car_parking_permit)
          + " for cars and \n$" + str(motorcycle_parking_permit) + " for motorcycles.")

    print("\nYou can mitigate costs by choosing to carpool with a friend and splitting the costs. However, that would"
          "\nrequire you to coordinate your schedule with theirs.")


# Outputs the costs of using Sacramento Regional Transit (SacRT) to commute to campus.
def output_transit_costs():
      print("Traveling by bus or lightrail through Sacramento Regional Transit is already covered through your tuition fees as a"
            "\nSac State student. There are no additional fees. All you have to do is pick up a commuter sleeve from the"
            "\nBursar's Office or the UTAPS Office on campus. Another cost to consider is time, since transit can take almost"
            "\ntwice as long to reach your destination as it would to drive there with your own vehicle. This is because transits"
            "\nfollow set routes and make multiple stops on the way.")


# Outputs the costs of biking to campus.
def output_biking_costs():
      print("The cost of a bicycle can start as low as $100 and can go higher than $1,000. It depends on the type of bicycle,"
            "\nits condition (new, used, etc.), where you buy it from, and additional warranties. It's also important to take"
            "\nmaintenance into account. Maintenance fees will vary based on the kind of bike you ride, how you treat the bike,"
            "\nwhether you get it serviced from a shop or DIY it, and more. However, you do save lots of money that would otherwise"
            "\nbe spent on gas.")
