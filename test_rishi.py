import calcs_rishi

distance = 40  # Distance is in miles
biking_time = 4000  # Time is in seconds
walking_time = 10000
car_time = 4500

calcs_rishi.calc_car_emissions(distance)
print()
calcs_rishi.calc_bus_emissions(distance)
print()
calcs_rishi.calc_motorcycle_emissions(distance)
print()

calcs_rishi.output_vehicle_costs()
