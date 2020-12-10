def get_possibilities(adapters):
    # add number of possibilities to add an adapter
    adapters_with_possibilities = [{
            "adapter": 0,
            "possibilities": 1
        }]
    
    for i, adapter in enumerate(adapters):
        previous_3_adapters = []
        for j in range(1,4):
            if adapter - adapters[i - j] < 4 and adapter > adapters[i-j]:
                previous_3_adapters.append(adapters[i - j])
        
        current_adapter_possibilities = 0
        for previous_adapter in previous_3_adapters:
            previous_adapter_object = [ y for y in adapters_with_possibilities if y["adapter"] == previous_adapter]
            current_adapter_possibilities += previous_adapter_object[0]["possibilities"]
        adapters_with_possibilities.append({
            "adapter": adapter,
            "possibilities": current_adapter_possibilities
        })
    # how many possibilities to add the last adapter
    return adapters_with_possibilities[-1]["possibilities"]

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
    all_adapters_sorted = get_full_list(data_to_list("./data"))
    print(get_possibilities(all_adapters_sorted))
