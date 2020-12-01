def get_multiplication_of_entries_that_sum_to_2020(entries):
    number_of_entries = len(entries)
    number_of_loops = 0
    for i, entry in enumerate(entries):
        # print("new iteration:")
        # print(i, entry)
        for j in range(i, number_of_entries):
            number_of_loops +=1
            entry_sum = entry + entries[j]
            print(f"sum is: {entry_sum}")
            if entry + entries[j] == 2020:
                print(f"found it! {entry}, {entries[j]}")
                print(f"# of tries: {number_of_loops}")
                return entry * entries[j]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))
    

if __name__ == "__main__":
    all_entries = data_to_list("./data")
    print(all_entries)
    print(get_multiplication_of_entries_that_sum_to_2020(all_entries))
    