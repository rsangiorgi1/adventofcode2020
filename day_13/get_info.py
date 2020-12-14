def solution(bus_info):
    timestamp = int(bus_info[0])
    waiting_since = timestamp
    bus_ids = list(map(int, filter(lambda bus_id: bus_id != "x" , bus_info[1].split(","))))

    while True:
        departing_buses_ids = list(filter(lambda bus_id: timestamp % bus_id == 0, bus_ids))
        if len(departing_buses_ids) != 0:
            return (timestamp - waiting_since) * departing_buses_ids[0]
        timestamp += 1

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(solution(data))