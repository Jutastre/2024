import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip()

map = data_string.split("\n")

xmax = len(map[0]) - 1
ymax = len(map) - 1

for y, row in enumerate(map):
    for x, char in enumerate(row):
        if char == "S":
            start = (x, y, 1)
        if char == "E":
            end = (x, y)


def neighbours(x, y, d):
    yield (x, y, (d - 1) % 4)
    yield (x, y, (d + 1) % 4)
    match d:
        case 0:
            potential = (x, y - 1, d)
        case 1:
            potential = (x + 1, y, d)
        case 2:
            potential = (x, y + 1, d)
        case 3:
            potential = (x - 1, y, d)
    x, y, d = potential
    if x < 0 or x > xmax or y < 0 or y > ymax:
        return
    if map[y][x] == "#":
        return
    yield potential


def backwards_neighbours(x, y, d):
    yield (x, y, (d - 1) % 4)
    yield (x, y, (d + 1) % 4)
    match d:
        case 0:
            yield (x, y + 1, d)
        case 1:
            yield (x - 1, y, d)
        case 2:
            yield (x, y - 1, d)
        case 3:
            yield (x + 1, y, d)


to_check = [start]
checked_positions = {start: 0}
updated_something = True
while updated_something:
    to_check_next = []
    updated_something = False
    for position in to_check:
        x, y, d = position
        score = checked_positions[position]
        for neighbour in neighbours(x, y, d):
            if d == neighbour[2]:
                target_score = score + 1
            else:
                target_score = score + 1000
            if (
                neighbour not in checked_positions
                or checked_positions[neighbour] > target_score
            ):
                checked_positions[neighbour] = target_score
                updated_something = True
                to_check_next.append(neighbour)
    to_check = to_check_next

in_short_path = set()

potential_winners = []
min_score = 999999999999999999999999999999999999999999
for position, score in checked_positions.items():
    if position[:2] == end:
        potential_winners.append((position,score))
        min_score = min(min_score, score)
print(min_score)

to_check = []
for position,score in potential_winners:
    if score == min_score:
        to_check.append(position)

while to_check:
    to_check_next = []
    for position in to_check:
        x, y, d = position
        in_short_path.add((x, y))
        for neighbour in backwards_neighbours(x, y, d):
            if neighbour not in checked_positions or neighbour in to_check_next:
                continue
            if neighbour[2] != position[2] and (
                checked_positions[position] == checked_positions[neighbour] + 1000
            ):
                to_check_next.append(neighbour)
            elif neighbour[2] == position[2] and (
                checked_positions[position] == checked_positions[neighbour] + 1
            ):
                to_check_next.append(neighbour)
    to_check = to_check_next
# print(in_short_path)

def print_map(map,pois):
    for y,row in enumerate(map):
        for x,char in enumerate(row):
            if (x,y) in pois:
                print('O',end='')
            else:
                print(char,end='')
        print("")
    
print_map(map,in_short_path)
print(len(in_short_path))