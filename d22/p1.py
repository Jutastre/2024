import itertools
import copy

FILENAME = "in.txt"

def mix(number, secret_number) -> int:
    return number ^ secret_number

def prune(secret) -> int:
    return secret % 16777216

def mixprune(number,secret) -> int:
    return prune(mix(number,secret))

def sequence(number) -> int:
    number = mixprune(number * 64, number)
    number = mixprune(number // 32, number)
    number = mixprune(number * 2048, number)
    return number


with open(FILENAME) as f:
    initial_numbers = [int(n) for n in f.read().strip().split("\n")]

sum = 0
for initial_number in initial_numbers:
    n = initial_number
    for _ in range(2000):
        n = sequence(n)
    sum += n

print(sum)