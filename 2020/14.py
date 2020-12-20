import re

instructions = open("2020/inputs/input14.txt", "r").readlines()


# part 1

mask = ""

memory = {}

for inst in instructions:
    i = inst.split(" = ")
    name = i[0]
    value = i[1].rstrip()
    if(name == "mask"):
        mask = value.rstrip()
        continue

    adress = int(re.match(r"mem\[(\d+)\]", name).group(1))
    bin_value = "0"*(36-len(bin(int(value))[2:])) + bin(int(value))[2:]
    write_value = ""
    for i in range(len(mask)):
        if(mask[i] == "X"):
            write_value += bin_value[i]
        if(mask[i] == "0"):
            write_value += "0"
        if(mask[i] == "1"):
            write_value += "1"
    memory[adress] = int(write_value, 2)

print(sum(memory.values()))


# part 2


def get_adresses(ad, m):
    adresses = []
    iterations = len(list(filter(lambda a: a == "X", m)))
    for n in range(2**iterations):
        float_iters = "0"*(iterations-len(bin(n)[2:])) + bin(n)[2:]
        a = ""
        p = 0
        for i in range(len(m)):
            if(m[i] == "0"):
                a += ad[i]
            if(m[i] == "1"):
                a += "1"
            if(m[i] == "X"):
                a += float_iters[p]
                p += 1
        adresses.append(a)
    return adresses


memory = {}

for inst in instructions:
    i = inst.split(" = ")
    name = i[0]
    value = i[1].rstrip()
    if(name == "mask"):
        mask = value.rstrip()
        continue

    temp = bin(int(re.match(r"mem\[(\d+)\]", name).group(1)))[2:]
    adress = "0"*(36-len(temp)) + temp
    for a in get_adresses(adress, mask):
        memory[int(a)] = int(value)

print(sum(memory.values()))
