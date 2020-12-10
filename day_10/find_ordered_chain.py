# data = list of output joltage of the joltage adapters in my bag
# any adapter can take between value & value - 3 jolts as input
# device has joltage for 3 jolts higher than highest in bag
# charging outlet has joltage rating 0
# don't skip adapters
# 
# example: charging outlet has value 0, so only adapters that can fit have value 1-3
# choose adapter with value 1 (1 - 0 = 1), only adapters that will fit have value 2-4
# choose adapter with value 4 (4 - 1 = 3), only adapters that will fit have value 5-7
# choose adapter with value 5 (5 - 4 = 3), only adapters that will fit have value 6-8
# choose adapter with value 6 (6 - 5 = 1), only adapters that will fit have value 6-9
# choose adapter with value 7 (7 - 6 = 1), only adapters that will fit have value 7-10
def get_answer():
    data = data_to_list("./data")
    sorted_adapters = get_full_list(data)
    diff_1_count = 0
    diff_3_count = 0
    for i in range(0, len(sorted_adapters) - 1):
        current_adapter = sorted_adapters[i]
        next_adapter = sorted_adapters[i + 1]
        diff = next_adapter - current_adapter
        print(type(current_adapter))
        print(f"adapter # {i} has value {current_adapter}, upcoming adapter has value {next_adapter}, diff is {diff}")
        if diff == 1:
            print("ooo")
            diff_1_count += 1
        if diff == 3:
            print("XXX")
            diff_3_count += 1
    return f"1 differences: {diff_1_count}, 3 differences: {diff_3_count}, product = {diff_1_count * diff_3_count}"




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