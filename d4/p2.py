import re

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

xmas_sum = 0
ymax = len(data)-1
xmax = len(data[0])-1
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if x < 1 or x == xmax or y < 1 or y == ymax:
            continue
        if char != 'A':
            continue
        corners = [data[y-1][x-1],data[y-1][x+1],data[y+1][x-1],data[y+1][x+1]]
        if set(corners) != set(('M','S')):
            continue
        if corners[0] == corners[3] or corners[1] == corners[2]:
            continue
        xmas_sum += 1

print (xmas_sum)
