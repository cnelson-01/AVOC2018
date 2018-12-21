
class GaurdSchedule:
    def __init__(self, id, dt):
        self.id = id
        # dict with 60 elements true for asleep false for awake
        self.isAsleepDict = {}
        self.dateTime = dt
        self.timeAsleep = 0

        for a in range(60):
            self.isAsleepDict[str(a)] = ""

    def setStatus(self, dt, isAsleep):
        startMinute = dt.minute
        for a in range(startMinute, 60):
            self.isAsleepDict[str(a)] = isAsleep
        self.updateTimeAsleep()

    def updateTimeAsleep(self):
        self.timeAsleep = 0
        for key, value in self.isAsleepDict.items():
            if value:
                self.timeAsleep += 1

    def getMinutesAsleep(self):
        result = []
        for key, value in self.isAsleepDict.items():
            if value:
                result.append(int(key))
        return result

    def getTimeAsleep(self):
        return self.timeAsleep
