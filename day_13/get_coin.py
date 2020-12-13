from functools import reduce

def solution(data):
    bus_ids = data[1].split(",")
    buses_info = get_buses_info(bus_ids)

    consecutive_buses_found = [buses_info[0]]


    # print(calculate_jump_size(buses_info))

    # print(is_departing(buses_info[0], 7))

    initial_timestamp = buses_info[0]["id"]
    jump_size = calculate_jump_size(consecutive_buses_found)
    timestamp_to_check = initial_timestamp

    while True:
        latest_bus_added = buses_info[(len(consecutive_buses_found)) - 1]
        bus_to_check = buses_info[(len(consecutive_buses_found))]
        bus_to_check_should_depart_at = timestamp_to_check + bus_to_check["t_plus"]
        # print(timestamp_to_check, latest_bus_added["t_plus"])
        latest_bus_added_can_depart_at = timestamp_to_check + latest_bus_added["t_plus"]
        final_bus_departs_at = timestamp_to_check + buses_info[-1]["t_plus"]
        bus_to_check_can_depart = is_departing(bus_to_check, bus_to_check_should_depart_at)
        print(f"""--------------------------
checking where first bus has timestamp: {timestamp_to_check}
last bus added was: {latest_bus_added}
buses found so far (in reverse order):

{consecutive_buses_found}

should check if we can add next bus: {bus_to_check}
does {bus_to_check} depart at {bus_to_check_should_depart_at}? {bus_to_check_can_depart}""")
        

        if bus_to_check_can_depart:
            consecutive_buses_found.append(bus_to_check)
            
            print(f"""
adding bus {bus_to_check}
buses found so far (in reverse order):

{consecutive_buses_found}

current jump size was {jump_size}, increasing to {jump_size * bus_to_check['id']}
-----------""")
            jump_size = calculate_jump_size(consecutive_buses_found)
        
    
            if len(consecutive_buses_found) == len(buses_info):
                print(f"""
found all buses {consecutive_buses_found} where first bus departs at {timestamp_to_check}
and latest bus departs at {final_bus_departs_at}
""")
                break



            continue
        # else:
            # consecutive_buses_found.pop()
            # jump_size = calculate_jump_size(consecutive_buses_found)
        


        timestamp_to_check += jump_size

#     first_bus_departing_at = buses_info[0]["id"]
#     previous_bus_departed_at = first_bus_timestamp

#     start_at = first_bus_timestamp
#     while first_bus_timestamp <= 100:
#         # print(f"all buses {bus_info}")
#         print(f"consecutive buses found so far: {consecutive_buses_found}")
#         if len(consecutive_buses_found) == len(buses_info):
#             print(f"all buses match up at time {first_bus_timestamp}")
#             break

#         current_bus_info = buses_info[len(consecutive_buses_found) - 1]
#         next_bus_info = buses_info[len(consecutive_buses_found)]
#         next_bus_should_depart_at = first_bus_timestamp - (buses_info[0]["t_plus"] - next_bus_info["t_plus"])

#         print(f"""
# current bus: {current_bus_info['id']} next bus: {next_bus_info['id']} first_bus_timestamp {first_bus_timestamp}
# looking if bus >>>>>>>>>>{next_bus_info['id']}<<<<<<<< is departing at >>>>{next_bus_should_depart_at}<<<<<
#         """)
#         # (4*x-2)%3 == 0


#         if next_bus_should_depart_at % next_bus_info["id"] == 0:
#             print(f"""
# --------------> bus {next_bus_info} departs at {next_bus_should_depart_at}
            
#             """)
#             consecutive_buses_found.append(next_bus_info)
#             first_bus_departing_at = first_bus_timestamp
#             previous_bus_departed_at = next_bus_should_depart_at
#             continue

#         print(f"""
# did not find a bus, next search should look at a first bus departing at {start_at}
#         """)
#         start_at += buses_info[0]["id"]
#         consecutive_buses_found.pop()
#         first_bus_timestamp *= first_bus_timestamp

    return "ok"

def calculate_jump_size(buses_found):
    ids = map(lambda bus_found: bus_found["id"], buses_found)
    return reduce(lambda x, y: x * y, ids, 1)
    # return buses_found[0][""]

def get_buses_info(bus_ids):
    bus_info = []

    for i, bus_id in enumerate(bus_ids):
        if bus_id != "x":
            bus_info.append({
                "id": int(bus_id),
                "t_plus": i
            })
    # bus_info.reverse()
    return bus_info
        
def is_departing(bus_info, departure_time):
    # print(bus_info)
    return departure_time % int(bus_info["id"]) == 0

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(solution(data))