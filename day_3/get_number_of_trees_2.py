from functools import reduce

def get_tree_count(data, right, down):
    # print("---------------")
    row_length = len(data[0])
    number_of_trees = 0
    for vertical_position, row in enumerate(data):
        # Ensure vertical position is correct by skipping over unnecessary rows
        if not vertical_position % down == 0:
            # print(row)
            continue
        
        # Ensure horizontal position is correct
        # 
        # Example: slope rules are "right 3, down 2"
        # if vertical_position = 0, horizontal_position should be 0
        # SKIPPED if vertical_position = 1
        # if vertical_position = 2, horizontal_position should be 3
        # SKIPPED if vertical_position = 3
        # if vertical_position = 4, horizontal_position should be 5
        # SKIPPED if vertical_position = 5
        horizontal_position = int((vertical_position / down * right) % row_length)
        
        # print(row[:horizontal_position] + "[" + row[horizontal_position] + "]" + row[horizontal_position + 1:])

        if row[horizontal_position] == "#":
            number_of_trees += 1
    return number_of_trees


def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split()))

if __name__ == "__main__":
    trees_from_all_slopes = [
        get_tree_count(data_to_list("./data"), 1, 1),
        get_tree_count(data_to_list("./data"), 3, 1),
        get_tree_count(data_to_list("./data"), 5, 1),
        get_tree_count(data_to_list("./data"), 7, 1),
        get_tree_count(data_to_list("./data"), 1, 2)
    ]
    product = reduce((lambda x, y: x * y) , trees_from_all_slopes)
    print(product)