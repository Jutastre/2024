import itertools
import copy

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")


controlpad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}
numpad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

print_lines = []


def print_or_panic(x: int, y: int, pad: dict, depth: int):
    if (x, y) not in pad.values():
        print(f"PANIC PANIC PANIC")
        print(f"{x=} {y=}")
        input()
        return
    return
    while len(print_lines) < 4:
        print_lines.append([])
    for line_idx in range(len(print_lines)):
        while len(print_lines[line_idx]) < ((depth + 1) * 4):
            print_lines[line_idx].append(" ")
    for k,v in pad.items():
        tx,ty = v
        if (tx,ty) == (x,y):
            print_lines[ty][(depth * 4) + tx] = f"\033[31;1;4m{k}\033[0m"
        else:
            print_lines[ty][(depth * 4) + tx] = k
        
    #print_lines[y][(depth * 4) + x] = "*"
    for row in print_lines:
        print("".join(row))
    #print("-----------------")
    #input()


def calculate_commands(target_sequence: str, pad: dict, depth: int):
    x, y = pad["A"]
    output_sequence = ""
    for button in target_sequence:
        tx, ty = pad[button]
        while x > tx:
            output_sequence += "<"
            x -= 1
        while x < tx:
            output_sequence += ">"
            x += 1
        while y < ty:
            output_sequence += "v"
            y += 1
        while y > ty:
            output_sequence += "^"
            y -= 1
        output_sequence += "A"
        #print("Hit!")
        #input()
    return output_sequence


complexity_sum = 0
for row in data:

    door_sequence = calculate_commands(row, numpad, 0)
    control_sequence_1 = calculate_commands(door_sequence, controlpad, 1)
    control_sequence_2 = calculate_commands(control_sequence_1, controlpad, 2)
    complexity = len(control_sequence_2) * int(row[:-1])
    complexity_sum += complexity
    print(f"{len(control_sequence_2) =}")
    print(f"          {int(row[:-1]) =}")
    print(f"                         {complexity =}")

print(f"Answer: {complexity_sum}")
