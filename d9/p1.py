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


while not is_defragged(data):
    while data[-1][0] == None:
        data.pop()
    for idx, block in enumerate(data):
        if block[0] == None:
            dest = idx
            break

    if data[-1][1] < data[dest][1]:
        data[dest][1] -= data[-1][1]
        data.insert(dest, [data[-1][0], data[-1][1]])
        data.pop()
    elif data[-1][1] == data[dest][1]:
        data[dest][0] = data[-1][0]
        data.pop()
    elif data[-1][1] > data[dest][1]:
        data[dest][0] = data[-1][0]
        data[-1][1] -= data[dest][1]


def checksum(data):
    checksum = 0
    block_index = 0
    for block in data:
        for _ in range(block[1]):
            # print(block[0], end = '')
            checksum += block_index * block[0]
            block_index += 1
    # print("")
    return checksum

print(checksum(data))
