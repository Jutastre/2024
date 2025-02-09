import itertools

FILENAME = "tin.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split("\n")

machines = []
for rows in itertools.batched(data_string, 4):
    machine = []
    machine.append(int(rows[0].split(" ")[2][1:-1]))
    machine.append(int(rows[0].split(" ")[3][1:]))
    machine.append(int(rows[1].split(" ")[2][1:-1]))
    machine.append(int(rows[1].split(" ")[3][1:]))
    # machine.append(int(rows[2].split(" ")[1][2:-1]))
    # machine.append(int(rows[2].split(" ")[2][2:]))
    machine.append(int(rows[2].split(" ")[1][2:-1]) + 10_000_000_000_000)
    machine.append(int(rows[2].split(" ")[2][2:]) + 10_000_000_000_000)
    machines.append(machine)
machine_answers = []
for machine_idx, machine in enumerate(machines):
    machine_answer = 0
    ax, ay, bx, by, tx, ty = machine
    swapped_a_b = False
    if ay / ax > by / bx:
        ax, ay, bx, by = bx, by, ax, ay
        swapped_a_b = True
    a_presses = 1
    b_presses = False
    if ay / ax > ty / tx or by / bx < ty / tx:  # impossible case
        continue
    while (ty - (a_presses * ay)) / (tx - (a_presses * ax)) < by / bx:
        a_presses += 100_000_000
    while (ty - (a_presses * ay)) / (tx - (a_presses * ax)) > by / bx:
        a_presses -= 100_000
    while (ty - (a_presses * ay)) / (tx - (a_presses * ax)) < by / bx:
        a_presses += 1000
    while (ty - (a_presses * ay)) / (tx - (a_presses * ax)) > by / bx:
        a_presses -= 1

    print(f"{a_presses=}")
    print(f"{a_presses * ax=}")
    print(f"{a_presses * ay=}")
    print(f"{tx-(a_presses * ax)=}")
    print(f"{tx-(a_presses * ay)=}")

    for press_ec in range(-8000, 8000):
        offset_a_presses = a_presses + press_ec
        if ((tx - (offset_a_presses * ax)) % bx != 0) or (
            (ty - (offset_a_presses * ay)) % by != 0
        ):
            continue
        if ((tx - (offset_a_presses * ax)) // bx) != (
            (ty - (offset_a_presses * ay)) // by
        ):
            break
        b_presses = (tx - (offset_a_presses * ax)) // bx
        break
    if not b_presses:
        continue
    if swapped_a_b:
        a_presses, b_presses = b_presses, a_presses
    machine_answers.append((a_presses * 3) + b_presses)


answer = sum(machine_answers)

print(f"Answer: {answer}")
