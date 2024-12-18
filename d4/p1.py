import re

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

xmas_sum = 0
ymax = len(data)
xmax = len(data[0])
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if x < xmax - 3:
            if row[x:x+4] == "XMAS" or row[x:x+4] == "SAMX":
                xmas_sum += 1
        if y < ymax - 3:
            word = "".join(data[y_offset][x] for y_offset in range(y,y+4))
            if word == "XMAS" or word == "SAMX":
                xmas_sum += 1
        if y < ymax - 3 and x < xmax - 3:
            word = "".join(data[y_offset][x_offset] for x_offset, y_offset in zip(range(x,x+4), range(y,y+4)))
            if word == "XMAS" or word == "SAMX":
                xmas_sum += 1
        if y > 2 and x < xmax - 3:
            word = "".join(data[y_offset][x_offset] for x_offset, y_offset in zip(range(x,x+4), range(y,y-4, -1)))
            if word == "XMAS" or word == "SAMX":
                xmas_sum += 1


print (xmas_sum)
