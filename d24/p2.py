import itertools
import copy
import sys
import tqdm
import random

sys.setrecursionlimit(50)
random.seed()
FILENAME = "in.txt"
BIG_NUMBER = 2**45

# dbj z16 ; qqp jcd ; z36 fhv
# known_swaps = [("fjh", "qff"), ("dbj", "z16"), ("qqp", "jcd"), ("z36", "fhv")]
# known_swaps = [("x00","fjh")]


# qff, qnw

# known_swaps = [("qff","qnw"),("dbj","z16"),("qqp","z23"),("z36","fbq")]
known_swaps = [("qff","qnw"),("dbj","z16"),("qqp","z23")]


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")
gates = {}
for row in data[0].split("\n"):
    gate2, value = row.split(": ")
    value = int(value)
    gates[gate2] = ("ABS", value)

for row in data[1].split("\n"):
    op1, operator, op2, _, gate2 = row.split()
    gates[gate2] = (operator, (op1, op2))


def get_gate_value(gate, gates):
    operator, value = gates[gate]
    match operator:
        case "ABS":
            return value
        case "XOR":
            return_value = get_gate_value(value[0], gates) ^ get_gate_value(
                value[1], gates
            )
            gates[gate] = ("ABS", return_value)
            return return_value
        case "AND":
            return_value = get_gate_value(value[0], gates) & get_gate_value(
                value[1], gates
            )
            gates[gate] = ("ABS", return_value)
            return return_value
        case "OR":
            return_value = get_gate_value(value[0], gates) | get_gate_value(
                value[1], gates
            )
            gates[gate] = ("ABS", return_value)
            return return_value


def set_x(num: int, gates: dict):
    x_gates = sorted([gate for gate in gates.keys() if gate[0] == "x"], reverse=False)
    binary = []
    while num:
        binary.append(num % 2)
        num //= 2
    while len(binary) < len(x_gates):
        binary.append(0)
    for gate, value in zip(x_gates, binary):
        gates[gate] = ("ABS", value)


def set_y(num: int, gates: dict):
    y_gates = sorted([gate for gate in gates.keys() if gate[0] == "y"], reverse=False)
    binary = []
    while num:
        binary.append(num % 2)
        num //= 2
    while len(binary) < len(y_gates):
        binary.append(0)
    for gate, value in zip(y_gates, binary):
        gates[gate] = ("ABS", value)


def get_z(gates: dict):
    z_gates = sorted([gate for gate in gates.keys() if gate[0] == "z"], reverse=False)
    binary = []
    for gate in z_gates:
        binary.append(str(get_gate_value(gate, gates)))
    result1 = int("".join(reversed(binary)), base=2)
    return result1


def test_addition(x: int, y: int, gates):
    copied_gates = copy.deepcopy(gates)
    set_x(x, copied_gates)
    set_y(y, copied_gates)
    try:
        result = get_z(copied_gates)
    except RecursionError:
        return None
    return result


def find_correct_bits(minimum_bits: int, gates):
    for n in range(max(minimum_bits,1), 45):
        # print(f"testing with {n=}")
        test_number = 2**n
        test_result1 = test_addition(test_number, 0, gates)
        test_result2 = test_addition(0, test_number, gates)
        expected_result = test_number
        # print(f"{expected_result=}    {test_result1=}    {test_result2=}")
        if test_result1 != expected_result or test_result1 != test_result2:
            return n-1
        test_number = (2 ** (n + 1)) - 1
        test_result1 = test_addition(test_number, 0, gates)
        test_result2 = test_addition(0, test_number, gates)
        expected_result = test_number
        # print(f"{expected_result=}    {test_result1=}    {test_result2=}")
        if test_result1 != expected_result or test_result1 != test_result2:
            return n-1
        if n == 1:
            if test_addition(0,0,gates) != 0:
                return 0
            if test_addition(1,0,gates) != 1:
                return 0
            if test_addition(0,1,gates) != 1:
                return 0
            if test_addition(1,1,gates) == 2:
                continue
        else:
            num = int("1" * (n-1),base = 2)
            if test_addition(num, num, gates) != num+num:
                return n-1
        for m in range(5):
            random_number = random.randint(0, BIG_NUMBER)
            as_binary = f"{random_number:b}"
            cropped = as_binary[-(n - 1) :]
            test_number = int(cropped, base=2)
            test_result1 = test_addition(test_number, 0, gates)
            test_result2 = test_addition(0, test_number, gates)
            expected_result = test_number
            # print(f"{expected_result=}    {test_result1=}    {test_result2=}")
            if test_result1 != expected_result or test_result1 != test_result2:
                return n-1
    print(f"{swap1=};{swap2=}")
    raise Exception("NOTHING WRONG EXCEPTION")


# result = test_addition(0b111,0,gates)
# binary_result = f"{result:050b}"
# print(binary_result)

for swap1, swap2 in known_swaps:
    gates[swap1], gates[swap2] = gates[swap2], gates[swap1]

random.seed()
for n in range(1000):
    number1 = random.randint(0, 2**min(n,44))
    number2 = random.randint(0, 2**min(n,44))
    result = test_addition(number1, number2, gates)
    if number1 + number2 != result:
        print(f"{number1=}, {number2=}, {result=}, {n=}")
        break
else:
    print("all checks out")
    quit()
# ---------- GOOD SHIT:
gates_backup = copy.deepcopy(gates)
best_pair = [find_correct_bits(0,gates), None, None]
for swap1, swap2 in tqdm.tqdm(itertools.combinations(gates, 2), total=(len(gates) ** 2)//2):
    better_than_nothing = False
    gates = copy.deepcopy(gates_backup)
    gates[swap1], gates[swap2] = gates[swap2], gates[swap1]
    # gates[swap3], gates[swap4] = gates[swap4], gates[swap3]
    correct_bits = find_correct_bits(best_pair[0], gates)
    if correct_bits > best_pair[0]:
        best_pair = [correct_bits, swap1, swap2]
        better_than_nothing = True
        print(f"better pair found : {best_pair=}")
        print(f"better pair found : {best_pair=}")
        print(f"better pair found : {best_pair=}")
    elif better_than_nothing and correct_bits == best_pair[0]:
        print(f"match found : {swap1=} {swap2=}")
        print(f"match found : {swap1=} {swap2=}")
        print(f"match found : {swap1=} {swap2=}")

# -----

