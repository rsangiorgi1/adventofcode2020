def get_multiplication_of_entries_that_sum_to_2020(entries):
    number_of_entries = len(entries)
    number_of_loops = 0
    for i, entry in enumerate(entries):
        for j in range(i + 1, number_of_entries):
            for k in range(j + 1, number_of_entries):
                number_of_loops +=1
                entry_sum = entry + entries[j] + entries[k]
                if entry_sum == 2020:
                    return entry * entries[j] * entries[k]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))
    

if __name__ == "__main__":
    all_entries = data_to_list("./data")
    print(get_multiplication_of_entries_that_sum_to_2020(all_entries))
    