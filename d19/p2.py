#!/usr/bin/env python3  

import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

towel_string = data[0]

design_list = data[1].split("\n")

towels = set(n for n in towel_string.split(", "))
possibilities = 0

memo = {"":1}

def find_towels(design):
    if design in memo:
        return memo[design]
    total = 0
    for towel in towels:
        if design[:len(towel)] == towel:
            total += find_towels(design[len(towel):])
    memo[design] = total
    return total

for design_idx, design in enumerate(design_list):
    designs = find_towels(design)
    possibilities += designs
    print(f"{design_idx + 1:4} designs processed; result {designs:16}; total possibilities is now at {possibilities:17}")
print(possibilities)