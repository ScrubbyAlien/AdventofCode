boarding_passes = open("2020/inputs/input05.txt").readlines()


# part 1

def seat_id_of(p):
    s = 0
    p = p.rstrip()
    for c in p:
        s = s << 1
        if(c == "B" or c == "R"):
            s = s | 1
    return s


seat_ids = list(map(seat_id_of, boarding_passes))
seat_ids.sort()

print(seat_ids[-1])


# part 2

for i in range(0, len(seat_ids) - 1):
    if(seat_ids[i+1] - seat_ids[i] == 2):
        print(seat_ids[i] + 1)
        break
