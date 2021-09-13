class Routine:
    def __init__(self, username, routineName):
        self.username = username
        self.routineName = routineName
        routineInsert = "INSERT INTO routine (username, routineName, exercise, amount, day) VALUES "
        dayArray = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        #routineList = List.fill(7)(ArrayBuffer[Tuple2[String, String]]())
        exerciseStr = ""

    def displayRoutine(self):
        pass
    def addDay(self):
        pass
    def insertRoutine(self):
        pass
    def generateRoutineData(self):
        pass
    def getRoutineName(self):
        pass
    def getExerciseSet(self):
        pass
    def getRoutineId(self):
        pass