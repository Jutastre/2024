FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n")

result_sum = 0

for row in data:
    result_target = int(row.split(": ")[0])
    operands = [int(n) for n in row.split(": ")[1].split(" ")]
    possible_values = [operands[0]]
    for right_operand in operands[1:]:
        new_possible_values = []
        for left_operand in possible_values:
            new_possible_values.append(left_operand + right_operand)
            new_possible_values.append(left_operand * right_operand)
        possible_values = new_possible_values
    if result_target in possible_values:
        result_sum += result_target

print(result_sum)
