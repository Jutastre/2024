import itertools
import copy

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")


controlpad = {'^':(1,0),'A':(2,0),'<':(0,1),'v':(1,1),'>':(2,1)}
numpad = {
    '7':(0,0),
    '8':(1,0),
    '9':(2,0),
    '4':(0,1),
    '5':(1,1),
    '6':(2,1),
    '1':(0,2),
    '2':(1,2),
    '3':(2,2),
    '0':(1,3),
    'A':(2,3)}

def panic(x,y):
    print(f"PANIC PANIC PANIC")
    print(f"{x=} {y=}")
    input()

def calculate_commands(target_sequence:str,pad:dict):
    x,y = pad['A']
    output_sequence = ''
    for button in target_sequence:
        tx,ty = pad[button]
        if x == 0:
            while x > tx:
                output_sequence += '<'
                x -= 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while x < tx:
                output_sequence += '>'
                x += 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while y > ty:
                output_sequence += '^'
                y -= 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while y < ty:
                output_sequence += 'v'
                y += 1
                if (x,y) not in pad.values():
                    panic(x,y)
        else:
            while y < ty:
                output_sequence += 'v'
                y += 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while y > ty:
                output_sequence += '^'
                y -= 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while x > tx:
                output_sequence += '<'
                x -= 1
                if (x,y) not in pad.values():
                    panic(x,y)
            while x < tx:
                output_sequence += '>'
                x += 1
                if (x,y) not in pad.values():
                    panic(x,y)
        output_sequence += 'A'
    return output_sequence

complexity_sum = 0
for row in data:

    door_sequence = calculate_commands(row, numpad)
    control_sequence_1 = calculate_commands(door_sequence, controlpad)
    control_sequence_2 = calculate_commands(control_sequence_1, controlpad)
    complexity = len(control_sequence_2) * int(row[:-1])
    complexity_sum += complexity
    print(f"{len(control_sequence_2) =}")
    print(f"          {int(row[:-1]) =}")
    print(f"                         {complexity =}")

print(f"Answer: {complexity_sum}")
