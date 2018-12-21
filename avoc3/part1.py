inF = "input.txt"

fabricMap = [[0 for a in range(1000)] for b in range(1000)]  # 2d map of fabric in sq in

totalOverlap = 0

for line in open(inF, 'r').readlines():
    x = int(line.split(" ")[2].split(',')[0])
    y = int(line.split(" ")[2].split(',')[1].replace(":", ""))
    width = int(line.split(" ")[3].split("x")[0])
    height = int(line.split(" ")[3].split("x")[1])

    for w in range(width):
        for h in range(height):
            fabricMap[w + x][h + y] += 1
            if fabricMap[w + x][h + y] == 2:
                totalOverlap += 1

print("total overlap: " + str(totalOverlap))
