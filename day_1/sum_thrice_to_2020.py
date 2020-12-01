def get_multiplication_of_entries_that_sum_to_2020(entries):
    number_of_entries = len(entries)
    number_of_loops = 0
    for i, entry in enumerate(entries):
        # print(f"new iteration for i: {i}")
        
        for j in range(i + 1, number_of_entries):
            # print(f"new iteration for j: {j}")
            for k in range(j + 1, number_of_entries):
                number_of_loops +=1
                # print(f"new iteration for k: {k}")
                # print(f"""First number: {entry},
                # Second number: {entries[j]},
                # Third number: {entries[k]}""")
                entry_sum = entry + entries[j] + entries[k]
                # print(f"sum is: {entry_sum}")
                if entry_sum == 2020:
                    # print(f"found it! {entry}, {entries[j]}, {entries[k]}")
                    # print(f"# of tries: {number_of_loops}")
                    return entry * entries[j] * entries[k]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))
    

if __name__ == "__main__":
    all_entries = data_to_list("./data")
    print(get_multiplication_of_entries_that_sum_to_2020(all_entries))
    # print(get_multiplication_of_entries_that_sum_to_2020([100, 2000, 12351, 11, 9, 6]))
    