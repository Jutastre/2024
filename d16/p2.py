import itertools

FILENAME = "tin.txt"


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
    yield (x, y + 1, d)
    yield (x - 1, y, d)
    yield (x, y - 1, d)
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
to_check = []

min_score = 999999999999999999999999999999999999999999
for pos, score in checked_positions.items():
    if pos[:2] == end:
        to_check.append(pos)
        min_score = min(min_score, score)
print(min_score)

while to_check:
    to_check_next = []
    for pos in to_check:
        in_short_path.add((x, y))
        x, y, d = pos
        for neighbour in backwards_neighbours(x, y, d):
            if neighbour not in checked_positions:
                continue
            if neighbour[2] != pos[2] and (
                checked_positions[pos] == checked_positions[neighbour] + 50
            ):
                to_check_next.append(neighbour)
            if neighbour[2] == pos[2] and (
                checked_positions[pos] == checked_positions[neighbour] + 1
            ):
                to_check_next.append(neighbour)
    to_check = to_check_next
print(in_short_path)
print(len(in_short_path))
