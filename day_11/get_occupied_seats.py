import copy

def get_number_of_occupied_seats(seat_layout):
    current_layout = seat_layout
    while True:
        new_layout = get_next_seat_layout(current_layout)
        if current_layout == get_next_seat_layout(current_layout):
            print("no new changes found!")
            break
        current_layout = new_layout
    return count_all_occupied_seats(new_layout)

def get_next_seat_layout(seat_layout):
    change_to_empty = []
    change_to_occupied = []
    for y, row in enumerate(seat_layout):
        for x, column in enumerate(row):
            current_coordinate = {"x": x, "y": y}
            if column == "L" and count_adjacent_occupied_seats(seat_layout, current_coordinate) == 0:
                change_to_occupied.append(current_coordinate)
            if column == "#" and count_adjacent_occupied_seats(seat_layout, current_coordinate) >= 4:
                change_to_empty.append(current_coordinate)
    new_layout = change_layout(seat_layout, change_to_empty, "L")
    new_layout = change_layout(new_layout, change_to_occupied, "#")
    return new_layout

def count_all_occupied_seats(seat_layout):
    occupied_seats_count = 0
    for row in seat_layout:
        for column in row:
            if column == "#":
                occupied_seats_count += 1
    return occupied_seats_count

def count_adjacent_occupied_seats(seat_layout, middle_coordinate):
    occupied_seats_count = 0

    x = middle_coordinate["x"]
    y = middle_coordinate["y"]
    coordinates_to_check = [
        # upper left
        { "x": x - 1, "y": y - 1 },
        # upper middle
        { "x": x, "y": y - 1 },
        # upper right
        { "x": x + 1, "y": y - 1 },
        # left
        { "x": x - 1, "y": y },
        # right
        { "x": x + 1, "y": y },
        # lower left
        { "x": x - 1, "y": y + 1 },
        # lower middle
        { "x": x, "y": y + 1 },
        # lower right
        { "x": x + 1, "y": y + 1 }
    ]
    for coordinate in coordinates_to_check:
        if occupied_seats_count >= 4:
            break
        if get_seat_by_coordinate(seat_layout, coordinate) == "#":
            occupied_seats_count += 1
    return occupied_seats_count

def get_seat_by_coordinate(seat_layout, coordinate):
    x = coordinate["x"]
    y = coordinate["y"]
    # skip if it's the end of seat layout
    if not 0 <= y < len(seat_layout) or not 0 <= x < len(seat_layout[0]):
        return ""
    return seat_layout[y][x]

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