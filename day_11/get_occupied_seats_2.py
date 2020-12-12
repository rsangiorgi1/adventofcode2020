import copy

def get_number_of_occupied_seats(seat_layout):
    current_layout = seat_layout
    while True:
        new_layout = get_next_seat_layout(current_layout)
        if current_layout == get_next_seat_layout(current_layout):
            break
        current_layout = new_layout
    return count_occupied_seats(new_layout)

def get_next_seat_layout(seat_layout):
    change_to_empty = []
    change_to_occupied = []
    for y, row in enumerate(seat_layout):
        for x, seat in enumerate(row):
            current_coordinate = {"x": x, "y": y}
            if seat == "L" and count_adjacent_occupied_seats(seat_layout, current_coordinate) == 0:
                change_to_occupied.append(current_coordinate)
            if seat == "#" and count_adjacent_occupied_seats(seat_layout, current_coordinate) >= 5:
                change_to_empty.append(current_coordinate)
    new_layout = change_layout(seat_layout, change_to_empty, "L")
    new_layout = change_layout(new_layout, change_to_occupied, "#")
    return new_layout

def count_occupied_seats(seat_layout):
    occupied_seats_count = 0
    for row in seat_layout:
        for seat in row:
            if seat == "#":
                occupied_seats_count += 1
    return occupied_seats_count

def get_coordinates_to_check(seat_layout, middle_coordinate):
    step_rules = [
        # upper left
        { "x": -1, "y": -1 },
        # upper middle
        { "x": 0, "y": -1 },
        # upper right
        { "x": 1, "y": -1 },
        # left
        { "x": -1, "y": 0 },
        # right
        { "x": 1, "y": 0 },
        # lower left
        { "x": -1, "y": 1 },
        # lower middle
        { "x": 0, "y": 1 },
        # lower right
        { "x": 1, "y": 1 },
    ]
    return [ get_first_seat_in_line(seat_layout, middle_coordinate, rule) for rule in step_rules ]


def get_first_seat_in_line(seat_layout, middle_coordinate, step_rule):
    next_step = {
            "x": middle_coordinate["x"] + step_rule["x"],
            "y": middle_coordinate["y"] + step_rule["y"]
        }
    current_step = middle_coordinate
    while current_step == middle_coordinate or get_seat_by_coordinate(seat_layout, current_step) == ".":
        next_step = {
            "x": current_step["x"] + step_rule["x"],
            "y": current_step["y"] + step_rule["y"]
        }
        if get_seat_by_coordinate(seat_layout, next_step) in ["#", "L", ""]:
            break
        current_step = next_step
    return next_step


def count_adjacent_occupied_seats(seat_layout, middle_coordinate):
    occupied_seats_count = 0
    coordinates_to_check = get_coordinates_to_check(seat_layout, middle_coordinate)
    for coordinate in coordinates_to_check:
        if get_seat_by_coordinate(seat_layout, coordinate) == "#":
            occupied_seats_count += 1
    return occupied_seats_count


def get_seat_by_coordinate(seat_layout, coordinate):
    x = coordinate["x"]
    y = coordinate["y"]
    # skip if it's the side of seat layout
    if not 0 <= y < len(seat_layout) or not 0 <= x < len(seat_layout[0]):
        return ""
    return seat_layout[coordinate["y"]][coordinate["x"]]

def change_layout(seat_layout, coordinates, symbol):
    new_layout = copy.deepcopy(seat_layout)
    for coordinate in coordinates:
        new_layout[coordinate["y"]][coordinate["x"]] = symbol
    return new_layout

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(list, content.split()))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(get_number_of_occupied_seats(data))