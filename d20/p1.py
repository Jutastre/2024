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


def map_track(map,start,end):
    track_points = {}
    to_check = [start]
    time_spent = 0
    while to_check:
        #print_mid_run(map, already_checked)
        to_check_next = []
        #if end in to_check:
            #return time_spent
        for point in to_check:
            if point not in track_points:
                track_points[point] = time_spent
            for tx, ty in neighbours(point):
                if (tx, ty) in track_points:
                    continue
                if ((tx, ty) not in to_check_next) and (map[ty][tx] != "#"):
                    to_check_next.append((tx, ty))
        to_check = to_check_next
        time_spent += 1
    return track_points


possible_cheat_starts = set()

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
                        possible_cheat_starts.add((tx, ty))

track_map = map_track(map, start, end)
original_race_time=track_map[end]
number_of_possible_cheats = len(possible_cheat_starts)

print(f"{original_race_time=}")
print(f"{number_of_possible_cheats=}")

good_cheats = 0

# cheat_register = {}
good_cheat_list = []
for idx, cheat in enumerate(possible_cheat_starts):
    #print(f"testing cheat #{idx+1}")
    copied_map = copy.deepcopy(map)
    cx, cy = cheat
    minimum_start_point_value = 999999999999
    minimum_start_point = None
    for cheat_step_2 in neighbours(cheat):
        if cheat_step_2 in track_map:
            for start_point in neighbours(cheat):
                if start_point is cheat_step_2:
                    continue
                if start_point in track_map and track_map[start_point] < minimum_start_point_value:
                    minimum_start_point = start_point
                    minimum_start_point_value = track_map[start_point]
            if not minimum_start_point:
                continue
            time_save = (track_map[cheat_step_2] - minimum_start_point_value) -2
            if time_save >= 100:
                good_cheats += 1
                good_cheat_list.append((cheat,cheat_step_2))




print(f"Answer: {good_cheats}")
