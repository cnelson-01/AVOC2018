# python3

inF = "input.txt"

#dict for hashing
pastResults = {}

result = 0
found = False
while (not found):
    for line in open(inF, "r").readlines():
        num = int(line[1:])
        if line[0] == "-":
            num *= -1
        result += num
        if str(result) not in pastResults:
            pastResults[str(result)] = 1
        else:
            print("first duplicate is: " + str(result))
            found = True
            break
