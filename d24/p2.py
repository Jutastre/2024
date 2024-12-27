import itertools
import copy

FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split("\n\n")
gates = {}
for row in data[0].split("\n"):
    gate,value = row.split(": ")
    value = int(value)
    gates[gate] = ("ABS",value)

for row in data[1].split("\n"):
    op1, operator, op2, _, gate = row.split()
    gates[gate] = (operator, (op1,op2))

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

z_gates = {}

for gate in gates.keys():
    if gate[0] == 'z':
        z_gates[gate] = get_gate_value(gate)

z_bits = ""

for n in range(99):
    gate = f"z{n:02}"
    if gate not in z_gates:
        break
    bits = str(z_gates[gate]) + bits
print(bits)
answer = int(f"{bits}", base = 2)
print(answer)