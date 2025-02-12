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

def calculate_arrow_commands(target_sequence: str, debug = False):
    x = 2
    y = 0
    total_output = []
    target_sequence.replace("A","A<delim>")
    for subsequence in target_sequence.split("<delim>"):
        if subsequence in memo:
            total_output.append(memo[subsequence])
            continue
        subsequence_output = []
        for button in subsequence:
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
                    subsequence_output.append("^" * (y - ty))
                else:
                    subsequence_output.append("v" * (ty - y))
            elif y == ty:
                if x > tx:
                    subsequence_output.append("<" * (x - tx))
                else:
                    subsequence_output.append(">" * (tx - x))
            elif x == 0 and ty == 0:
                subsequence_output.append((">" * (tx - x)) + "^")
            elif y == 0 and tx == 0:
                subsequence_output.append("v" + ("<" * (x - tx)))
            # "normal" case:
            else:
                if tx < x:
                    subsequence_output.append("<" * (x - tx))
                if ty < y:
                    subsequence_output.append("^" * (y - ty))
                if ty > y:
                    subsequence_output.append("v" * (ty - y))
                if tx > x:
                    subsequence_output.append(">" * (tx - x))

            subsequence_output.append("A")
            x = tx
            y = ty
        subsequence_result = "".join(subsequence_output)
        memo[subsequence] = subsequence_result
        total_output.append(subsequence_result)
    return "".join(total_output)

def doublebot_it(sequence):

    door_sequences = calculate_numpad_commands(row)
    control_sequence_1 = calculate_arrow_commands(door_sequences)
    control_sequence_2 = calculate_arrow_commands(control_sequence_1, debug = True)
    return control_sequence_2

def bot_it_more(sequence):

    control_sequence = calculate_numpad_commands(row)
    for bots in range(25):
        print(f"processing botlayer {bots}...")
        print(f"sequence length now {len(control_sequence)}")

        control_sequence = calculate_arrow_commands(control_sequence)
    return control_sequence



complexity_sum = 0
for row in data:
    sequence = bot_it_more(row)
    print(sequence)
    complexity = len(sequence) * int(row[:-1])
    print(f"{len(sequence)} * {int(row[:-1])} = {complexity}")
    complexity_sum += complexity
    print(f"{int(row[:-1]) =}")
    print(f"{complexity =}")

print(f"Answer: {complexity_sum}")
