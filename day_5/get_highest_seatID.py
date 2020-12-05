from functools import reduce

def get_highest_seat_id(boarding_passes):
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)
        seat_ids.append(seat_id)
        print(f"boarding pass: {boarding_pass}, seat id: {seat_id}")
    return max(seat_ids)


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
    print(get_highest_seat_id(data_to_list("./data")))
