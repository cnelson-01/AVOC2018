inF = 'sampleInput.txt'

heads = []


def getThisNameFromLine(line):
    return line.split(' ')[1]


def getChildNameFromLine(line):
    return line.split(' ')[7]


class Step:
    def __init__(self, name):
        self.children = []
        self.name = name

    def find(self, name):
        if name == self.name:
            return self
        for child in self.children:
            res = child.find(name)
            if res:
                return res
        return ''

    def updateChildren(self, heads, childName):
        child = ''
        for head in heads:
            child = head.find(childName)
            if child == head:
                self.children.append(child)
                heads.remove(head)
                heads.append(self)
        if not child:
            child = Step(childName)
            self.children.append(child)


for line in open(inF, 'r').readlines():
    step = ''
    name = getThisNameFromLine(line)
    for head in heads:
        step = head.find(name)
    if not step:
        heads.append(Step(name))
    if not heads[-1].updateChildren(heads, getChildNameFromLine(line)):
        heads.append(Step(name))


pass
