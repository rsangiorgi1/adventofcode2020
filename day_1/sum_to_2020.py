def get_multiplication_of_entries_that_sum_to_2020(entries):
    number_of_entries = len(entries)
    for i, entry in enumerate(entries):
        for j in range(i, number_of_entries):
            if entry + entries[j] == 2020:
                return entry * entries[j]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))
    

if __name__ == "__main__":
    all_entries = data_to_list("./data")
    print(get_multiplication_of_entries_that_sum_to_2020(all_entries))
    