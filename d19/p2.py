#!/usr/bin/env python3  

import itertools

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")

towel_string = data[0]

design_list = data[1].split("\n")

towel_list = [n for n in towel_string.split(", ")]
towel_lengths = [len(n) for n in towel_list]
towel_lengths = sorted(list(set(towel_lengths)))
towels = set(towel_list)
possibilities = 0

memo = {"":1}

def find_towels(design):
    if design in memo:
        return memo[design]
    total = 0
    for length in towel_lengths:
        if design[:length] in towels:
            total += find_towels(design[length:])
    memo[design] = total
    return total

for design_idx, design in enumerate(design_list):
    designs = find_towels(design)
    possibilities += designs
    print(f"{design_idx + 1:8} designs processed; result {designs:8}; total possibilities is now at {possibilities:10}")
print(possibilities)