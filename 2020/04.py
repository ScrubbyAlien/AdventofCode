import re

passports = open("2020/inputs/input04.txt", "r").read().split("\n\n")


# part 1

correct_passports = 0


for p in passports:
    passport = re.split("[ \n]", p)
    fields_to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in passport:
        field_name = field.split(":")[0]
        if(field_name in fields_to_check):
            fields_to_check.remove(field_name)
    if(len(fields_to_check) == 0):
        correct_passports += 1
print(correct_passports)


# part 2

correct_passports = 0


def validField(field, name):
    field_value = field.split(":")[1]
    if (name == "byr"):
        return int(field_value) >= 1920 and int(field_value) <= 2002
    if (name == "iyr"):
        return int(field_value) >= 2010 and int(field_value) <= 2020
    if (name == "eyr"):
        return int(field_value) >= 2020 and int(field_value) <= 2030
    if (name == "hgt"):
        m = re.match(r"(\d+)(in|cm)", field_value)
        if (m):
            if (m.group(2) == "in"):
                return int(m.group(1)) >= 59 and int(m.group(1)) <= 76
            if (m.group(2) == "cm"):
                return int(m.group(1)) >= 150 and int(m.group(1)) <= 193
        else:
            return False
    if (name == "hcl"):
        return re.match(r"^#[0-9a-f]{6}$", field_value)
    if (name == "ecl"):
        return field_value in valid_ecls
    if (name == "pid"):
        return re.match(r"^(\d{9})$", field_value)


valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for p in passports:
    passport = re.split("[ \n]", p)
    fields_to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in passport:
        field_name = field.split(":")[0]
        if(field_name in fields_to_check):
            if(validField(field, field_name)):
                fields_to_check.remove(field_name)
    if(len(fields_to_check) == 0):
        correct_passports += 1
print(correct_passports)
