import itertools
import copy

FILENAME = "in.txt"


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


def get_gate_value(gate):
    operator, value = gates[gate]
    match operator:
        case "ABS":
            return value
        case "XOR":
            return_value = get_gate_value(value[0]) ^ get_gate_value(value[1])
            gates[gate] = ("ABS", return_value)
            return return_value
        case "AND":
            return_value = get_gate_value(value[0]) & get_gate_value(value[1])
            gates[gate] = ("ABS", return_value)
            return return_value
        case "OR":
            return_value = get_gate_value(value[0]) | get_gate_value(value[1])
            gates[gate] = ("ABS", return_value)
            return return_value


# z_gates = {}

# for gate in gates.keys():
#     if gate[0] == 'z':
#         z_gates[gate] = get_gate_value(gate)
z_gates = sorted([gate for gate in gates.keys() if gate[0] == "z"], reverse=True)
for gate in z_gates:
    gate_tiers: list[set[str]] = []
    gate_tiers.append(set([gate]))
    idx = 0
    while gate_tiers[idx]:
        gate_tiers.append(set())
        for gate2 in gate_tiers[idx]:
            if gates[gate2][0] == "ABS":
                break
            op1, op2 = gates[gate2][1]
            gate_tiers[-1].add(op1)
            gate_tiers[-1].add(op2)
        idx += 1

    print(f"---------------------------")
    print(f"                       map for {gate=}")
    for idx, tier in enumerate(gate_tiers):
        print(f"{idx}: {tier=}")

# z_bits = ""

# for n in range(99):
#     gate = f"z{n:02}"
#     if gate not in z_gates:
#         break
#     bits = str(z_gates[gate]) + bits
# print(bits)
# answer = int(f"{bits}", base = 2)
# print(answer)
