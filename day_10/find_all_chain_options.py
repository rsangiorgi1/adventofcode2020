# import numpy as np

# def get_answer():
#     data = data_to_list("./tdata")
#     sorted_adapters = get_full_list(data)
#     all_valid_orders_to_check = [np.array(sorted_adapters)]
#     found_valid_orders = [np.array(sorted_adapters)]
#     history = []

#     while len(all_valid_orders_to_check) != 0:
#         new_valid_orders = get_valid_orders_by_deleting_1(all_valid_orders_to_check[0])
#         [ found_valid_orders.append(new_order) for new_order in new_valid_orders ]
#         history.append((all_valid_orders_to_check[0]))
#         all_valid_orders_to_check.pop(0)
#         [ all_valid_orders_to_check.append(new_order) for new_order in new_valid_orders ]
#         print("found orders: ")
#         [ print(order) for order in found_valid_orders ]
#         # make things unique
#         all_valid_orders_to_check = get_unique_arrays(all_valid_orders_to_check)
#         found_valid_orders = get_unique_arrays(found_valid_orders)

#         # TODO: strip all valid orders to check from orders found in history
#     unique_found_valid_orders = set(map(tuple, found_valid_orders))
#     return len(unique_found_valid_orders)

# def get_unique_arrays(list_of_arrays):
#     return list(set(map(tuple, list_of_arrays)))

# def get_valid_orders_by_deleting_1(sorted_adapters):
#     original_list = np.array(sorted_adapters)
#     valid_orders = []
#     print("")
#     for i in range(1, len(sorted_adapters) - 2):
#         print(f"checking if still valid order after removing {sorted_adapters[:i]} >{i}< {sorted_adapters[i + 1:]}")
#         if can_be_removed(sorted_adapters, i):

#             new_option = np.delete(original_list, i)
#             valid_orders.append(new_option)
#             sorted_adapters = original_list
#     return valid_orders


# def can_be_removed(sorted_adapters, index):
#     if index != 0 and index < len(sorted_adapters) - 1 and sorted_adapters[index + 1] - sorted_adapters[index - 1] <= 3:
#         return True
#     return False

# def is_valid_order(adapters):
#     if adapters[0] != 0:
#         return False
#     if adapters[len(adapters) - 1] != max(adapters):
#         return False
#     for i in range(0, len(adapters) - 1):
#         if not 0 <= adapters[i + 1] - adapters[i] <= 3:
#             return False
#     return True


def get_answer(adapters):
    # arr = [
    #     {
    #         "a": 3,
    #         "b": 0    
    #     },
    #     {
    #         "a": 5,
    #         "b": 2    
    #     }
    # ]
    
    # return [ x for x in arr if x["a"] == 3 ]
    
    possibilities_per_adapter = []
    for i, adapter in enumerate(adapters):
        print("\n")
        print(f"-->looking at adapter {adapter}")
        print(f"previous (max) 3 adapters:")
        previous_3_adapters = []
        for j in range(1,4):
            if adapter - adapters[i - j] < 4 and adapter > adapters[i-j]:
                previous_3_adapters.append(adapters[i - j])
        print(f"shoud look at previous adapters: {previous_3_adapters}")
        
        current_adapter_possibilities = 0
        for previous_adapter in previous_3_adapters:
            # print(adapter)
            x = [ y for y in possibilities_per_adapter if y["adapter"] == previous_adapter]
            print(f"possibilities for adapter {previous_adapter}: {x}")
            current_adapter_possibilities += x[0]["possibilities"]
        if current_adapter_possibilities == 0 or current_adapter_possibilities == 1:
            current_adapter_possibilities +=1
        new_entry = {
            "adapter": adapter,
            "possibilities": current_adapter_possibilities
        }
        print("adding new adapter:")
        print(new_entry)
        possibilities_per_adapter.append(new_entry)


    return possibilities_per_adapter[-1]["possibilities"]


def get_full_list(data):
    sorted_adapters = sorted(data)
    # add charging outlet joltage
    # sorted_adapters.insert(0, 0)
    # add device's built in joltage
    sorted_adapters.append(max(data) + 3)
    return sorted_adapters

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(int, content.split()))

if __name__ == "__main__":
    x = get_full_list(data_to_list("./tdata"))
    print(get_answer(x))