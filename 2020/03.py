grid = open("2020/inputs/input03.txt", "r").readlines()


# part 1

pos = 0
trees = 0

print(len(grid))

width = len(grid[0]) - 1

for i in range(1, len(grid)):
    row = grid[i].rstrip("\n")
    pos += 3
    pos %= width

    if (row[pos] == "#"):
        trees += 1
print(trees)


# part 2

trees = 0

tuples = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
print(len(grid))
for x, y in tuples:
    pos = 0
    for i in range(0, len(grid), y):
        row = grid[i].rstrip("\n")
        if (row[pos] == "#"):
            trees += 1
        pos = (pos+x) % width
    product *= trees
    trees = 0
print(product)


# 360502272
# 4352292000
# 3695737500
