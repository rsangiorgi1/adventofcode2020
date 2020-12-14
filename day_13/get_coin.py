from functools import reduce

def solution(bus_data):
    bus_ids = bus_data[1].split(",")
    buses_info = [ { "id": int(bus_id), "t_plus": i }
        for i, bus_id in enumerate(bus_ids) if bus_id != "x" ]
    consecutive_buses_found = [buses_info[0]]
    first_bus_departure_time = buses_info[0]["id"]
    jump_size = calculate_jump_size(consecutive_buses_found)

    while True:
        bus_to_check = buses_info[(len(consecutive_buses_found))]
        bus_to_check_should_depart_at = first_bus_departure_time + bus_to_check["t_plus"]
        bus_to_check_can_depart = bus_to_check_should_depart_at % bus_to_check["id"] == 0
        print(f"""--------------------------
Checking where first bus departs at {first_bus_departure_time}...
Found [{len(consecutive_buses_found)}/{len(buses_info)}] buses so far, where last bus found was: {buses_info[(len(consecutive_buses_found)) - 1]['id']}
Does next bus {bus_to_check['id']} depart at {bus_to_check_should_depart_at}? {bus_to_check_can_depart}""")

        # Did we find a new consecutive bus?
        if bus_to_check_can_depart:
            consecutive_buses_found.append(bus_to_check)
            print(f"""Adding bus {bus_to_check['id']}
Found [{len(consecutive_buses_found)}/{len(buses_info)}] buses so far""")

            # Was it the last consecutive bus that we needed to find?
            if len(consecutive_buses_found) == len(buses_info):
                print(f"Found all consecutive buses! They depart at {first_bus_departure_time} to {first_bus_departure_time + buses_info[-1]['t_plus']}")
                return first_bus_departure_time
            print(f"Current jump size: {jump_size}, increasing to {calculate_jump_size(consecutive_buses_found)}")
            jump_size = calculate_jump_size(consecutive_buses_found)
            # Look for the same timestamp again if a next bus is immediately found as well
            continue
        print(f"Jumping {jump_size} ahead to check again")
        first_bus_departure_time += jump_size

def calculate_jump_size(buses_found):
    return reduce(lambda x, y: x * y, map(lambda bus_found: bus_found["id"], buses_found), 1)

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(solution(data))