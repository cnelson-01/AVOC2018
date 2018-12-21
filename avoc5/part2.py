inF = "input.txt"

polymer = open(inF, "r").readline().strip()


class PolyUnit:
    def __init__(self, c):
        self.c = c
        if self.c == self.c.upper():
            self.antiC = c.lower()
        else:
            self.antiC = c.upper()

    def react(self, n):
        if n == self.antiC:
            return ''
        else:
            return self.c + n


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


result = polymer
i = 0


def getPolyLen(poly):
    result = poly
    while True:
        startLen = len(result)
        nextResult = ''

        # get chunks and do even
        cl = chunks(list(result), 2)
        for c in cl:
            if len(c) == 2:
                pu = PolyUnit(c[0])
                nextResult += pu.react(c[1])
            else:
                nextResult += c[0]
        result = nextResult

        # get chuncks and do odd
        cl = chunks(list(result[1:]), 2)
        nextResult = result[0]
        for c in cl:
            if len(c) == 2:
                pu = PolyUnit(c[0])
                nextResult += pu.react(c[1])
            else:
                nextResult += c[0]
        # print("iteration: " + str(i) + " len: " + str(len(nextResult)) + " " + nextResult)
        if len(result) == startLen:
            break
        result = nextResult
    return len(result)


units = 'abcdefghijklmnopqrstuvwxyz'

result = []
for u in list(units):
    print('doping: ' + u)
    result.append(getPolyLen(polymer.replace(u, "").replace(u.upper(), "")))

print("min: " + str(min(result)) + " value: " + units[result.index(min(result))])
