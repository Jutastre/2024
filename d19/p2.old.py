#!/usr/bin/env python3  

import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

towel_string = data[0]

design_list = data[1].split("\n")

towels = set(n for n in towel_string.split(", "))

possibilities = 0

def find_towels(design):
    if design == "":
        return 1
    total = 0
    for towel in towels:
        if design[:len(towel)] == towel:
            total += find_towels(design[len(towel):])
    return total

for design_idx, design in enumerate(design_list):
    possibilities += find_towels(design)
    print(f"{design_idx + 1:4} designs processed; total possibilities is now at {possibilities}")
print(possibilities)