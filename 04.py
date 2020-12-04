import re


def part1(data):
    passports = get_passports(data)

    n_complete_passports = 0

    for passport in passports:
        n_complete_passports += check_passport_completeness(passport)

    return n_complete_passports


def part2(data):
    passports = get_passports(data)

    n_valid_passports = 0

    for passport in passports:
        n_valid_passports += check_passport_validity(passport)

    return n_valid_passports


def get_passports(data):
    passports_data = data.split('\n\n')

    passports = []

    for passport in passports_data:
        passports.append(extract_passport_entries(passport))

    return passports


def extract_passport_entries(passport_data):
    key_value_regex = r'\w+:\S+'

    match = re.findall(key_value_regex, passport_data)

    passport_entries = dict(item.split(":") for item in [m for m in match])

    return passport_entries


def check_passport_completeness(passport):
    mandatory_entries = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    passport_entries = passport.keys()

    for entry in mandatory_entries:
        if entry not in passport_entries:
            return False

    return True


def check_passport_validity(passport):
    if not check_passport_completeness(passport):
        return False

    mandatory_entries_conditions = {
        'byr': r'int(val) >= 1920 and int(val) <= 2020',
        'iyr': r'int(val) >= 2010 and int(val) <= 2020',
        'eyr': r'int(val) >= 2020 and int(val) <= 2030',
        'hgt': r'validate_height(val)',
        'hcl': r're.match(r"^#[a-f0-9]{6}$", val) != None',
        'ecl': r're.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", val) != None',
        'pid': r're.match(r"^[0-9]{9}$", val) != None'
    }

    global_dict = {'re': re, 'validate_height' : validate_height}

    for key in mandatory_entries_conditions.keys():
        if not eval(mandatory_entries_conditions[key], global_dict,
                    {'val': passport[key]}):
            return False

    return True


def validate_height(val):
    match = re.match(r"^(\d+)(cm|in)$", val)

    if match == None:
        return False

    height = int(match.group(1))
    unit = match.group(2)

    if (unit == 'cm' and height >= 150 and height <= 193) or (unit == 'in' and height >= 59 and height <= 76):
        return True
    else:
        return False
