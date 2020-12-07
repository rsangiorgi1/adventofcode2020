def get_tree_count(data):
    row_length = len(data[0])
    print(row_length)
    number_of_trees = 0
    for i, row in enumerate(data):
        # if i = 13, index should be 13 % 10
        index = (i * 3) % row_length
        # print(index)
        

        # index = (i + 1) * 3
        if row[index] == "#":
            new_row = row[:index] + "X" + row[index + 1:]
            number_of_trees += 1
            print("hit a tree:")
        elif row[index] == ".":
            new_row = row[:index] + "O" + row[index + 1:]
        else:
            print("unexpected")
        print(row)
        print(new_row)
    print(number_of_trees)


def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    get_tree_count(data_to_list("./data"))
    # get_tree_count(data_to_list("./test_data"))
    