def count_valid_passwords(passwords):
    valid_passwords = 0
    for pw in passwords:
        pieces = pw.split()
        number = pieces[0]
        lower_limit = number.split("-")[0]
        upper_limit = number.split("-")[1]
        letter = pieces[1][0] # trim the ":"
        password = pieces[2]
        hits = password.count(letter)
        if int(lower_limit) <= hits <= int(upper_limit):
            valid_passwords += 1
    return valid_passwords

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    print(count_valid_passwords(data_to_list("./data")))