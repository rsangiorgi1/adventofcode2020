def count_valid_passwords(passwords):
    valid_passwords = 0
    for pw in passwords:
        pieces = pw.split()
        number = pieces[0]
        first_index = int(number.split("-")[0])
        second_index = int(number.split("-")[1])
        letter = pieces[1][0] # trim the ":"
        password = pieces[2]
        number_of_hits = 0
        if is_letter_at_position(first_index, password, letter):
            number_of_hits += 1
        if is_letter_at_position(second_index, password, letter):
            number_of_hits += 1
        if number_of_hits == 1:
            valid_passwords += 1
    return valid_passwords

def is_letter_at_position(position, word, letter):
    if len(word) < position:
        return False
    return word[position - 1] == letter

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    print(count_valid_passwords(data_to_list("./data")))