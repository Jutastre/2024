FILENAME = "in.txt"

def middle(update):
    return update[(len(update)-1) // 2]

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

middle_sum = 0

for update in updates:
    printed = []
    for page in update:
        if page in requirements:
            if any(((required_page in update) and (required_page not in printed)) for required_page in requirements[page]):
                break
        printed.append(page)
    else:
        middle_sum += middle(update)

print (middle_sum)
