answers = open("2020/inputs/input06.txt").read().split("\n\n")


# part 1

sum = 0

for a in answers:
    sum += len(set(a.replace("\n", "")))

print(sum)


# part 2

sum = 0

for a in answers:
    sum += len(set.intersection(*list(map(set, a.rstrip().split("\n")))))

print(sum)
