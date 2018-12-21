import datetime
from avoc4 import GaurdSchedule

inF = "input.txt"
outF = "inputChron.txt"

orderedLines = []
schedules = []
gaurds = {}

dateFormatString = "[%Y-%m-%d %H:%M]"


def getDt(line):
    dt = datetime.datetime.strptime(line.split("]")[0] + ']', dateFormatString)
    return dt


def getID(line):
    id = int(line.split("#")[1].split(" ")[0])
    return id


for line in open(inF, "r").readlines():
    inserted = False
    for index, ol in enumerate(orderedLines):
        if getDt(line) < getDt(ol):
            orderedLines.insert(index, line)
            inserted = True
            break
    if not inserted:
        orderedLines.append(line)
    print(line.strip())

of = open(outF, "w")
of.writelines(orderedLines)

for line in orderedLines:
    dt = getDt(line)
    if "Guard" in line:
        id = getID(line)
        schedules.append(GaurdSchedule.GaurdSchedule(id, dt))
    if "falls asleep" in line:
        schedules[-1].setStatus(dt, True)
    elif "wakes up" in line:
        schedules[-1].setStatus(dt, False)

for s in schedules:
    if str(s.id) not in gaurds:
        gaurds[str(s.id)] = [s]
    else:
        gaurds[str(s.id)].append(s)

maxTimeAsleep = 0
maxTimeAsleepGaurdId = 0
maxTimeMinutesTally = []
for gId, gSchedulesList in gaurds.items():

    minutesTally = [0 for a in range(60)]
    for sch in gSchedulesList:
        minutes = sch.getMinutesAsleep()
        for m in minutes:
            minutesTally[m] += 1

    if max(minutesTally) > maxTimeAsleep:
        maxTimeAsleep = max(minutesTally)
        maxTimeAsleepGaurdId = gSchedulesList[0].id
        maxTimeMinutesTally = minutesTally

print("max time asleep: " + str(maxTimeAsleep))
print("gaurd ID: " + str(maxTimeAsleepGaurdId))
print("Minutes Tally: " + str(maxTimeMinutesTally))
print("Max minute: " + str(maxTimeMinutesTally.index(max(maxTimeMinutesTally))))

print("result: " + str(maxTimeMinutesTally.index(max(maxTimeMinutesTally)) * maxTimeAsleepGaurdId))
