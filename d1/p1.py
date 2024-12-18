

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split('\n')

list1 = []
list2 = []
for row in data:
    n1,n2 = row.split()
    n1 = int(n1)
    n2 = int(n2)
    list1.append(n1)
    list2.append(n2)

difference_sum = 0

for n1,n2 in zip(sorted(list1),sorted(list2)):
    difference_sum += abs(n1-n2)

print (difference_sum)
