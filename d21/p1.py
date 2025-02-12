import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class numpad_robot:
    def __init__(self):
        self.x = 2
        self.y = 3

    def calculate_commands(self, target_sequence: str):
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
            if self.x == tx:
                if self.y > ty:
                    output_sequence.append("^" * (self.y - ty))
                else:
                    output_sequence.append("v" * (ty - self.y))
            elif self.y == ty:
                if self.x > tx:
                    output_sequence.append("<" * (self.x - tx))
                else:
                    output_sequence.append(">" * (tx - self.x))
            elif self.y == 3 and tx == 0:
                output_sequence.append(("^" * (self.y - ty)) + ("<" * (self.x - tx)))
            elif self.x == 0 and ty == 3:
                output_sequence.append((">" * (tx - self.x)) + ("v" * (ty - self.y)))
            # "normal" case:
            else:
                if tx < self.x:
                    output_sequence.append("<" * (self.x - tx))
                if ty < self.y:
                    output_sequence.append("^" * (self.y - ty))
                if ty > self.y:
                    output_sequence.append("v" * (ty - self.y))
                if tx > self.x:
                    output_sequence.append(">" * (tx - self.x))

            output_sequence.append("A")
            self.x = tx
            self.y = ty
        return "".join(output_sequence)
    
class arrow_robot:
    def __init__(self):
        self.x = 2
        self.y = 0

    def calculate_commands(self, target_sequence: str, debug = False):
        output_sequence = []
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
            if self.x == tx:
                if self.y > ty:
                    output_sequence.append("^" * (self.y - ty))
                else:
                    output_sequence.append("v" * (ty - self.y))
            elif self.y == ty:
                if self.x > tx:
                    output_sequence.append("<" * (self.x - tx))
                else:
                    output_sequence.append(">" * (tx - self.x))
            elif self.x == 0 and ty == 0:
                output_sequence.append((">" * (tx - self.x)) + "^")
            elif self.y == 0 and tx == 0:
                output_sequence.append("v" + ("<" * (self.x - tx)))
            # "normal" case:
            else:
                if tx < self.x:
                    output_sequence.append("<" * (self.x - tx))
                if ty < self.y:
                    output_sequence.append("^" * (self.y - ty))
                if ty > self.y:
                    output_sequence.append("v" * (ty - self.y))
                if tx > self.x:
                    output_sequence.append(">" * (tx - self.x))

            output_sequence.append("A")
            self.x = tx
            self.y = ty
        return "".join(output_sequence)

def doublebot_it(sequence):
    door_robot = numpad_robot()
    robot1 = arrow_robot()
    robot2 = arrow_robot()

    door_sequences = door_robot.calculate_commands(row)
    control_sequence_1 = robot1.calculate_commands(door_sequences, debug = True)
    control_sequence_2 = robot2.calculate_commands(control_sequence_1, debug = True)
    return control_sequence_2


complexity_sum = 0
for row in data:
    sequence = doublebot_it(row)
    print(sequence)
    complexity = len(sequence) * int(row[:-1])
    print(f"{len(sequence)} * {int(row[:-1])} = {complexity}")
    complexity_sum += complexity
    print(f"{int(row[:-1]) =}")
    print(f"{complexity =}")

print(f"Answer: {complexity_sum}")
