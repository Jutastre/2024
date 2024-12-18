FILENAME = "in.txt"


with open(FILENAME) as f:
    data = f.read().strip().split('\n\n')

requirements = {}
for row in data[0].split('\n'):
    n2,n1 = (int(n) for n in row.split('|'))
    if n1 in requirements:
        requirements[n1].append(n2)
    else:
        requirements[n1] = [n2]
updates = [[int(n) for n in row.split(',')] for row in data[1].split('\n')]

def middle(update):
    return update[(len(update)-1) // 2]

def check_correct_order(update, requirements):
    printed = []
    for page in update:
        if page in requirements:
            if any(((required_page in update) and (required_page not in printed)) for required_page in requirements[page]):
                return False
        printed.append(page)
    return True


middle_sum = 0

faulty_updates = []

for update in updates:
    if not check_correct_order(update, requirements):
        faulty_updates.append(update)


for update in faulty_updates:
    reconstructed = []
    while len(reconstructed) != len(update):
        for page in update:
            if page in reconstructed:
                continue
            if page in requirements:
                if any(((required_page in update) and (required_page not in reconstructed)) for required_page in requirements[page]):
                    continue
            reconstructed.append(page)
    middle_sum += middle(reconstructed)

print (middle_sum)
