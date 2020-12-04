def count_valid_passports(passports):
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1
    return valid_passports

def is_valid_passport(passport):
    print(f"---> new passport: {passport}<---")
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]
    if all(word in passport for word in required_fields):
        print(f"----->valid passport: {passport}<-----")
        return True
    return False

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n\n")))

if __name__ == "__main__":
    print(count_valid_passports(data_to_list("./data")))