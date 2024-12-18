import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

safe_count = 0

def check_if_safe(report):
    if report[0]>report[1]:
        for higher, lower in itertools.pairwise(report):
            if (higher - lower < 1) or (higher - lower > 3):
                break
        else:
            return True
    elif report[0]<report[1]:
        for lower, higher in itertools.pairwise(report):
            if (higher - lower < 1) or (higher - lower > 3):
                break
        else:
            return True
    return False


for row in data:
    found_safe = False
    report = [int(n) for n in row.split()]
    if check_if_safe(report):
        safe_count += 1
        continue


print (safe_count)
