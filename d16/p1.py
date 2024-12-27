import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip()

map = data_string.split("\n")

xmax = len(map[0]) - 1
ymax = len(map) - 1

for y,row in enumerate(map):
    for x,char in enumerate(row):
        if char == 'S':
            start =(x,y,1)
        if char == 'E':
            end =(x,y)

def neighbours(x,y,d):
    yield (x,y,(d-1) % 4)
    yield (x,y,(d+1) % 4)
    match d:
        case 0:
            potential =(x,y-1,d)
        case 1:
            potential =(x+1,y,d)
        case 2:
            potential =(x,y+1,d)
        case 3:
            potential =(x-1,y,d)
    x,y,d = potential
    if x < 0 or x > xmax or y < 0 or y > ymax:
        return
    if map[y][x] == '#':
        return
    yield potential

to_check = [start]
checked_positions = {start:0}
updated_something = True
while updated_something:
    to_check_next = []
    updated_something = False
    for position in to_check:
        x,y,d = position
        score = checked_positions[position]
        for neighbour in neighbours(x,y,d):
            if d == neighbour[2]:
                target_score = score + 1
            else:
                target_score = score + 1000
            if neighbour not in checked_positions or checked_positions[neighbour] > target_score:
                checked_positions[neighbour] = target_score
                updated_something = True
                to_check_next.append(neighbour)
    to_check = to_check_next

min_score = 999999999999999999999999999999999999999999
for pos,score in checked_positions.items():
    if pos[:2] == end:
        min_score = min(min_score, score)
print(min_score)