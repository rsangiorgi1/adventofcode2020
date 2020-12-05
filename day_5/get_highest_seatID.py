from functools import reduce

def get_missing_seat_id(boarding_passes):
    seat_ids = sorted(map(get_seat_id, boarding_passes))
    print(seat_ids)
    for i, seat_id in enumerate(seat_ids):
        print(seat_id)
        if not is_consecutive(seat_id, seat_ids[i + 1]):
            print(f"No seat found between seat {seat_id} and seat {seat_ids[i + 1]}")
            return seat_id + 1

def is_consecutive(a, b):
    return a - b == -1

def get_seat_id(boarding_pass):
    row = get_place_info(boarding_pass, "ROW")
    column = get_place_info(boarding_pass, "COLUMN")
    return row * 8 + column

def get_place_info(boarding_pass, mode):
    ticket_info = ""
    possibilities = []
    if mode == "ROW":
        ticket_info = boarding_pass[:-3]
        possibilities = list(range(128))
    elif mode == "COLUMN":
        ticket_info = boarding_pass[7:]
        possibilities = list(range(8))

    for i in range(len(ticket_info)):
        possibilities = get_half_possibilities(ticket_info[i], possibilities)
    return possibilities[0]

def get_half_possibilities(place_indicator, remaining_possibilities):
    if place_indicator in ["R", "B"]:
        return split_range("UPPER", remaining_possibilities)
    if place_indicator in ["L", "F"]:
        return split_range("LOWER", remaining_possibilities)

def split_range(side_indicator, full_range):
    half_range = len(full_range) // 2
    if side_indicator == "LOWER":
        return full_range[:-half_range]
    if side_indicator == "UPPER":
        return full_range[half_range:]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    print(get_missing_seat_id(data_to_list("./data")))
