import itertools

FILENAME = "in.txt"


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
    if ax / ay == bx / by:
        print("same angle found")
        print(f"{ax/ay} == {bx/by}")
        print(f"target angle is{tx/ty}")
        raise (Exception)
    if (ax / ay > tx / ty and bx / by > tx / ty) or (
        ax / ay < tx / ty and bx / by < tx / ty
    ):
        print(
            "not possible because (ax/ay > tx/ty and bx/by > tx/ty) or (ax/ay < tx/ty and bx/by < tx/ty)"
        )
        print(f"ax/ay = {ax/ay}")
        print(f"bx/by = {bx/by}")
        print(f"tx/ty = {tx/ty}")
        continue
    swapped = False
    if (ay / ax) > (by / bx):
        ax, ay, bx, by = bx, by, ax, ay
        swapped = True
    max = (tx // ax) + 1
    pivot = 0
    pivot_size = max // 2
    while pivot_size > 0:
        if (ty - (pivot * ay)) / (tx - (pivot * ax)) > (by / bx):
            pivot -= pivot_size
        elif (ty - (pivot * ay)) / (tx - (pivot * ax)) == (by / bx):
            break
        else:
            pivot += pivot_size
        pivot_size //= 2
    if (tx - (pivot * ax)) % bx == 0:
        print(f"{pivot=}")
        print(f"{(pivot * ax)=}")
        print(f"{(tx - (pivot * ax))=}")
        print(pivot * ax)
        if swapped:
            machine_answer = (pivot) + 3*((tx - (pivot * ax)) // bx)
        else:
            machine_answer = (3*pivot) + ((tx - (pivot * ax)) // bx)
    machine_answers.append(machine_answer)
    print(f"{machine_idx + 1} machines processed")
    # input("")

answer = sum(machine_answers)

print(f"Answer: {answer}")
