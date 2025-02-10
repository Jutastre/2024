import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

program_string = data[4].split()[1]
program = [int(n) for n in program_string.split(",")]

reg_a = int(data[0].split()[-1])
reg_b = int(data[1].split()[-1])
reg_c = int(data[2].split()[-1])

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
    
def decode_combo_to_string(literal_operand):
    if literal_operand == 4:
        return "A"
    elif literal_operand == 5:
        return "B"
    elif literal_operand == 6:
        return "C"
    elif literal_operand < 4:
        return str(literal_operand)
    else:
        return "ERROR!!!"

print(program)
def run_program(program, register_a):
    output = []
    global reg_a
    global reg_b
    global reg_c
    reg_a = register_a
    reg_b = 0
    reg_c = 0
    prog_counter = 0
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
            output.append((decode_combo(literal_operand) % 8))
        elif opcode == 6:
            reg_b = reg_a // 2**decode_combo(literal_operand)
        elif opcode == 7:
            reg_c = reg_a // 2**decode_combo(literal_operand)
        prog_counter += 2
    return output
    # print("")
# print("---------")
# for opcode,operand in itertools.batched(program,2):
#     if opcode == 0:
#         print(f"A = A << {decode_combo_to_string(operand)})")
#     elif opcode == 1:
#         print(f"B = B xor {operand} ")
#     elif opcode == 2:
#         print(f"B = {decode_combo_to_string(operand)} % 8")
#     elif opcode == 3:
#         print(f"""if A != 0:
#     prog_counter = {operand}
#     continue""")
#     elif opcode == 4:
#         print("B = B xor C")
#     elif opcode == 5:
#         # print("")
#         print(f"print(f\"{{{decode_combo_to_string(operand)} % 8}}\", end = ',')")
#     elif opcode == 6:
#         print(f"B = A << {decode_combo_to_string(operand)}")
#     elif opcode == 7:
#         print(f"C = A << {decode_combo_to_string(operand)}")
#     prog_counter += 2

# print("\nfinished!")
# print(f"{reg_a = }, {reg_b = }, {reg_c = }")

def solution_to_value(solution):
    register_value = 0
    for n in ((solution)):
        register_value = register_value << 3
        register_value += n
    return register_value

solution = []

def recursive_test(partial_solution:list[int], program):
    output = run_program(program, solution_to_value(partial_solution))
    if len(partial_solution) > 0:
        for idx,n in enumerate(reversed(output)):
            if n != program[-idx - 1]:
                print(f"Wrong output ({partial_solution=})({output=})")
                return False
    if len(output) < len(program):
        for number_to_test in range(0,8):
            solution_to_test = [n for n in partial_solution] + [number_to_test]
            result = recursive_test(solution_to_test, program)
            if result:
                return result
    if len(output) == len(program):
        return partial_solution
    
    print("EOF")
    return False

# while len(solution) < len(program):
#     solution.append(0)
#     for number_to_test in range(0,8):
#         # if len(solution) == 1 and number_to_test == 0:
#         #     number_to_test = 2
#         solution[-1] = number_to_test
#         register_value = solution_to_value(solution)
#         output = run_program(program, register_value)
#         if output[0] == program[len(program) - len(solution)]:
#             break
solution = recursive_test([], program)
print(f"{solution=}")
print(f"{program=}")
if solution:
    print(f"{run_program(program, solution_to_value(solution))=}")
    print(solution_to_value(solution))