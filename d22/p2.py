import itertools
import copy

FILENAME = "in.txt"

def mix(number, secret_number) -> int:
    return number ^ secret_number

def prune(secret) -> int:
    return secret % 16777216

def mixprune(number,secret) -> int:
    return prune(mix(number,secret))

def sequence_step(number) -> int:
    number = mixprune(number * 64, number)
    number = mixprune(number // 32, number)
    number = mixprune(number * 2048, number)
    return number


with open(FILENAME) as f:
    initial_numbers = [int(n) for n in f.read().strip().split("\n")]

total_score_dict = {}

sum = 0
for initial_number in initial_numbers:
    n = initial_number
    history = [False,False,False,False]
    monkey_score_dict = {}
    for _ in range(2000):
        last_price = n % 10
        n = sequence_step(n)
        current_price = n % 10
        change = current_price - last_price
        history = history[1:] + [change]
        if history[0]:
            sequence = tuple(history)
            if sequence not in monkey_score_dict:
                monkey_score_dict[sequence] = current_price
    for k,v in monkey_score_dict.items():
        if k in total_score_dict:
            total_score_dict[k] += v
        else:
            total_score_dict[k] = v

highest = 0

for k,v in total_score_dict.items():
    if v > highest:
        best_sequence = k
        highest = v

print(highest)