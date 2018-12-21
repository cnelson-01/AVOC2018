inF = 'input.txt'

pointsx = []
pointsy = []

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


# init the grid
for col in range(len(grid)):
    for row in range(len(grid[0])):
        (ptindex, moreThanOne) = findNearestPoint(col, row)
        if not moreThanOne:
            grid[col][row] = ptindex
        else:
            grid[col][row] = -1

# areas = [area, isInfinate]
areas = [[0, False] for a in range(len(pointsx))]
# find the area
for col in range(len(grid)):
    for row in range(len(grid[0])):
        if grid[col][row] > 0:
            pt = grid[col][row]
            areas[pt] = [areas[pt][0] + 1, isInfinate(col, row) or areas[pt][1]]

m = 0
for a in areas:
    if not a[1]:
        if a[0] > m:
            m = a[0]

for a in range(len(grid)):
    print(grid[a])
print("max area: " + str(m))

