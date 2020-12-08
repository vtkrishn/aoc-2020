import re

def check_fields(passport):
    valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return valid_fields.issubset(set(passport.keys()))

def check_year(passport, key, start, end):
    return start <= int(passport.get(key, -1)) <= end

def check_byr(passport):
    return check_year(passport, 'byr',1920, 2002)

def check_iyr(passport):
    return check_year(passport, 'iyr', 2010, 2020)

def check_eyr(passport):
    return check_year(passport, 'eyr', 2020, 2030)

def check_hgt(passport):
    value = passport.get('hgt')
    if value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193: return True
    if value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76: return True

def check_hcl(passport):
    return re.compile(r"^#[0-9a-f]{6}$").match(passport['hcl'])

def check_ecl(passport):
    return passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def check_pid(passport):
    return re.compile(r"^\d{9}$").match(passport['pid'])

def check_all(passport):
    return all(function_call(passport) for function_call in [check_fields, check_byr, check_iyr, check_eyr,check_hgt, check_hcl, check_ecl, check_pid])

def parse(input_lines):
    passports = []
    passport = {}
    for line in input_lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            for field in line.split(' '):
                key, value = field.split(':')
                passport[key] = value
    if passport:
        passports.append(passport)
    return passports


with open('inputs.txt', 'r') as fh:
    input_lines = fh.read().splitlines()

    passports = parse(input_lines)

    # part 1
    part1 = sum([check_fields(passport) for passport in passports])
    # part 2
    part2 = sum([check_all(passport) for passport in passports])

    print(part1)
    print(part2)