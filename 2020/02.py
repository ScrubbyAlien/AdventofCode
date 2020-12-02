passwords = open("2020/inputs/input02.txt", "r").readlines()

# part 1

valid_pswds = 0

for p in passwords:
    password = p.split(": ")[1].split("\n")[0]
    maxNumber = int(p.split("-")[1].split(" ")[0])
    minNumber = int(p.split("-")[0])
    letter = p.split(" ")[1].split(":")[0]
    letter_instances = 0
    for char in password:
        if (char == letter):
            letter_instances += 1
    if(letter_instances >= minNumber):
        if(letter_instances <= maxNumber):
            valid_pswds += 1

print(valid_pswds)

# part 2

valid_pswds = 0

for p in passwords:
    password = p.split(": ")[1].split("\n")[0]
    first_pos = int(p.split("-")[0]) - 1
    second_pos = int(p.split("-")[1].split(" ")[0]) - 1
    letter = p.split(" ")[1].split(":")[0]

    if(password[first_pos] == letter or password[second_pos] == letter):
        if(not (password[first_pos] == letter and password[second_pos] == letter)):
            valid_pswds += 1

print(valid_pswds)
