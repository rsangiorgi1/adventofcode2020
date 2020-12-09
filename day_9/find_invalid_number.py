def find_incorrect_number(numbers, preamble_length):
    for i, entry in enumerate(numbers[preamble_length:]):
        index = i + preamble_length
        preamble_numbers = get_preamble(numbers, preamble_length, index)
        if not has_sum(list(map(int, preamble_numbers)), int(entry)):
            return entry
    return "ok"

def has_sum(preamble_numbers, current_number):
    for i, first_preamble_number in enumerate(preamble_numbers):
        for j in range(i + 1, len(preamble_numbers)):
            if first_preamble_number + preamble_numbers[j] == current_number:
                return True
    return False

def get_preamble(all_numbers, preamble_length, current_index):
    start_index = current_index - 1 - preamble_length
    end_index = current_index - 1
    return [ entry for i, entry in enumerate(all_numbers) if start_index <= i <= end_index ]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    data = data_to_list("./data")
    print(find_incorrect_number(data, 25))