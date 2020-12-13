# luciapuzzle
from functools import reduce
import math

info = open("2020/inputs/input13.txt", "r").read()


# part 1

earliest_time = int(info.split("\n")[0])
bus_ids = list(map(int, filter(lambda a: a != "x",
                               info.split("\n")[1].split(","))))

id_diff = [2**64, 2**64, 2**64]
for bus in bus_ids:
    f = math.ceil(earliest_time / bus)
    if(bus * f < id_diff[1]):
        id_diff = [bus, f * bus, f * bus - earliest_time]

print(id_diff[0] * id_diff[2])


# part 2


a_i = []
busses = info.split("\n")[1].split(",")
for a in busses:
    if(a != "x"):
        a_i.append(int(a) - int(busses.index(a)))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


n = bus_ids
a = a_i
print(chinese_remainder(n, a))
