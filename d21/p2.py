import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def calculate_numpad_commands(target_sequence: str):
    x = 2
    y = 3
    output_sequence = []
    for button in target_sequence:
        match button:
            case "7":
                tx = 0
                ty = 0
            case "8":
                tx = 1
                ty = 0
            case "9":
                tx = 2
                ty = 0
            case "4":
                tx = 0
                ty = 1
            case "5":
                tx = 1
                ty = 1
            case "6":
                tx = 2
                ty = 1
            case "1":
                tx = 0
                ty = 2
            case "2":
                tx = 1
                ty = 2
            case "3":
                tx = 2
                ty = 2
            case "0":
                tx = 1
                ty = 3
            case "A":
                tx = 2
                ty = 3
        if x == tx:
            if y > ty:
                output_sequence.append("^" * (y - ty))
            else:
                output_sequence.append("v" * (ty - y))
        elif y == ty:
            if x > tx:
                output_sequence.append("<" * (x - tx))
            else:
                output_sequence.append(">" * (tx - x))
        elif y == 3 and tx == 0:
            output_sequence.append(("^" * (y - ty)) + ("<" * (x - tx)))
        elif x == 0 and ty == 3:
            output_sequence.append((">" * (tx - x)) + ("v" * (ty - y)))
        # "normal" case:
        else:
            if tx < x:
                output_sequence.append("<" * (x - tx))
            if ty < y:
                output_sequence.append("^" * (y - ty))
            if ty > y:
                output_sequence.append("v" * (ty - y))
            if tx > x:
                output_sequence.append(">" * (tx - x))

        output_sequence.append("A")
        x = tx
        y = ty
    return "".join(output_sequence)

memo = {}

def calculate_arrow_command_length(target_sequence: str, depth: int):
    if depth < 1:
        return len(target_sequence)
    x = 2
    y = 0
    if (target_sequence,depth) in memo:
        return memo[(target_sequence,depth)]
    target_output = []
    for button in target_sequence:
        match button:
            case "^":
                tx = 1
                ty = 0
            case "A":
                tx = 2
                ty = 0
            case "<":
                tx = 0
                ty = 1
            case "v":
                tx = 1
                ty = 1
            case ">":
                tx = 2
                ty = 1
        if x == tx:
            if y > ty:
                target_output.append("^" * (y - ty))
            else:
                target_output.append("v" * (ty - y))
        elif y == ty:
            if x > tx:
                target_output.append("<" * (x - tx))
            else:
                target_output.append(">" * (tx - x))
        elif x == 0 and ty == 0:
            target_output.append((">" * (tx - x)) + "^")
        elif y == 0 and tx == 0:
            target_output.append("v" + ("<" * (x - tx)))
        # "normal" case:
        else:
            if tx < x:
                target_output.append("<" * (x - tx))
            if ty < y:
                target_output.append("^" * (y - ty))
            if ty > y:
                target_output.append("v" * (ty - y))
            if tx > x:
                target_output.append(">" * (tx - x))

        target_output.append("A")
        x = tx
        y = ty
    target_result = "".join(target_output)

    if depth > 1:
        sequence_to_split = target_result.replace("A","AB").split("B")
        total_output = []
        for subsequence in sequence_to_split:
            total_output.append(calculate_arrow_command_length(subsequence, depth-1))
        final_sum = sum(total_output)
    else:
        final_sum = len(target_result)
    memo[(target_sequence,depth)] = final_sum
    return final_sum

def bot_it_more(sequence):

    control_sequence = calculate_numpad_commands(sequence)
    answer = calculate_arrow_command_length(control_sequence, depth = 25)
    return answer



complexity_sum = 0
for row in data:
    sequence_length = bot_it_more(row)
    print(sequence_length)
    complexity = sequence_length * int(row[:-1])
    print(f"{sequence_length} * {int(row[:-1])} = {complexity}")
    complexity_sum += complexity
    print(f"{int(row[:-1]) =}")
    print(f"{complexity =}")

print(f"Answer: {complexity_sum}")
