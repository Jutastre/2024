import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")
ymax = len(data)
xmax = len(data[0])
obstacles = []
guard = None
for y, row in enumerate(data):
    for x, char in enumerate(row):
        match char:
            case "#":
                obstacles.append((x, y))
            case "^":
                guard = [x, y, 0]


def step_guard(guard, obstacles):
    x, y, orientation = guard
    match orientation:
        case 0:
            target = (x, y - 1)
        case 1:
            target = (x + 1, y)
        case 2:
            target = (x, y + 1)
        case 3:
            target = (x - 1, y)
    if any([target[0] < 0, target[1] < 0, target[0] >= xmax, target[1] >= ymax]):
        return None
    if target in obstacles:
        return x, y, (orientation + 1) % 4
    else:
        return target[0], target[1], orientation

possible_loops = 0

for new_obstacle_x,new_obstacle_y in itertools.product(range(xmax),range(ymax)):
    temp_obstacles = [(new_obstacle_x,new_obstacle_y)] + obstacles
    temp_guard = guard
    previous_positions = set()

    while temp_guard != None:
        previous_positions.add(tuple(temp_guard))
        temp_guard = step_guard(temp_guard,temp_obstacles)
        if temp_guard in previous_positions:
            possible_loops += 1
            break

print(possible_loops)
