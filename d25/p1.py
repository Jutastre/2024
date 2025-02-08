import itertools
FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

keys = []
locks = []

for object in data:
    array = []
    lines = object.split("\n")
    if lines[0][0] == ".":
        for x in range(5):
            for y in range(6):
                if lines[y+1][x] == "#":
                    array.append(5-y)
                    break
        keys.append(array)
    if lines[0][0] == "#":
        for x in range(5):
            for y in range(6):
                if lines[y+1][x] == ".":
                    array.append(y)
                    break
        locks.append(array)

pairs_that_fit = 0

for key,lock in itertools.product(keys,locks):
    fits = True
    for x in range(5):
        if key[x] + lock[x] > 5:
            fits = False
            break
    if fits:
        pairs_that_fit += 1

print(pairs_that_fit)