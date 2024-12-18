#this extracts string data from data.txt, what is used in each day's challenge
strData = []
with open("in.txt") as f:
    for line in f:
        strData.append(line.replace("\n", ""))

#adding boundary to data - indexed data[y][x]
data = []
for row in strData:
    data.append(["!"] + list(row) + ["!"])
    
data.insert(0, ["!"]*len(data[0]))
data.append(["!"]*len(data[0]))

#finding initial guard pos
for yGuardInit, row in enumerate(data):
    if "^" in row:
        xGuardInit = row.index("^")
        break

#rewriting guard pos as valid space
data[yGuardInit][xGuardInit] = "."

directions = ((0,-1), (1,0), (0,1), (-1,0))
def run_simulation(xGuard, yGuard, dirGuard, data, isPart2=False):
    visitedPositions = {(xGuard, yGuard, dirGuard)} if isPart2 else {(xGuard, yGuard)}#set to avoid duplicates
    while True:
        nextItem = data[yGuard+directions[dirGuard][1]][xGuard+directions[dirGuard][0]]
        if nextItem == "!":
            break
        elif nextItem == "#":
            dirGuard = (dirGuard+1)%4
            continue

        xGuard += directions[dirGuard][0]
        yGuard += directions[dirGuard][1]

        if isPart2:
            oldLen = len(visitedPositions)
            visitedPositions.add((xGuard, yGuard, dirGuard))
            if len(visitedPositions) == oldLen:
                return "loop found"
        else:
            visitedPositions.add((xGuard, yGuard))

    return visitedPositions
    
visitedPositions = list(run_simulation(xGuardInit, yGuardInit, 0, data))
len(visitedPositions)


total = 0
for coord in visitedPositions:
    if coord == (xGuardInit, yGuardInit):
        continue

    x = coord[0]
    y = coord[1]
    data[y][x] = "#"
    if run_simulation(xGuardInit, yGuardInit, 0, data, True) == "loop found":
        total += 1
    
    #restoring
    data[y][x] = "."
print(total)