import re

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip() + "    "

statement_sum = 0

def check_if_correct_mul(string):
    pass

enabled = True

cur = -1
while cur < (len(data)-12):
    cur += 1
    if data[cur:cur+4] == "do()":
        enabled = True
        continue
    if data[cur:cur+7] == "don't()":
        enabled = False
        continue
    if enabled:
        if data[cur:cur+4] == "mul(":
            possibly_numbers = data[cur+4:cur+12]
            if ")" not in possibly_numbers:
                continue
            possibly_numbers = possibly_numbers.split(')')[0]
            if "," not in possibly_numbers:
                continue
            n1,n2 = possibly_numbers.split(',')
            if not n1.isnumeric() or not n2.isnumeric():
                continue
            n1,n2 = int(n1), int(n2)
            if n1 < 0 or n2 < 0 or n1 > 999 or n2 > 999:
                continue
            statement_sum += n1 * n2


print (statement_sum)
