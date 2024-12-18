import itertools

FILENAME = "in.txt"


with open(FILENAME) as f:
    data_string = f.read().strip()
assert len(data_string) % 2 == 1
data = []
id = 0
for batch in itertools.batched(data_string, 2):
    data.append([id, int(batch[0])])
    if len(batch) > 1:
        data.append([None, int(batch[1])])
    id += 1


def is_defragged(data):
    for block in data[:-1]:
        if block[0] == None:
            return False
    return True

def prune(data):
    for b1,b2 in itertools.pairwise(data):
        if b1[0] == b2[0]:
            b1[1] += b2[1]
            b2[1] = 0
    data = [block for block in data if block[1] != 0]
    return data
def checksum(data):
    checksum = 0
    block_index = 0
    for block in data:
        for _ in range(block[1]):
            #print(block[0] if block[0] != None else '.', end = '')
            if block[0] != None:
                checksum += block_index * block[0]
            block_index += 1
    #print("")
    return checksum
data = prune(data)

for block in reversed(data):
    if block[0] != None:
        id = block[0]
        break

while id >= 0:
    for idx, block in enumerate(data):
        if block[0] == id:
            src = idx
            break
    dest = None
    for idx, block in enumerate(data):
        if idx >= src:
            break
        if block[0] == None and block[1] >= data[src][1]:
            dest = idx
            break
    if dest:
        if data[src][1] < data[dest][1]:
            data[dest][1] -= data[src][1]
            data.insert(dest, [data[src][0], data[src][1]])
            data[src+1][0] = None
        elif data[src][1] == data[dest][1]:
            data[dest][0] = data[src][0]
            data[src][0] = None
        data = prune(data)
    id -= 1
    checksum(data)




print(f"answer: {checksum(data)}")
