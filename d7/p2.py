FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")

result_sum = 0


def find_possibilities(number_list):
    possible_values = [number_list[0]]
    for right_operand in number_list[1:]:
        new_possible_values = []
        for left_operand in possible_values:
            new_possible_values.append(left_operand + right_operand)
            new_possible_values.append(left_operand * right_operand)
            new_possible_values.append(int(str(left_operand) + str(right_operand)))
        possible_values = new_possible_values
    return possible_values


for row in data:
    result_target = int(row.split(": ")[0])
    operands = [int(n) for n in row.split(": ")[1].split(" ")]
    possible_values = find_possibilities(operands)
    if result_target in possible_values:
        result_sum += result_target

print(result_sum)
