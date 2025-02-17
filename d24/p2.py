import itertools
import copy
import sys
import tqdm
import random

# import threading

sys.setrecursionlimit(150)
random.seed()
FILENAME = "in.txt"
MAX_BITS = 45
BIG_NUMBER = 2**MAX_BITS

RANDOM_NUMBER_COUNT = 4
PRECALCULATE_RANDOM = True
THREADS = 64
TARGET_BITS = 45

known_swaps = None

# ("qff", "qnw")
# ("dbj", "z16")
# match found : swap1='qqp' swap2='wdr'
# match found : swap1='jcd' swap2='dmw'

# known_swaps = [("qff","qnw"),("dbj","z16"),("qqp","z23"),("z36","fbq")]
# known_swaps = [("qff", "qnw"), ("dbj", "z16"), ("jcd", "dmw")]
# known_swaps = ["qff","qnw","dbj","z16","qqp","z23","z36","fbq"]
# known_swaps = ["z10","z09"]
known_swaps = ["qff","qnw","qcr","z16"]

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
        return 0
    return result


if PRECALCULATE_RANDOM:
    random_numbers = [random.randint(0, BIG_NUMBER) for _ in range(RANDOM_NUMBER_COUNT)]
    print(f"random numbers:")
    for number in random_numbers:
        print(number)


