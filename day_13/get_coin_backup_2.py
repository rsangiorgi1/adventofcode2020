def solution(data):
    bus_ids = data[1].split(",")
    bus_info = get_bus_info(bus_ids)

    bus_ids = list(map(lambda bus: bus["id"], bus_info))
    consecutive_buses_found = [bus_info[0]]

    first_bus_timestamp = bus_info[0]["id"]
    first_bus_departing_at = bus_info[0]["id"]
    previous_bus_departed_at = first_bus_timestamp

    start_at = first_bus_timestamp
    while first_bus_timestamp <= 100:
        # print(f"all buses {bus_info}")
        print(f"consecutive buses found so far: {consecutive_buses_found}")
        if len(consecutive_buses_found) == len(bus_info):
            print(f"all buses match up at time {first_bus_timestamp}")
            break

        current_bus_info = bus_info[len(consecutive_buses_found) - 1]
        next_bus_info = bus_info[len(consecutive_buses_found)]
        next_bus_should_depart_at = first_bus_timestamp - (bus_info[0]["t_plus"] - next_bus_info["t_plus"])

        print(f"""
current bus: {current_bus_info['id']} next bus: {next_bus_info['id']} first_bus_timestamp {first_bus_timestamp}
looking if bus >>>>>>>>>>{next_bus_info['id']}<<<<<<<< is departing at >>>>{next_bus_should_depart_at}<<<<<
        """)
        # (4*x-2)%3 == 0


        if next_bus_should_depart_at % next_bus_info["id"] == 0:
            print(f"""
--------------> bus {next_bus_info} departs at {next_bus_should_depart_at}
            
            """)
            consecutive_buses_found.append(next_bus_info)
            first_bus_departing_at = first_bus_timestamp
            previous_bus_departed_at = next_bus_should_depart_at
            continue

        print(f"""
did not find a bus, next search should look at a first bus departing at {start_at}
        """)
        start_at += bus_info[0]["id"]
        consecutive_buses_found.pop()
        first_bus_timestamp *= first_bus_timestamp

    return "ok"

def get_bus_info(bus_ids):
    bus_info = []

    for i, bus_id in enumerate(bus_ids):
        if bus_id != "x":
            bus_info.append({
                "id": int(bus_id),
                "t_plus": i
            })
    # bus_info.reverse()
    return bus_info
        
def is_departing(bus_id, departure_time):
    print(bus_id)
    return departure_time % int(bus_id) == 0

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(solution(data))