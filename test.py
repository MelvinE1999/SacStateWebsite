import calcs

distance = 40  # Distance is in miles
biking_time = 4000  # Time is in seconds
walking_time = 10000
car_time = 4500

calcs.calc_car_emissions(distance)
print()
calcs.calc_bus_emissions(distance)
print()
calcs.calc_motorcycle_emissions(distance)
print()
calcs.calc_bicycle_emissions(distance)

calcs.output_vehicle_costs()
