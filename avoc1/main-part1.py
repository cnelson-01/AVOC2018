#python3

inF = "input.txt"

result = 0
for line in open(inF, "r").readlines():
    num = int(line[1:])
    if line[0] == "-":
        num *= -1
    result += num

print ("result is: " + str(result))

