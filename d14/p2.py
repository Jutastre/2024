import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split("\n")

if FILENAME == "tin.txt":
    room_size_x = 11
    room_size_y = 7
else:
    room_size_x = 101
    room_size_y = 103
seconds_to_simulate = 100

robots = []
for row in data_string:
    p1, p2 = (piece[2:] for piece in row.split(" "))
    x, y = (int(n) for n in p1.split(","))
    xv, yv = (int(n) for n in p2.split(","))
    robots.append((x, y, xv, yv))

def simulate(robots, seconds_to_simulate):


    end_positions = []

    for x, y, xv, yv in robots:
        x = (x + (xv * seconds_to_simulate)) % room_size_x
        y = (y + (yv * seconds_to_simulate)) % room_size_y
        end_positions.append((x, y))
    return end_positions

for seconds in range(52,40000, 258-52):
    end_positions = simulate(robots, seconds)
    print(f"{seconds} seconds simulated:")
    for y in range(room_size_y):
        for x in range(room_size_x):
            count = end_positions.count((x,y))
            count = str(count) if count else '.'
            print(f"{count:2}", end='')
        print("")
    input("")

# print(f"Answer: {answer}")
