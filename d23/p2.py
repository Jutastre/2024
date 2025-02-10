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

groups:set[tuple] = set()

for row in data:
    c1, c2 = row.split("-")
    c1_connected = set(connections[c1])
    c2_connected = set(connections[c2])
    shared_third_parties = c1_connected.intersection(c2_connected)
    for c3 in shared_third_parties:
        groups.add(tuple(sorted([c1,c2,c3])))

while len(groups) > 1:
    bigger_groups = set()
    for group in groups:
        group_list = list(group)
        group_connections = [set(connections[computer]) for computer in group]
        shared_connections = group_connections[0]
        for other_computers_connections in group_connections:
            shared_connections.intersection_update(other_computers_connections)
        for shared_connection in shared_connections:
            bigger_groups.add(tuple(sorted(group_list + [shared_connection])))
    groups = bigger_groups

while True:
    bigger_groups = set()
    for group in groups:
        group_list = list(group)
        group_connections = [set(connections[computer]) for computer in group]
        shared_connections = group_connections[0]
        for other_computers_connections in group_connections:
            shared_connections.intersection_update(other_computers_connections)
        for shared_connection in shared_connections:
            bigger_groups.add(tuple(sorted(group_list + [shared_connection])))
    if len(bigger_groups) != 0:
        groups = bigger_groups
    else:
        break

print(len(groups))
for computer in groups.pop():
    print(computer, end=",")
print("")