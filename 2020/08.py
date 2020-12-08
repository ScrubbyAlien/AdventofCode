instructions = open("2020/inputs/input08.txt", "r").readlines()


# part 1


indexes_visited = []
acc = 0
i = 0
while i < len(instructions):

    if(i in indexes_visited):
        break
    else:
        indexes_visited.append(i)

    instruction, value = instructions[i].rstrip().split(" ")
    if(instruction == "acc"):
        acc += int(value)
    if(instruction == "jmp"):
        i += int(value) - 1

    i += 1

print(acc)


# part 2


jmp_indexes = []
nop_indexes = []
for i in range(0, len(instructions)):
    p = instructions[i].rstrip().split(" ")[0]
    if(p == "jmp"):
        jmp_indexes.append(i)
    if(p == "nop"):
        nop_indexes.append(i)


def run_program(instructions):
    no_loop = True
    indexes_visited = []
    acc = 0
    i = 0
    while i < len(mod_instructions):

        if(i in indexes_visited):
            no_loop = False
            break
        else:
            indexes_visited.append(i)

        instruction, value = mod_instructions[i].rstrip().split(" ")
        if(instruction == "acc"):
            acc += int(value)
        if(instruction == "jmp"):
            i += int(value) - 1

        i += 1
    if(no_loop):
        print(acc)
    else:
        return "loop"


no_loop = True
indexes_visited = []
acc = 0
i = 0
for i in jmp_indexes:
    value = instructions[i].rstrip().split(" ")[1]
    mod_instructions = instructions.copy()
    mod_instructions[i] = "nop " + value
    run_program(mod_instructions)

for i in nop_indexes:
    value = instructions[i].rstrip().split(" ")[1]
    mod_instructions = instructions.copy()
    mod_instructions[i] = "jmp " + value
    run_program(mod_instructions)
