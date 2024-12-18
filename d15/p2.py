import itertools
import copy

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split("\n\n")

room = []
for y, row in enumerate(data_string[0].split("\n")):
    row = row.replace("#","##")
    row = row.replace("O","[]")
    row = row.replace(".","..")
    row = row.replace("@","@.")
    room_row = []
    for x, char in enumerate(row):
        if char == "@":
            room_row.append(".")
            robot = (x, y)
        else:
            room_row.append(char)
    room.append(room_row)

moves = ""


def add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


for row in data_string[1].split("\n"):
    moves += row

for move in moves:
    pass

def do_move(robot,room,move):
    new_room = copy.deepcopy(room)
    match move:
        case "^":
            direction = (0, -1)
        case "v":
            direction = (0, +1)
        case "<":
            direction = (-1, 0)
        case ">":
            direction = (+1, 0)
    stack_size = 0
    target = add(robot, direction)
    total_boxes_to_push = []
    boxes_to_push = []
    if direction[1] != 0:
        if room[target[1]][target[0]] == "#":
            return False, robot
        if room[target[1]][target[0]] == "[":
            boxes_to_push.append(target)
        if room[target[1]][target[0]] == "]":
            boxes_to_push.append(add(target, (-1,0)))
        # collision = False
        while boxes_to_push:
            new_boxes_to_push = []
            for box in boxes_to_push:
                total_boxes_to_push.append(box)
                targets = [add(box,(0,direction[1])),add(box,(1,direction[1]))]
                for target in targets:
                    match room[target[1]][target[0]]:
                        case "#":
                            return False, robot
                        case  "[":
                            new_boxes_to_push.append(target)
                        case  "]":
                            if add(target, (-1,0)) not in new_boxes_to_push:
                                new_boxes_to_push.append(add(target, (-1,0)))
            boxes_to_push = new_boxes_to_push
        for box in total_boxes_to_push:
            new_room[box[1]][box[0]] = '.'
            new_room[box[1]][box[0] + 1] = '.'
        for box in total_boxes_to_push:
            target = add(box,(0,direction[1]))
            new_room[target[1]][target[0]] = '['
            new_room[target[1]][target[0] + 1] = ']'
        robot = add(robot, direction)
        # new_room[robot[1]][robot[0]] = "."
        return new_room, robot
    if direction[0] != 0:
        target = add(robot, direction)
        while room[target[1]][target[0]] != '.':
            if room[target[1]][target[0]] == '#':
                return False, robot
            target = add(target, direction)
        target = add(robot, direction)
        last_ch = room[target[1]][target[0]]
        while last_ch != '.':
            target = add(target, direction)
            temp_ch = room[target[1]][target[0]]
            room[target[1]][target[0]] = last_ch
            last_ch = temp_ch
            # target = add(target, direction)
        #room[target[1]][target[0]] = "O"
        robot = add(robot, direction)
        room[robot[1]][robot[0]] = "."
        return room, robot
def print_room(room, robot):
    room = copy.deepcopy(room)
    room[robot[1]][robot[0]] = '@'
    for y, row in enumerate(room):
        for x, char in enumerate(row):
            print(char, end="")
            # if char == 'O':
            #     gps_sum += (100 * y) + x
        print("")

for move in moves:
    room_after_move = do_move(robot,room,move)
    if room_after_move[0]:
        room,robot = room_after_move
    #print(f"move: {move}")
print_room(room,robot)

gps_sum = 0

for y,row in enumerate(room):
    for x,char in enumerate(row):
        if char == '[':
            gps_sum += (y*100) + x

print(f"Answer: {gps_sum}")
