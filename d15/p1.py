import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split("\n\n")

room = []
for y, row in enumerate(data_string[0].split("\n")):
    room_row = []
    for x, char in enumerate(row):
        if char == "@":
            room_row.append(".")
            robot = (x, y)
        else:
            room_row.append(char)
    room.append(room_row)

moves = ""


def add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


for row in data_string[1].split("\n"):
    moves += row

for move in moves:
    match move:
        case "^":
            direction = (0, -1)
        case "v":
            direction = (0, +1)
        case "<":
            direction = (-1, 0)
        case ">":
            direction = (+1, 0)
    stack_size = 0
    target = add(robot, direction)
    while room[target[1]][target[0]] == "O":
        stack_size += 1
        target = add(target, direction)
    if room[target[1]][target[0]] == "#":
        continue
    room[target[1]][target[0]] = "O"
    robot = add(robot, direction)
    room[robot[1]][robot[0]] = "."

gps_sum = 0

for y, row in enumerate(room):
    for x, char in enumerate(row):
        print(char, end="")
        if char == 'O':
            gps_sum += (100 * y) + x
    print("")

print(f"Answer: {gps_sum}")
