import itertools
import copy

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class numpad_robot:
    def __init__(self):
        self.x = 2
        self.y = 3

    def calculate_commands(self, target_sequence: str):
        output_sequences = [""]
        for button in target_sequence:
            button_sequences = []
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
            button_subsequences = []
            if self.x != tx:
                if self.x < tx:
                    button = ">"
                else:
                    button = "<"
                count = abs(self.x - tx)
                button_subsequences.append(button * count)
            if self.y != ty:
                if self.y < ty:
                    button = "v"
                else:
                    button = "^"
                count = abs(self.y - ty)
                button_subsequences.append(button * count)

            if len(button_subsequences) == 0:
                button_sequences.append("A")
            elif len(button_subsequences) == 1:
                button_sequences.append(button_subsequences[0] + "A")
            else:
                button_sequences.append(button_subsequences[0] + button_subsequences[1] + "A")
                button_sequences.append(button_subsequences[1] + button_subsequences[0] + "A")
            new_output_sequences = []
            for previous_sequence in output_sequences:
                for button_sequence in button_sequences:
                    new_output_sequences.append(previous_sequence + button_sequence)
            output_sequences = new_output_sequences
            self.x = tx
            self.y = ty
        return output_sequences


class control_robot:
    button_positions = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}

    def __init__(self):
        self.x = 2
        self.y = 0

    def calculate_commands(self, target_sequences: str):
        total_output_sequences = []
        for target_sequence in target_sequences:
            output_sequences = [""]
            for button in target_sequence:
                button_sequences = []
                tx,ty = control_robot.button_positions[button]
                button_subsequences = []
                if self.x != tx:
                    if self.x < tx:
                        button = ">"
                    else:
                        button = "<"
                    count = abs(self.x - tx)
                    button_subsequences.append(button * count)
                if self.y != ty:
                    if self.y < ty:
                        button = "v"
                    else:
                        button = "^"
                    count = abs(self.y - ty)
                    button_subsequences.append(button * count)

                if len(button_subsequences) == 0:
                    button_sequences.append("A")
                elif len(button_subsequences) == 1:
                    button_sequences.append(button_subsequences[0] + "A")
                else:
                    button_sequences.append(button_subsequences[0] + button_subsequences[1] + "A")
                    button_sequences.append(button_subsequences[1] + button_subsequences[0] + "A")
                new_output_sequences = []
                for previous_sequence in output_sequences:
                    for button_sequence in button_sequences:
                        new_output_sequences.append(previous_sequence + button_sequence)
                output_sequences = new_output_sequences
                self.x = tx
                self.y = ty
            total_output_sequences += output_sequences
        return total_output_sequences


complexity_sum = 0
for row in data:
    door_robot = numpad_robot()
    control_robot_1 = control_robot()
    control_robot_2 = control_robot()

    door_sequences = door_robot.calculate_commands(row)
    control_sequences_1 = control_robot_1.calculate_commands(door_sequences)
    control_sequences_2 = control_robot_2.calculate_commands(control_sequences_1)
    minimum_length = min((len(sequence) for sequence in control_sequences_2))
    complexity = minimum_length * int(row[:-1])
    complexity_sum += complexity
    print(f"{minimum_length =}")
    print(f"{int(row[:-1]) =}")
    print(f"{complexity =}")

print(f"Answer: {complexity_sum}")
