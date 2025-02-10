#!/usr/bin/env python3  

import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

towel_string = data[0]

design_list = data[1].split("\n")

towels = set(n for n in towel_string.split(", "))

possible = 0

def find_towels(design):
    if design == "":
        return True
    for towel in towels:
        if design[:len(towel)] == towel:
            if find_towels(design[len(towel):]):
                return True
    return False

for design in design_list:
    if find_towels(design):
        possible += 1
        print(f"{design} is possible")
    else:
        print(f"{design} is NOT possible")

print(possible)