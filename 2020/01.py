expenses_list = list(
    map(int, open("2020/inputs/input01.txt", "r").readlines())
)

# part 1

a = 0
b = 0

for i in expenses_list:
    for j in expenses_list:
        if(i + j == 2020):
            a = i
            b = j
            break

print(a * b)

# part 2

c = 0

for i in expenses_list:
    for j in expenses_list:
        for k in expenses_list:
            if(i + j + k == 2020):
                a = i
                b = j
                c = k
                break

print(a * b * c)
