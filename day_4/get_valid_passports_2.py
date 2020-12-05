import re

REQUIRED_FIELDS = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

def count_valid_passports(passports):
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport): valid_passports += 1
    return valid_passports

def is_valid_passport(passport):
    if all(word in passport for word in REQUIRED_FIELDS):
        return validate_fields(passport)
    return False

def validate_fields(passport):
    # let's try a dictionary comprehension :)
    passport_template = {key: extract_passport_value(passport, key) for key in REQUIRED_FIELDS}

    # Check for the following rules:
    # byr: length: 4, type int, min 1920, max 2002
    # iyr: length: 4, type int, min 2010, max 2020
    # eyr: length: 4, type int, min 2020, max 2030
    # hgt: ends with in? min 59, max 76 | ends with cm? min 150, max 193
    # hcl: hex, so min #000000, max #ffffff
    # ecl: enum(amb blu brn gry grn hzl oth)
    # pid: length: 9, type int, min 000000000, max 999999999
    return \
    is_valid_number(passport_template["byr"], 4, 1920, 2002) and \
    is_valid_number(passport_template["iyr"], 4, 2010, 2020) and \
    is_valid_number(passport_template["eyr"], 4, 2020, 2030) and \
    is_valid_height(passport_template["hgt"]) and \
    is_valid_hex(passport_template["hcl"]) and \
    is_valid_eye_color(passport_template["ecl"]) and \
    is_valid_number(passport_template["pid"], 9, 0, 999999999)

# validation functions
def is_valid_number(number, length, min_value, max_value):
    number_as_int = 0
    try:
        number_as_int = int(number)
    except ValueError:
        return False
    return len(number) == length and min_value <= number_as_int <= max_value

def is_valid_hex(value):
    return bytes("#000000", "utf-8") <= bytes(value, "utf-8") <= bytes("#ffffff", "utf-8")

def is_valid_height(value):
    if value.endswith("in"):
        return 59 <= int(value[:-2]) <= 76
    elif value.endswith("cm"):
        return 150 <= int(value[:-2]) <= 193
    else: return False

def is_valid_eye_color(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# helper functions
def extract_passport_value(passport, key):
    return re.search(rf"{key}:(.*?)(?!\S)", passport).group(1)

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n\n")))

if __name__ == "__main__":
    print(count_valid_passports(data_to_list("./data")))