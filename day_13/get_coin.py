def solution(data):
    bus_ids = data[1].split(",")
    bus_info = get_bus_info(bus_ids)

    departure_time = 0
    bus_ids = list(map(lambda bus: bus["id"], bus_info))
    consecutive_buses = [bus_info[0]]
    print(bus_ids)
    print(bus_info)

    count = 0
    # while departure_time < 10000:
        # print(f"look for bus {bus_to_find}")
        # if is_departing(bus_to_find, departure_time):
        #     print("ok")
        # departure_time += bus_info[0]["t_plus"]

    while count <= 5:
        # current_bus_info = bus_info[len(consecutive_buses)]
        # previous_bus_info = bus_info[len(consecutive_buses) + 1]
        current_bus_info = bus_info[0]
        previous_bus_info = bus_info[1]
        difference_with_previous_bus = bus_info[0]["t_plus"] - bus_info[1]["t_plus"]
        print(f"""
    trying to find bus {previous_bus_info}
    attempt {count}, timestamp {count * bus_info[0]["id"]}
    consecutive buses found {consecutive_buses}
    difference with previous bus: {difference_with_previous_bus}
        """)
        # (4*x-2)%3 == 0
        if looksgood(current_bus_info, previous_bus_info, count):

            print(f"buses {current_bus_info['id']} and {previous_bus_info['id']} follow the rule at time {count * bus_ids[0]}")
            if not previous_bus_info in consecutive_buses:
                consecutive_buses.append(previous_bus_info)
        # else:
        #     departure_time 
        count += 1

    return "ok"

def looksgood(current_bus_info, previous_bus_info, attempt):
    difference_with_previous_bus = current_bus_info["t_plus"] - previous_bus_info["t_plus"]
    return (current_bus_info["id"]*attempt - difference_with_previous_bus) % previous_bus_info["id"] == 0

def get_bus_info(bus_ids):
    bus_info = []

    for i, bus_id in enumerate(bus_ids):
        if bus_id != "x":
            bus_info.append({
                "id": int(bus_id),
                "t_plus": i
            })
    bus_info.reverse()
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