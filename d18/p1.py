#!/usr/bin/env python3  

import itertools

FILENAME = "in.txt"

if FILENAME[0] == "t":
    xmax = 6
    ymax = 6
    bytes_to_check = 12
else:
    xmax = 70
    ymax = 70
    bytes_to_check = 1024

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

fallen_bytes = []
for row in data[:bytes_to_check]:
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

map = [["#" if (x,y) in fallen_bytes else ' ' for x in range(xmax+1)] for y in range(ymax+1)]

to_check = [(0, 0)]
steps_taken = 0
already_checked = []
while (xmax, ymax) not in to_check:
    to_check_next = []
    for position in to_check:
        for neighbour in neighbours(position):
            if neighbour not in already_checked and neighbour not in fallen_bytes:
                to_check_next.append(neighbour)
        already_checked.append(position)
    to_check = to_check_next
    steps_taken += 1
    print(f"\n{steps_taken}:\n")
    #print_map(map, already_checked)
    #input()


print(steps_taken)
