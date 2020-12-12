import copy

def calculate_final_coordinate(instructions):
    latest_coordinates = { "x": 0, "y": 0 }
    latest_waypoint = { "x": 10, "y": 1 }
    for instruction in instructions:
        latest_coordinates, latest_waypoint = get_new_coordinates(latest_coordinates, instruction, latest_waypoint)
    return calculate_manhattan_value(latest_coordinates)


def calculate_manhattan_value(coordinates):
    return abs(coordinates["y"]) + abs(coordinates["x"])

def get_new_coordinates(current_coordinates, instruction, current_waypoint):
    new_coordinates = copy.deepcopy(current_coordinates)
    new_waypoint = copy.deepcopy(current_waypoint)
    current_x = current_coordinates["x"]
    current_y = current_coordinates["y"]
    waypoint_x = current_waypoint["x"]
    waypoint_y = current_waypoint["y"]
    instruction_type = instruction[0]
    instruction_value = int(instruction[1:])

    # move waypoint
    if instruction_type == "E":
        new_waypoint = { "x": waypoint_x + instruction_value, "y": waypoint_y }
    if instruction_type == "S":
        new_waypoint = { "x": waypoint_x, "y": waypoint_y - instruction_value }
    if instruction_type == "W":
        new_waypoint = { "x": waypoint_x - instruction_value, "y": waypoint_y }
    if instruction_type == "N":
        new_waypoint = { "x": waypoint_x, "y": waypoint_y + instruction_value }
    if instruction_type in [ "R", "L"]:
        new_waypoint = get_new_waypoint(current_waypoint, instruction_type, instruction_value)

    # move ship
    if instruction_type == "F":
        new_coordinates = { "x": current_x + instruction_value * waypoint_x, "y": current_y + instruction_value * waypoint_y }

#     print(f"""
# currently at c: {current_coordinates}, w: {current_waypoint}
# instruction:    {instruction_type} -> {instruction_value}
# new at c:       {new_coordinates}, w: {new_waypoint}
# """)
    return new_coordinates, new_waypoint

def get_new_waypoint(current_waypoint, spin, degrees):
    # first calculate number of counterclockwise rotations
    if spin == "R":
        degrees = -degrees
    counterclockwise_quarter_rotations = degrees // 90 % 4
    # then, per counterclockwise rotation, switch x and y and make y negative
    new_waypoint = copy.deepcopy(current_waypoint)
    for _ in range(counterclockwise_quarter_rotations):
        new_waypoint = rotate_counterclockwise_quarter(new_waypoint)
    return new_waypoint

def rotate_counterclockwise_quarter(coordinates):
    return { "x": -coordinates["y"], "y": coordinates["x"] }

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(calculate_final_coordinate(data))