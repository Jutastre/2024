import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")

antennas = {}
ymax = len(data) - 1
xmax = len(data[0]) - 1
max_range = max(xmax,ymax)
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == ".":
            continue
        if char not in antennas:
            antennas[char] = []
        antennas[char].append((x, y))
antinodes = []
for frequency in antennas.values():
    for a1, a2 in itertools.combinations(frequency, 2):
        dx, dy = (a1[0] - a2[0], a1[1] - a2[1])
        for divisor in range(1, max(dx, dy) + 1):
            if ((dx / divisor) % 1 == 0) and ((dy / divisor) % 1 == 0):
                dx = dx // divisor
                dy = dy // divisor
                break
        for multiplier in range(-max_range,max_range): # 
            antinodes.append((a1[0] + dx * multiplier, a1[1] + dy * multiplier))


def in_range(antinode):
    if antinode[0] < 0:
        return False
    if antinode[0] > xmax:
        return False
    if antinode[1] < 0:
        return False
    if antinode[1] > ymax:
        return False
    return True


unique_antinodes_in_range = set(
    antinode for antinode in antinodes if in_range(antinode)
)
# print(unique_antinodes_in_range)
print(len(unique_antinodes_in_range))
