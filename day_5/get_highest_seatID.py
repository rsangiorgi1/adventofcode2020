from functools import reduce

def get_highest_seat_id(boarding_passes):
    for boarding_pass in boarding_passes:
        print(f"boarding pass: {boarding_pass}")
        print(get_row(boarding_pass))
        print(get_column(boarding_pass))

def get_column(boarding_pass):
    column_info = boarding_pass[7:]
    print(column_info)
    possible_columns = list(range(0, 8))
    for i in range(3):
        if column_info[i] == "R":
            possible_columns = get_remaining_half("UPPER", possible_columns)
        elif column_info[i] == "L":
            possible_columns = get_remaining_half("LOWER", possible_columns)
    return possible_columns[0]

def get_row(boarding_pass):
    row_info = boarding_pass[:-3]
    print(row_info)
    return row_info

def get_seat_id(row, column):
    return row * 8 + column

def get_remaining_half(mode, full_range):
    half_range = int(len(full_range)*0.5)
    if mode == "LOWER":
        return full_range[:-half_range]
    elif mode == "UPPER":
        return full_range[half_range:]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    # print(get_remaining_half("LOWER", [1,2,3,4]))
    get_highest_seat_id(data_to_list("./data"))