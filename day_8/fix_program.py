def get_working_instructions():
    is_valid_program = False
    accumulator = 0
    start_search_from = 0
    
    while not is_valid_program:
        initial_instructions = data_to_list("./data")
        flipped_instructions, flipped_instruction_index = flip_first_jmp_nop(initial_instructions, start_search_from)
        start_search_from = flipped_instruction_index + 1
        accumulator, is_valid_program = check_program(flipped_instructions)
    return accumulator

def flip_first_jmp_nop(instructions, start_index):
    found_at = 0
    for i in range(start_index, len(instructions)):
        if instructions[i].split(" ")[0] == "nop":
            instructions[i] = "jmp" + instructions[i][3:]
            found_at = i
            break
        if instructions[i].split(" ")[0] == "jmp":
            instructions[i] = "nop" + instructions[i][3:]
            found_at = i
            break
    return instructions, found_at

def check_program(instructions):
    accumulator_value = 0
    history = []
    current_instruction_index = 0
    
    while True:
        if not current_instruction_index in history:
            history.append(current_instruction_index)
        else:
            return accumulator_value, False
        current_instruction_index, accumulator_value = get_next_instruction(instructions, current_instruction_index, accumulator_value)
        if current_instruction_index == len(instructions):
            return accumulator_value, True
        if current_instruction_index > len(instructions):
            return accumulator_value, False

def get_next_instruction(instructions, current_index, current_accumulator_value):
    # returns index for next instruction AND the updated accumulator value
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
    print(get_working_instructions())
