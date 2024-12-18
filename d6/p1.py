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
    match orientation % 4:
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
        return x, y, orientation + 1
    else:
        return target[0], target[1], orientation

walked_places = set()

while guard != None:
    walked_places.add((guard[0],guard[1]))
    guard = step_guard(guard,obstacles)


print(len(walked_places))
