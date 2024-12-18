import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split("\n")

def complex_mag_diff(left,right):
    diff = (right.real**2 + right.imag**2)**0.5 - (left.real**2 + left.imag**2)**0.5
    return diff

machines = []
for rows in itertools.batched(data_string, 4):
    machine = []
    machine.append(int(rows[0].split(" ")[2][1:-1]))
    machine.append(int(rows[0].split(" ")[3][1:]))
    machine.append(int(rows[1].split(" ")[2][1:-1]))
    machine.append(int(rows[1].split(" ")[3][1:]))
    machine.append(int(rows[2].split(" ")[1][2:-1]) + 10000000000000)
    machine.append(int(rows[2].split(" ")[2][2:]) + 10000000000000)
    machines.append(machine)
machine_answers = []
for machine_idx, machine in enumerate(machines):
    ax, ay, bx, by, tx, ty = machine
    a_button = complex(ax, ay)
    b_button = complex(bx, by)
    target = complex(tx, ty)
    positions_per_coin:dict[str,set[complex]] = {0: [(0 + 0j)]}
    machine_answer = 0
    for coins in range(1000000000000000000):
        if target in positions_per_coin[coins]:
            machine_answer = coins
            break
        if all((complex_mag_diff(n, target) < 0) for n in positions_per_coin[coins]):
            break
        if coins + 1 not in positions_per_coin:
            positions_per_coin[coins + 1] = set()
        if coins + 3 not in positions_per_coin:
            positions_per_coin[coins + 3] = set()
        positions = positions_per_coin[coins]
        for position in positions:
            positions_per_coin[coins + 1].add((position + b_button))
            positions_per_coin[coins + 3].add((position + a_button))
    machine_answers.append(machine_answer)
    print(f"{machine_idx + 1} machines processed")

answer = sum(machine_answers)

print(f"Answer: {answer}")
