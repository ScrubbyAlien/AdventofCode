import time

numbers = list(map(int, open("2020/inputs/input09.txt", "r").readlines()))

# part 1

wrong_number = 0

for i in range(25, len(numbers)):
    possible_numbers = []
    for x in range(i-25, i):
        for y in range(i-25, i):
            if(numbers[x] != numbers[y]):
                possible_numbers.append(numbers[x] + numbers[y])
    if(numbers[i] not in possible_numbers):
        print(numbers[i])
        wrong_number = numbers[i]


# part 2

start = time.time()

for r in range(2, len(numbers) + 1):
    for i in range(0, len(numbers)-r):
        l = numbers[i:i+r]
        if(sum(l) == wrong_number):
            print(min(l) + max(l))
            break
    else:
        continue
    break

end = time.time()

print(end - start)
