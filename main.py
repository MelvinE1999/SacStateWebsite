import calc
import commuteinfo

def main():
    distance, travel_time, commute_option = commuteinfo.get_travel_time_and_distance()

    if commute_option.lower() == "driving":
            calc.output_vehicle_travel_time(travel_time)
            calc.calc_car_emissions(distance)
            calc.output_vehicle_costs()
    elif commute_option.lower() == "bus":
            calc.output_bus_travel_time(travel_time)
            calc.calc_bus_emissions(distance)
    elif commute_option.lower() == "bike":
            calc.output_biking_travel_time(travel_time)

main()

