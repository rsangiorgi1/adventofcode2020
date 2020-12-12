import copy

def calculate_final_coordinate(instructions):
    latest_coordinates = { "x": 0, "y": 0 }
    latest_direction = "E"
    for instruction in instructions:
        latest_coordinates, latest_direction = get_new_coordinates(latest_coordinates, latest_direction, instruction)
    
    return calculate_manhattan_value(latest_coordinates)


def calculate_manhattan_value(coordinates):
    return abs(coordinates["y"]) + abs(coordinates["x"])

def get_new_coordinates(current_coordinates, current_direction, instruction):
    new_coordinates = copy.deepcopy(current_coordinates)
    new_direction = copy.deepcopy(current_direction)
    current_x = current_coordinates["x"]
    current_y = current_coordinates["y"]
    instruction_type = instruction[0]
    instruction_value = int(instruction[1:])

    if instruction_type == "E" or instruction_type == "F" and current_direction == "E":
        new_coordinates = { "x": current_x + instruction_value, "y": current_y }
    if instruction_type == "S" or instruction_type == "F" and current_direction == "S":
        new_coordinates = { "x": current_x, "y": current_y - instruction_value }
    if instruction_type == "W" or instruction_type == "F" and current_direction == "W":
        new_coordinates = { "x": current_x - instruction_value, "y": current_y }
    if instruction_type == "N" or instruction_type == "F" and current_direction == "N":
        new_coordinates = { "x": current_x, "y": current_y + instruction_value }

    if instruction_type in [ "R", "L"]:
        new_direction = get_new_direction(current_direction, instruction_type, instruction_value)

    print(f"""currently at {current_coordinates}
ship is moving {current_direction}
instruction says to {instruction_type} -> {instruction_value}
new coordinates are {new_coordinates}
new direction is {new_direction}
    
    """)
    return new_coordinates, new_direction

def get_new_direction(current_direction, spin, degrees):
    if spin == "L":
        degrees = -degrees
    ALL_DIRECTIONS_IN_ORDER = [ "E", "S", "W", "N" ]
    i = ALL_DIRECTIONS_IN_ORDER.index(current_direction)
    new_i = (degrees // 90 + i) % len(ALL_DIRECTIONS_IN_ORDER)
    new_direction = ALL_DIRECTIONS_IN_ORDER[new_i]
    return new_direction

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    # print(content)
    return list(map(str, content.split()))

if __name__ == "__main__":
    data = data_to_list("./data")
    # print(data)
    print(calculate_final_coordinate(data))