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
    machine.append(int(rows[2].split(" ")[1][2:-1]))
    machine.append(int(rows[2].split(" ")[2][2:]))
    # machine.append(int(rows[2].split(" ")[1][2:-1]) + 10_000_000_000_000)
    # machine.append(int(rows[2].split(" ")[2][2:]) + 10_000_000_000_000)
    machines.append(machine)
machine_answers = []
for machine_idx, machine in enumerate(machines):
    machine_answer = 0
    ax,ay,bx,by,tx,ty = machine
    if ax/ay == bx/by:
        print("same angle found")
        print(f"{ax/ay} == {bx/by}")
        print(f"target angle is{tx/ty}")
        input("")
    if (ax/ay > tx/ty and bx/by > tx/ty) or (ax/ay < tx/ty and bx/by < tx/ty):
        print("not possible because (ax/ay > tx/ty and bx/by > tx/ty) or (ax/ay < tx/ty and bx/by < tx/ty)")
        print(f"ax/ay = {ax/ay}")
        print(f"bx/by = {bx/by}")
        print(f"tx/ty = {tx/ty}")
        continue
        #input("")
    a_angle = ax/ay
    b_angle_offset = bx + tx/by + ty
    b_a_ratio = 1/ (b_angle_offset * (1 / a_angle))
    for n in range(82):
        print(n + n * b_a_ratio)
    print(f"{b_a_ratio=}")
    machine_answers.append(machine_answer)
    print(f"{machine_idx + 1} machines processed")
    input("")

answer = sum(machine_answers)

print(f"Answer: {answer}")
