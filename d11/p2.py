import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split(" ")

stones_list = [int(n) for n in data_string]

stones = {}
for stone in stones_list:
    if stone in stones:
        stones[stone] += 1
    else:
        stones[stone] = 1

print(f"after {0}: {sum(stones.values())}")
for step in range(75):
    # print(f"Starting step {step}...")
    new_stones = {}
    for stone_number, amount in stones.items():
        if stone_number == 0:
            if 1 in new_stones:
                new_stones[1] += amount
            else:
                new_stones[1] = amount
        elif len(string := str(stone_number)) % 2 == 0:

            stone1 = int(string[: (len(string) // 2)])
            stone2 = int(string[(len(string) // 2) :])
            if stone1 in new_stones:
                new_stones[stone1] += amount
            else:
                new_stones[stone1] = amount
            if stone2 in new_stones:
                new_stones[stone2] += amount
            else:
                new_stones[stone2] = amount
        else:
            stone_number *= 2024
            if stone_number in new_stones:
                new_stones[stone_number] += amount
            else:
                new_stones[stone_number] = amount
    stones = new_stones
    print(f"after {step+1}: {sum(stones.values())}")

print(f"Answer: {sum(stones.values())}")
