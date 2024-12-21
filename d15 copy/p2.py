import itertools
import copy

FILENAME = "in.txt"


with open(FILENAME) as f:
    map = f.read().strip().split("\n")

xmax = len(map[0]) - 1
ymax = len(map) - 1


def neighbours(coords):
    x, y = coords
    for neighbour in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
        nx, ny = neighbour
        if nx < 0 or nx > xmax or ny < 0 or ny > ymax:
            continue
        yield neighbour
    return

def print_mid_run(map, ran_points):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if (x,y) in ran_points:
                print("*", end = '')
            else:
                print(char, end = '')
        print("")

def run_race(map, start, end):
    already_checked = []
    to_check = [start]
    time_spent = 0
    while True:
        #print_mid_run(map, already_checked)
        time_spent += 1
        to_check_next = []
        if end in to_check:
            return time_spent
        for point in to_check:
            if point not in already_checked:
                already_checked.append(point)
            for tx, ty in neighbours(point):
                if (tx, ty) in already_checked:
                    continue
                if ((tx, ty) not in to_check_next) and (map[ty][tx] != "#"):
                    to_check_next.append((tx, ty))
        to_check = to_check_next


possible_cheats = set()

for y, row in enumerate(map):
    for x, char in enumerate(row):
        match char:
            case "E":
                end = (x, y)
            case "S" | ".":
                if char == "S":
                    start = (x, y)
                for tx, ty in neighbours((x, y)):
                    if map[ty][tx] == "#":
                        possible_cheats.add((tx, ty))

original_race_time = run_race(map, start, end)
number_of_possible_cheats = len(possible_cheats)

print(f"{original_race_time=}")
print(f"{number_of_possible_cheats=}")

good_cheats = 0

# cheat_register = {}

for idx, cheat in enumerate(possible_cheats):
    print(f"testing cheat #{idx+1}")
    copied_map = copy.deepcopy(map)
    cx, cy = cheat
    copied_map[cy] = copied_map[cy][:cx] + "." + copied_map[cy][cx + 1 :]
    cheated_time = run_race(copied_map, start, end)
    time_save = original_race_time - cheated_time
    # cheat_register[cheat] = time_save
    if time_save >= 100:
        good_cheats += 1


print(f"Answer: {good_cheats}")
