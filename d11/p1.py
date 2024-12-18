import itertools

FILENAME = "zero.txt"


with open(FILENAME) as f:
    data_string = f.read().strip().split(' ')

stones = [int(n) for n in data_string]

for step in range(25):
    # print(f"Starting step {step}...")
    cur = 0
    while cur < len(stones):
        if stones[cur] == 0:
            stones[cur] = 1
        elif len(str(stones[cur])) % 2 == 0:
            string = str(stones[cur])
            stone1 = string[:len(string) // 2]
            stone2 = string[len(string) // 2:]
            stones = stones[:cur] + [int(stone1),int(stone2)] + stones[cur+1:]
            cur += 1
        else:
            stones[cur] *= 2024
        cur += 1
    print(f"after {step}: {len(stones)}")

print(f"Answer: {len(stones)}")