def find_correct_bits(minimum_bits: int, gates):
    for n in range(max(minimum_bits, 1), MAX_BITS + 1):
        # print(f"testing with {n=}")
        modulo = 2 ** (n + 1)
        test_result1 = test_addition(0, 0, gates) % modulo
        if test_result1 != 0:
            return n - 1
        test_number = 2 ** (n - 1)
        test_result1 = test_addition(test_number, 0, gates) % modulo
        test_result2 = test_addition(0, test_number, gates) % modulo
        test_result3 = test_addition(test_number, test_number, gates) % modulo
        expected_result = test_number
        if (
            test_result1 != expected_result
            or test_result1 != test_result2
            or test_result3 != (test_number * 2)
        ):
            return n - 1

        test_number = (2**n) - 1
        test_result1 = test_addition(test_number, 0, gates) % modulo
        test_result2 = test_addition(0, test_number, gates) % modulo
        test_result3 = test_addition(test_number, test_number, gates) % modulo
        expected_result = test_number
        if (
            test_result1 != expected_result
            or test_result1 != test_result2
            or test_result3 != (test_number * 2)
        ):
            return n - 1
        if n == 1:
            if test_addition(0, 0, gates) % modulo != 0:
                return 0
            if test_addition(1, 0, gates) % modulo != 1:
                return 0
            if test_addition(0, 1, gates) % modulo != 1:
                return 0
            if test_addition(1, 1, gates) % modulo == 0:
                continue
        else:
            num = int("0" + ("1" * (n - 1)), base=2)
            if test_addition(num, num, gates) % modulo != num + num:
                return n - 1
        iterator = random_numbers if PRECALCULATE_RANDOM else range(RANDOM_NUMBER_COUNT)
        for m1,m2 in itertools.pairwise(iterator):
            if PRECALCULATE_RANDOM:
                random_number1 = m1 % (modulo // 2)
                random_number2 = m2 % (modulo // 2)
            else:
                random_number1 = random.randint(0, 2 ** (n - 1))
                random_number2 = random.randint(0, 2 ** (n - 1))
            test_result1 = test_addition(random_number1, 0, gates) % modulo
            test_result2 = test_addition(0, random_number1, gates) % modulo
            expected_result = random_number1
            # print(f"{expected_result=}    {test_result1=}    {test_result2=}")
            if test_result1 != expected_result or test_result1 != test_result2:
                return n - 1
            doubled_number = test_addition(random_number1, random_number1, gates) % modulo
            if doubled_number != random_number1 * 2:
                return n - 1
            added_number = test_addition(random_number1, random_number2, gates) % modulo
            if added_number != random_number1 + random_number2:
                return n - 1
    return MAX_BITS


# x_gates = sorted([gate for gate in gates.keys() if gate[0] == "x"], reverse=False)
# y_gates = sorted([gate for gate in gates.keys() if gate[0] == "y"], reverse=False)
# z_gates = sorted([gate for gate in gates.keys() if gate[0] == "z"], reverse=False)
# for target_gate in x_gates:
#     print(f"gate {target_gate}:", end = "")
#     for gate,content in gates.items():
#         gate_type, value = content
#         if gate_type == "ABS":
#             continue
#         if value[0] == target_gate or value[1] == target_gate:
#             print(f"({gate_type} {gate}), ", end = "")
#     print("")
# quit()
def evaluate_swap_pair(initial_gates, possible_swaps, start, stop, results: list):
    gates = copy.deepcopy(gates_backup)
    best_pair = [find_correct_bits(0, gates), None, None]
    matching_pairs = []
    tqdm.tqdm.write(f"starting with {best_pair[0]} correct bits")
    better_than_nothing = False
    for swap1, swap2 in itertools.islice(possible_swaps, start, stop):
        gates = copy.deepcopy(initial_gates)
        gates[swap1], gates[swap2] = gates[swap2], gates[swap1]
        # gates[swap3], gates[swap4] = gates[swap4], gates[swap3]
        correct_bits = find_correct_bits(best_pair[0], gates)
        if correct_bits > best_pair[0]:
            best_pair = [correct_bits, swap1, swap2]
            matching_pairs = []
            better_than_nothing = True
            # tqdm.tqdm.write(f"better pair found : {best_pair=}")
        elif better_than_nothing and correct_bits == best_pair[0]:
            matching_pairs.append(swap1, swap2)
            # tqdm.tqdm.write(f"match found : {swap1=} {swap2=}")
    results.append(best_pair)


if known_swaps:
    for swap1, swap2 in itertools.batched(known_swaps, 2):
        gates[swap1], gates[swap2] = gates[swap2], gates[swap1]

# ---------- GOOD SHIT:
gates_backup = copy.deepcopy(gates)

non_input_gates = [gate for gate in gates if (not (gate[0] == "x" or gate[0] == "y"))]
print(f"{len(gates)=}")
print(f"{len(non_input_gates)=}")

labels_swapped = []

target_bits = min(TARGET_BITS,44)

while find_correct_bits(1, gates) < target_bits:
# for _ in range(2):

    # gates = copy.deepcopy(gates_backup)
    best_pair = [find_correct_bits(0, gates), None, None]
    print(f"starting search with {best_pair[0]} bits correct already")
    non_input_gates = [
        gate for gate in gates if (not (gate[0] == "x" or gate[0] == "y"))
    ]
    for swap1, swap2 in tqdm.tqdm(
        itertools.combinations(non_input_gates, 2),
        total=(len(non_input_gates) * (len(non_input_gates) - 1)) // 2, 
        ncols= 200
    ):
        # if swap1[0] == "x" or swap1[0] == "y" or swap2[0] == "x" or swap2[0] == "y":
        #     continue
        better_than_nothing = False
        gates = copy.deepcopy(gates_backup)
        gates[swap1], gates[swap2] = gates[swap2], gates[swap1]
        # gates[swap3], gates[swap4] = gates[swap4], gates[swap3]
        correct_bits = find_correct_bits(best_pair[0], gates)
        if correct_bits > best_pair[0]:
            best_pair = [correct_bits, swap1, swap2]
            better_than_nothing = True
            tqdm.tqdm.write(f"better pair found : {best_pair=}")
        elif better_than_nothing and correct_bits == best_pair[0]:
            tqdm.tqdm.write(f"match found : {swap1=} {swap2=}")
    _, swap1, swap2 = best_pair
    if swap1 and swap2:
        tqdm.tqdm.write(f"swapping {swap1} with {swap2}")
        gates_backup[swap1], gates_backup[swap2] = (
            gates_backup[swap2],
            gates_backup[swap1],
        )
        labels_swapped.append(swap1)
        labels_swapped.append(swap2)
    else:
        tqdm.tqdm.write(f"No swaps found! Exiting...")
        break
    gates = copy.deepcopy(gates_backup)
# -----
# ____ BELOW THIS SHItTY MULTITHREADINg


# # tqdm.tqdm.write(f"starting with {best_pair[0]} correct bits")
# better_than_nothing = False
# # for swap1, swap2 in tqdm.tqdm(
# #     itertools.combinations(gates, 2),
# #     total=(len(gates) * (len(gates) - 1)) // 2,
# #     smoothing=0.01,
# # ):
# job_length = (len(gates) * (len(gates) - 1)) // 2
# result_list = []
# threads = []
# for thread_idx in range(THREADS):
#     results = []
#     result_list.append(results)
#     start = (job_length // 64) * thread_idx
#     stop = max((((job_length // 64) * thread_idx + 1) - 1), job_length)
#     threads.append(threading.Thread(
#         target=evaluate_swap_pair,
#         args=(gates, itertools.combinations(gates, 2), start, stop, results),
#     ))

# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# best_pair = [0,None,None]
# for pair in result_list:
#     if pair[0] > best_pair:
#         best_pair = pair

# ---------- FINAL SANITY CHECK:

gates = copy.deepcopy(gates_backup)
no_errors = True
random.seed()
for n in range(target_bits//2, target_bits*2):
    number1 = random.randint(0, 2 ** min(n, target_bits-1))
    number2 = random.randint(0, 2 ** min(n, target_bits-1))
    result = test_addition(number1, number2, gates)
    if number1 + number2 != result:
        print(
            f"{number1=}, {number2=}, {result=}, expected_result={number1+number2} {n=}"
        )
        no_errors = False
if no_errors:
    print("all checks out!")
    correct_labels = labels_swapped
    if known_swaps:
        correct_labels += known_swaps
    print(f"answer: {','.join(sorted(correct_labels))}")
