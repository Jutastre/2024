import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split('\n')

grid = [[ch for ch in row] for row in data_string]

xmax = len(grid[0]) - 1
ymax = len(grid) - 1

def in_range(x,y):
    if x < 0 or x > xmax:
        return False
    if y < 0 or y > ymax:
        return False
    return True

def neighbours(coords):
    x,y = coords
    yield (x+1,y)
    yield (x-1,y)
    yield (x,y+1)
    yield (x,y-1)
    return

areas = {}
perimeters:dict[str,set] = {}

def preprocess(grid):
    id_incrementer = 0
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if not isinstance(ch, str):
                continue
            to_replace = ch
            to_check = [(x,y)]
            checked = set()
            grid[y][x] = id_incrementer
            while to_check:
                check_next = []
                for point in to_check:
                    for nx,ny in neighbours(point):
                        if (nx,ny) not in checked and in_range(nx,ny) and grid[ny][nx] == to_replace:
                            grid[ny][nx] = id_incrementer
                            checked.add((nx,ny))
                            check_next.append((nx,ny))
                to_check = check_next
            id_incrementer += 1


preprocess(grid)

for y,row in enumerate(grid):
    for x,ch in enumerate(row):
        coords = (x,y)
        if ch not in areas:
            areas[ch] = 0
            perimeters[ch] = set()
        areas[ch] += 1
        for neighbour in neighbours(coords):
            nx,ny = neighbour
            if not in_range(nx,ny) or grid[ny][nx] != ch:
                #areas[ch] += 1
                if nx > x:
                    perimeters[ch].add((x,y,'e'))
                if nx < x:
                    perimeters[ch].add((x,y,'w'))
                if ny > y:
                    perimeters[ch].add((x,y,'s'))
                if ny < y:
                    perimeters[ch].add((x,y,'n'))

perimeter_counts = {}

for ch,perims in perimeters.items():
    perimeter_counts[ch] = 0
    while perims:
        piece = perims.pop()
        x,y,direction = piece
        match direction:
            case 'e'|'w':
                while (next:=(x,y-1,direction)) in perims:
                    perims.remove(next)
                    y -= 1
                x,y,direction = piece
                while (next:=(x,y+1,direction)) in perims:
                    perims.remove(next)
                    y += 1
            case 's'|'n':
                while (next:=(x-1,y,direction)) in perims:
                    perims.remove(next)
                    x -= 1
                x,y,direction = piece
                while (next:=(x+1,y,direction)) in perims:
                    perims.remove(next)
                    x += 1
        perimeter_counts[ch] += 1




answer = sum(perimeter_counts[ch] * areas[ch] for ch in areas.keys())

print(f"Answer: {answer}")
