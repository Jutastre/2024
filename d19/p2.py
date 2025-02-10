#!/usr/bin/env python3  

import itertools

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

towel_string = data[0]

design_list = data[1].split("\n")

towels = set(n for n in towel_string.split(", "))

possible = 0

def find_towels(design):
    if design == "":
        return 1
    for towel in towels:
        total = 0
        if design[:len(towel)] == towel:
            total += find_towels(design[len(towel):])
    return total

for design in design_list:
    possible += find_towels(design)
print(possible)