import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

connections:dict[str,list[str]] = {}

for row in data:
    c1, c2 = row.split("-")
    for _ in range(2):
        if c1 in connections:
            connections[c1].append(c2)
        else:
            connections[c1] = [c2]
        c1,c2 = c2,c1

triplets = set()

for row in data:
    c1, c2 = row.split("-")
    c1_connected = set(connections[c1])
    c2_connected = set(connections[c2])
    shared_third_parties = c1_connected.intersection(c2_connected)
    for c3 in shared_third_parties:
        if all((c1[0] != "t",c2[0] != "t",c3[0] != "t")):
            continue
        triplets.add(tuple(sorted([c1,c2,c3])))

print(len(triplets))