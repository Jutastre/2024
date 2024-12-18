import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split('\n')

hmap = [[int(n) for n in row] for row in data_string]

xmax = len(hmap[0]) - 1
ymax = len(hmap) - 1


def neighbours(coords):
    x, y = coords
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1
    return


def in_range(coords):
    x, y = coords
    if x < 0 or x > xmax:
        return False
    if y < 0 or y > ymax:
        return False
    return True

def at(coords,hmap):
    x, y = coords
    return hmap[y][x]

def count_paths(start_x, start_y, hmap):
    height = hmap[start_y][start_x]
    start = (start_x, start_y)
    # checked = set()
    paths = [[start]]
    for _ in range(9):
        paths_next = []
        for path in paths:
            for next_step in neighbours(path[-1]):
                if in_range(next_step) and at(path[-1],hmap) + 1 == at(next_step,hmap):
                    paths_next.append(path + [next_step])
        paths = paths_next
    path_count = 0
    for path in paths:
        if at(path[-1],hmap) == 9:
            path_count += 1
    return path_count


path_sum = 0

for start_y, row in enumerate(hmap):
    for start_x, height in enumerate(row):
        if height == 0:
            path_sum += count_paths(start_x, start_y, hmap)

print(f"Answer: {path_sum}")
