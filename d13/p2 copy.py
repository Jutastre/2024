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
    # one button cases handled first to avoid ruling them out due to floating point errors -- actually these cases should be impossible with a and b only having two digit numbers, with t being so large
    if tx % ax == 0 and ty % ay == 0 and tx // ax == ty // ay:
        machine_answers.append(machine_answer:=((tx // ax) * 3))
        print(f"machine #{machine_idx} resulted in {machine_answer}, ({(tx // ax)}) -- A ONLY")
        continue
    if tx % bx == 0 and ty % by == 0 and tx // bx == ty // by:
        machine_answers.append(machine_answer:=(tx // bx))
        print(f"machine #{machine_idx} resulted in {machine_answer}, ({(tx // bx)}) -- B ONLY")
        continue


    swapped_a_b = False
    if ay / ax > by / bx:
        ax, ay, bx, by = bx, by, ax, ay
        swapped_a_b = True
    a_presses = 1
    b_presses = False


    if ay / ax > ty / tx or by / bx < ty / tx:  # impossible case
        continue
    adjustment_size = 100_000_000
    sign = 1
    while adjustment_size >= 1:
        while (
            (((tx - (a_presses * ax)) // bx) <= ((ty - (a_presses * ay)) // by)) ^ 
            (sign == 1)
        ):
            a_presses += adjustment_size * sign
        sign *= -1
        adjustment_size //= 10
    if swapped_a_b:
        ax, ay, bx, by = bx, by, ax, ay
        a_presses, b_presses = b_presses, a_presses
    for adjustment in range(-1,2):
        adjusted_a_presses = a_presses + adjustment
        if (((tx - (adjusted_a_presses * ax)) // bx) == ((ty - (adjusted_a_presses * ay)) // by)):
            b_presses = (tx - (adjusted_a_presses * ax)) // bx

            ax_distance = adjusted_a_presses * ax
            ay_distance = adjusted_a_presses * ay
            bx_distance = adjusted_a_presses * bx
            by_distance = adjusted_a_presses * by
            if ax_distance + bx_distance != tx or ay_distance + by_distance != ty:
                b_presses = False
                continue
            a_presses = adjusted_a_presses
            break
        else:
            continue
    if not b_presses or not a_presses:
        print(f"machine #{machine_idx} failed #1")
        continue
    machine_answer = (a_presses * 3) + b_presses
    print(f"machine #{machine_idx} resulted in {machine_answer}, ({a_presses}a + {b_presses}b)")
    # print(f"X = {ax_distance} + {bx_distance} == {ax_distance + bx_distance}, {tx=}")
    # print(f"Y = {ay_distance} + {by_distance} == {ay_distance + by_distance}, {ty=}")
    machine_answers.append(machine_answer)


answer = sum(machine_answers)

print(f"Answer: {answer}")
