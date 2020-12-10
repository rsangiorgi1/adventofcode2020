import numpy as np

def get_answer():
    data = data_to_list("./tdata")
    sorted_adapters = get_full_list(data)
    all_valid_orders_to_check = [np.array(sorted_adapters)]
    found_valid_orders = [np.array(sorted_adapters)]
    history = []

    while len(all_valid_orders_to_check) != 0:
        new_valid_orders = get_valid_orders_by_deleting_1(all_valid_orders_to_check[0])
        [ found_valid_orders.append(new_order) for new_order in new_valid_orders ]
        history.append((all_valid_orders_to_check[0]))
        all_valid_orders_to_check.pop(0)
        [ all_valid_orders_to_check.append(new_order) for new_order in new_valid_orders ]

        # make things unique
        all_valid_orders_to_check = get_unique_arrays(all_valid_orders_to_check)
        found_valid_orders = get_unique_arrays(found_valid_orders)

        # TODO: strip all valid orders to check from orders found in history
    unique_found_valid_orders = set(map(tuple, found_valid_orders))
    return len(unique_found_valid_orders)

def get_unique_arrays(list_of_arrays):
    return list(set(map(tuple, list_of_arrays)))

def get_valid_orders_by_deleting_1(sorted_adapters):
    original_list = np.array(sorted_adapters)
    valid_orders = []
    print("")
    for i in range(1, len(sorted_adapters) - 2):
        print(f"checking {sorted_adapters[:i]} >{i}< {sorted_adapters[i + 1:]}")
        if can_be_removed(sorted_adapters, i):
            new_option = np.delete(original_list, i)
            valid_orders.append(new_option)
            sorted_adapters = original_list
    return valid_orders


def can_be_removed(sorted_adapters, index):
    if index != 0 and index < len(sorted_adapters) - 1 and sorted_adapters[index + 1] - sorted_adapters[index - 1] <= 3:
        return True
    return False

def is_valid_order(adapters):
    if adapters[0] != 0:
        return False
    if adapters[len(adapters) - 1] != max(adapters):
        return False
    for i in range(0, len(adapters) - 1):
        if not 0 <= adapters[i + 1] - adapters[i] <= 3:
            return False
    return True


def get_full_list(data):
    sorted_adapters = sorted(data)
    # add charging outlet joltage
    sorted_adapters.insert(0, 0)
    # add device's built in joltage
    sorted_adapters.append(max(data) + 3)
    return sorted_adapters

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))

if __name__ == "__main__":
    print(get_answer())