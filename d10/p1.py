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


def count_paths(start_x, start_y, hmap):
    height = hmap[start_y][start_x]
    start = (start_x, start_y)
    checked = set()
    to_check = [start]
    while to_check:
        check_next = []
        for point in to_check:
            checked.add(point)
            check_next += [
                neighbour
                for neighbour in neighbours(point)
                if (
                    in_range(neighbour)
                    and neighbour not in checked
                    and hmap[neighbour[1]][neighbour[0]] == height + 1
                )
            ]
        to_check = check_next
        height += 1
    path_count = 0
    for point in checked:
        if hmap[point[1]][point[0]] == 9:
            path_count += 1
    return path_count


path_sum = 0

for start_y, row in enumerate(hmap):
    for start_x, height in enumerate(row):
        if height == 0:
            path_sum += count_paths(start_x, start_y, hmap)

print(f"Answer: {path_sum}")
