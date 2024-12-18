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

end_positions = []

for x, y, xv, yv in robots:
    x = (x + (xv * seconds_to_simulate)) % room_size_x
    y = (y + (yv * seconds_to_simulate)) % room_size_y
    end_positions.append((x, y))

q1, q2, q3, q4 = 0, 0, 0, 0

for x, y in end_positions:
    if x <= (room_size_x // 2) - 1 and y <= (room_size_y // 2) - 1:
        q1 += 1
    elif x >= (room_size_x // 2) + 1 and y <= (room_size_y // 2) - 1:
        q2 += 1
    elif x <= (room_size_x // 2) - 1 and y >= (room_size_y // 2) + 1:
        q3 += 1
    elif x >= (room_size_x // 2) + 1 and y >= (room_size_y // 2) + 1:
        q4 += 1

answer = q1 * q2 * q3 * q4

print(f"Answer: {answer}")
