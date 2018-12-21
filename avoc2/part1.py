inF = "input.txt"

contains2ExactCount = 0
contains3ExactCount = 0


def containsExactly(line, count):
    for c in list(line):
        if len(line.split(c)) - 1 == count:
            return True
    return False

for line in open(inF, 'r').readlines():
    if containsExactly(line, 2):
        contains2ExactCount += 1
    if containsExactly(line, 3):
        contains3ExactCount += 1

print("result: " + str(contains2ExactCount * contains3ExactCount))
