#!/usr/bin/env python3

import itertools

FILENAME = "in.txt"

if FILENAME[0] == "t":
    xmax = 6
    ymax = 6
else:
    xmax = 70
    ymax = 70

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

fallen_bytes = []
for row in data:
    x, y = row.split(",")
    fallen_bytes.append((int(x), int(y)))


def neighbours(pos):
    x, y = pos
    possible_neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for nx, ny in possible_neighbours:
        if nx < 0 or nx > xmax or ny < 0 or ny > ymax:
            continue
        yield (nx, ny)


def print_map(map, pois):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if (x, y) in pois:
                print("O", end="")
            else:
                print(char, end="")
        print("")


map = [
    ["#" if (x, y) in fallen_bytes else " " for x in range(xmax + 1)]
    for y in range(ymax + 1)
]


def pathfind(fallen_byte_list, fallen_byte_count):
    fallen_bytes = fallen_byte_list[:fallen_byte_count]
    to_check = [(0, 0)]
    already_checked = []
    updated = True
    while updated and (xmax, ymax) not in to_check:
        updated = False
        to_check_next = []
        for position in to_check:
            for neighbour in neighbours(position):
                if (
                    neighbour not in to_check_next
                    and neighbour not in already_checked
                    and neighbour not in fallen_bytes
                ):
                    to_check_next.append(neighbour)
                    updated = True
            already_checked.append(position)
        to_check = to_check_next
    return (xmax, ymax) in to_check


pivot = len(fallen_bytes) // 2
pivot_size = pivot // 2
while pivot_size > 0:
    print(f"testing {pivot}")
    if not pathfind(fallen_bytes, pivot):
        pivot -= pivot_size
    else:
        pivot += pivot_size
    pivot_size //= 2

pivot -= 1
print(pivot)
print(pathfind(fallen_bytes, pivot))
print(fallen_bytes[pivot-1])

pivot += 1
print(pivot)
print(pathfind(fallen_bytes, pivot))
print(fallen_bytes[pivot-1])

pivot += 1
print(pivot)
print(pathfind(fallen_bytes, pivot))
print(fallen_bytes[pivot-1])
