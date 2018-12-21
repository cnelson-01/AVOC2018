inF = "input.txt"

testInput = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz",
]

lines = open(inF, 'r').readlines()
# lines = testInput
for line1 in lines:
    for line2 in lines:
        diffs = 0
        resultString = ""
        for index, value in enumerate(list(line1)):
            if line1[index] != line2[index]:
                diffs += 1
                if diffs == 1:
                    resultString = line1[:index] + line1[index + 1:]
            if diffs > 1:
                break
        if diffs == 1:
            break
    if diffs == 1:
        print("result: " + resultString)
        break
