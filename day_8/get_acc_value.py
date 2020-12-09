def run_program(instructions):
    accumulator_value = 0
    history = []
    current_instruction_index = 0
    
    while True:
        print(f"BEFORE: current acc value = {accumulator_value}, current index = {current_instruction_index}")
        print(f"history: {history}")
        if not current_instruction_index in history:
            history.append(current_instruction_index)
        else:
            print(f"already followed instruction #{current_instruction_index}")
            print(f"won't perform {instructions[current_instruction_index]} a second time")
            print(f"AFTER: current acc value = {accumulator_value}, current index = {current_instruction_index}")
            break
        current_instruction_index, accumulator_value = get_next_instruction(instructions, current_instruction_index, accumulator_value)
        print(f"AFTER: current acc value = {accumulator_value}, current index = {current_instruction_index}")
        print(f"history: {history}")
    
    
    return "ok"


def get_next_instruction(instructions, current_index, current_accumulator_value):
    # returns index for next instruction AND the updaed accumulator value
    instruction_type = instructions[current_index].split(" ")[0]
    instruction_value = instructions[current_index].split(" ")[1]
    if instruction_type == "nop":
        # next instruction = row below
        # accumulator remains the same
        return current_index + 1, current_accumulator_value
    if instruction_type == "acc":
        # next instruction = row below
        # accumulator increases/decreases by value
        new_accumulator_value  = int(current_accumulator_value) + int(instruction_value)
        return current_index + 1, new_accumulator_value
    if instruction_type == "jmp":
        # next instruction index increases/decreases by value
        # accumulator remains the same
        new_index = int(current_index) + int(instruction_value)
        return new_index, current_accumulator_value
    
    return instructions[current_index]

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    data = data_to_list("./data")
    # print(data)
    print(run_program(data))