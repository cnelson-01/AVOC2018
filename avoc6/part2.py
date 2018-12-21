inF = 'input.txt'

pointsx = []
pointsy = []

# '''
# 1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# '''
#
# pointsx = [
#     1, 1, 8, 3, 5, 8
# ]
# pointsy = [
#     1, 6, 3, 4, 5, 9
# ]

distSumThresh = 10000

for line in open(inF, 'r').readlines():
    pointsx.append(int(line.split(',')[0]))
    pointsy.append(int(line.split(' ')[1]))

minx = min(pointsx)
maxx = max(pointsx)

miny = min(pointsy)
maxy = max(pointsy)

grid = [[0 for a in range(maxy + 1)] for b in range(maxx + 1)]

for index, x in enumerate(pointsx):
    y = pointsy[index]
    grid[x][y] = index


def calculateDistance(col, row, index):
    dist = abs(pointsx[index] - col) + abs(pointsy[index] - row)
    return dist


def findNearestPoint(col, row):
    moreThanOne = False
    ptIndex = 0
    dist = calculateDistance(col, row, 0)
    for index, x in enumerate(pointsx[1:]):
        y = pointsy[index]
        tmp = calculateDistance(col, row, index)
        if tmp < dist:
            dist = tmp
            ptIndex = index
            moreThanOne = False
        elif tmp == dist:
            moreThanOne = True
    return ptIndex, moreThanOne


def isInfinate(col, row):
    if col == 0 or row == 0:
        return True
    if col == maxx or row == maxy:
        return True
    return False


def findSumOfDistances(col, row):
    s = 0
    for index, x in enumerate(pointsx):
        y = pointsy[index]
        s += calculateDistance(col, row, index)
    return s


# init the grid
for col in range(len(grid)):
    for row in range(len(grid[0])):
        s = findSumOfDistances(col, row)
        if s < distSumThresh:
            grid[col][row] = s
        else:
            grid[col][row] = -1
            # (ptindex, moreThanOne) = findNearestPoint(col, row)
        # if not moreThanOne:
        #     grid[col][row] = ptindex
        # else:
        #     grid[col][row] = -1

# # areas = [area, isInfinate]
# areas = [[0, False] for a in range(len(pointsx))]
count = 0
# find the area
for col in range(len(grid)):
    for row in range(len(grid[0])):
        if grid[col][row] > 0:
            count += 1
# m = 0
# for a in areas:
#     if not a[1]:
#         if a[0] > m:
#             m = a[0]

for a in range(len(grid)):
    print(grid[a])
print("area: " + str(count))
