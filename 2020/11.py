import copy

seats = list(map(list, open("2020/inputs/input11.txt", "r").read().split("\n")))


# part 1

def is_valid(x, y):
    return (y >= 0 and y < len(seats)) and (x >= 0 and x < len(seats[y]))


def num_occ_adj_seats(x, y):
    return len([(x_, y_)
                for x_ in range(x-1, x+2)
                for y_ in range(y-1, y+2)
                if((x, y) != (x_, y_)
                    and is_valid(x_, y_)
                    and seats[y_][x_] == "#")])


def calc_new_seats():
    global seats
    global new_seats

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if(seats[y][x] == "L" and num_occ_adj_seats(x, y) == 0):
                new_seats[y][x] = "#"
            elif(seats[y][x] == "#" and num_occ_adj_seats(x, y) >= 4):
                new_seats[y][x] = "L"


new_seats = copy.deepcopy(seats)

calc_new_seats()
while seats != new_seats:
    seats = copy.deepcopy(new_seats)
    calc_new_seats()


n = 0
for y in range(len(seats)):
    for x in range(len(seats[y])):
        if(seats[y][x] == "#"):
            n += 1

print(n)


# part 2


seats = list(map(list, open("2020/inputs/input11.txt", "r").read().split("\n")))

new_seats = copy.deepcopy(seats)

deltas = [(-1, -1), (0, -1), (1, -1),
          (-1, 0),           (1, 0),
          (-1, 1),  (0, 1),  (1, 1)]


def num_occ_seen_seats(x, y):
    n = 0
    for d in deltas:
        m = 1
        while True:
            if(is_valid(x + d[0] * m, y + d[1] * m)):
                if(seats[y + d[1] * m][x + d[0] * m] != "."):
                    if(seats[y + d[1] * m][x + d[0] * m] == "#"):
                        n += 1
                    break
            else:
                break
            m += 1
    return n


def calc_new_seats_2():
    global seats
    global new_seats

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if(seats[y][x] == "L" and num_occ_seen_seats(x, y) == 0):
                new_seats[y][x] = "#"
            elif(seats[y][x] == "#" and num_occ_seen_seats(x, y) >= 5):
                new_seats[y][x] = "L"


calc_new_seats_2()
while seats != new_seats:
    seats = copy.deepcopy(new_seats)
    calc_new_seats_2()

n = 0
for y in range(len(seats)):
    for x in range(len(seats[y])):
        if(seats[y][x] == "#"):
            n += 1

print(n)
