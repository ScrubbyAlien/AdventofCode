jolts = list(map(int, open("2020/inputs/input10.txt", "r").readlines()))


# part 1

jolts.sort()

jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

sorted_jolt_differences = [jolts[i]-jolts[i-1] for i in range(1, len(jolts))]
sorted_jolt_differences.sort()

index = sorted_jolt_differences.index(3)
ones = sorted_jolt_differences[:index]
threes = sorted_jolt_differences[index:]

print(len(threes) * len(ones))


# part 2

jolt_differences = [jolts[i]-jolts[i-1] for i in range(1, len(jolts))]

trib = [1, 2, 4, 7]
product = 1
seq_adapt = 0

for d in jolt_differences:
    if(d == 1):
        seq_adapt += 1
    if(d == 3):
        if(seq_adapt == 0):
            seq_adapt = 1
        product *= trib[seq_adapt-1]
        seq_adapt = 0


print(product)
