def find_contiguous_set(entries, target_number):
    contigous_set_so_far = []
    for i, entry in enumerate(entries):
        for j in range(i, len(entries)):
            if sum(contigous_set_so_far) < target_number:
                contigous_set_so_far.append(int(entries[j]))
            elif sum(contigous_set_so_far) == target_number:
                if len(contigous_set_so_far) != 1:
                    return (min(contigous_set_so_far) + max(contigous_set_so_far))
                contigous_set_so_far = []
            elif sum(contigous_set_so_far) > target_number:
                contigous_set_so_far = []
    return "nothing found :("

def find_incorrect_number(numbers, preamble_length):
    for i, entry in enumerate(numbers[preamble_length:]):
        index = i + preamble_length
        preamble_numbers = get_preamble(numbers, preamble_length, index)
        if not has_sum(list(map(int, preamble_numbers)), int(entry)):
            return int(entry)
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
    incorrect_number = find_incorrect_number(data, 25)
    print(find_contiguous_set(data, incorrect_number))