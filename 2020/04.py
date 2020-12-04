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
