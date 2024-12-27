FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

program_string = data[4].split()[1]
program = [int(n) for n in program_string.split(",")]

reg_a = int(data[0].split()[-1])
reg_b = int(data[1].split()[-1])
reg_c = int(data[2].split()[-1])

# program = [2,6]

# reg_a = 0
# reg_b = 0
# reg_c = 9

prog_counter = 0

def decode_combo(literal_operand):
    if literal_operand == 4:
        return reg_a
    elif literal_operand == 5:
        return reg_b
    elif literal_operand == 6:
        return reg_c
    elif literal_operand < 4:
        return literal_operand
    else:
        return "ERROR!!!"

while prog_counter <= len(program) - 2:
    opcode = program[prog_counter]
    literal_operand = program[prog_counter + 1]
    if opcode == 0:
        reg_a = reg_a // (2**decode_combo(literal_operand))
    elif opcode == 1:
        reg_b = reg_b ^ literal_operand 
    elif opcode == 2:
        reg_b = decode_combo(literal_operand)    % 8
    elif opcode == 3:
        if reg_a != 0:
            prog_counter = literal_operand
            continue
    elif opcode == 4:
        reg_b = reg_b ^ reg_c
    elif opcode == 5:
        # print("")
        print(f"{decode_combo(literal_operand) % 8}", end = ',')
    elif opcode == 6:
        reg_b = reg_a // 2**decode_combo(literal_operand)
    elif opcode == 7:
        reg_c = reg_a // 2**decode_combo(literal_operand)
    prog_counter += 2
        

print("\nfinished!")
print(f"{reg_a = }, {reg_b = }, {reg_c = }")






        