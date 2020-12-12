import math

instructions = open("2020/inputs/input12.txt", "r").readlines()


# part 1

p = [0, 0]
cur_angle = 0
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
cur_dir = dirs[int((cur_angle % 360) / 90)]

for i in instructions:
    i = i.rstrip()
    inst, value = i[0], int(i[1:])
    if(inst == "R"):
        cur_angle += value
        cur_dir = dirs[int((cur_angle / 90) % 4)]
    if(inst == "L"):
        cur_angle -= value
        cur_dir = dirs[int((cur_angle / 90) % 4)]
    if(inst == "F"):
        p[0] += cur_dir[0] * value
        p[1] += cur_dir[1] * value
    if(inst == "N"):
        p[1] += value
    if(inst == "E"):
        p[0] += value
    if(inst == "S"):
        p[1] -= value
    if(inst == "W"):
        p[0] -= value

print(abs(p[0]) + abs(p[1]))


# part 2

wp = [10, 1]
p = [0, 0]


def rot(wp, value, sign):
    v = value * sign
    return [wp[0] * int(math.cos(math.radians(v))) -
            wp[1] * int(math.sin(math.radians(v))),
            wp[0] * int(math.sin(math.radians(v))) +
            wp[1] * int(math.cos(math.radians(v)))]


for i in instructions:
    i = i.rstrip()
    inst, value = i[0], int(i[1:])
    if(inst == "N"):
        wp[1] += value
    if(inst == "E"):
        wp[0] += value
    if(inst == "S"):
        wp[1] -= value
    if(inst == "W"):
        wp[0] -= value
    if(inst == "F"):
        for i in range(value):
            p[0] += wp[0]
            p[1] += wp[1]
    if(inst == "L"):
        wp = rot(wp, value, 1)
    if(inst == "R"):
        wp = rot(wp, value, -1)

print(abs(p[0]) + abs(p[1]))
