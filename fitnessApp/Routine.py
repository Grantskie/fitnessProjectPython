import aesthetics
import os

class Routine:
    def __init__(self, username, routineName, cursor):
        self.username = username
        self.routineName = routineName
        self.cursor = cursor
        self.routineList = self.generateRoutineData()
        self.dayArray = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.routineInsert = "INSERT INTO routine (username, routineName, exercise, amount, day) VALUES "


    def displayRoutine(self):
        exerciseStr = ""
        for x in range(7):
            for i in self.routineList[x]:
                if i != None:
                    exerciseStr += i[0] + "->" + i[1] + "\t"
            dayColStr = str(x + 1) + ") " + self.dayArray[x] + "  "
            print(aesthetics.dayColumn(dayColStr) + " " + exerciseStr)
            exerciseStr = ""
            aesthetics.printBorderHorz(1)

    def addDay(self, dayNum):
        dayNumber = int(dayNum) - 1
        day = self.dayArray[dayNumber]
        os.system('cls')
        aesthetics.printHeader(day)
        aesthetics.printBorderVertStr("Enter exercise")
        aesthetics.printBorderHorz(1)
        exercise = input(">Input<")
        os.system('cls')
        aesthetics.printHeader("Enter amount (Distance, duration, sets/reps)")
        amount = input(">Input<")
        tupleInput = (exercise, amount)
        print(tupleInput)
        self.routineList[dayNumber].append(tupleInput)
        print(self.routineList)
        self.routineInsert += f"(\'{self.username}\', \'{self.routineName}\', \'{exercise}\', \'{amount}\', \'{day}\'),"

    def insertRoutine(self, cursor, cnx):
        self.routineInsert = self.routineInsert[0:-1]
        cursor.execute(self.routineInsert)
        cnx.commit()

    def generateRoutineData(self):
        selectQuery = f"SELECT day, exercise, amount FROM routine WHERE username = \'{self.username}\' AND routineName = \'{self.routineName}\'"
        self.cursor.execute(selectQuery)
        result = self.cursor.fetchall()
        routineList = []
        for i in range(7):
            inner = []
            for j in range(1):
                inner.append(None)
            routineList.append(inner)
        for i in result:
            if i[0] == "Sunday":
                insertTuple = (i[1], i[2])
                routineList[0].append(insertTuple)
            elif i[0] == "Monday":
                insertTuple = (i[1], i[2])
                routineList[1].append(insertTuple)
            elif i[0] == "Tuesday":
                insertTuple = (i[1], i[2])
                routineList[2].append(insertTuple)
            elif i[0] == "Wednesday":
                insertTuple = (i[1], i[2])
                routineList[3].append(insertTuple)
            elif i[0] == "Thursday":
                insertTuple = (i[1], i[2])
                routineList[4].append(insertTuple)
            elif i[0] == "Friday":
                insertTuple = (i[1], i[2])
                routineList[5].append(insertTuple)
            else:
                insertTuple = (i[1], i[2])
                routineList[6].append(insertTuple)
        return routineList

    def getRoutineName(self):
        return self.routineName

    def getExerciseSet(self):
        returnSet = {}
        for i in range(6):
            for j in self.routineList(i):
                returnSet.add()
        return returnSet

    def getRoutineId(self, exercise, amount, cursor):
        routineId = 0
        selectId = f"SELECT routineId FROM routine WHERE username = \'{self.username}\' AND routineName = \'{self.routineName}\' AND exercise = \'{exercise}\' AND amount = \'{amount}\' ORDER BY routineId DESC"
        cursor.execute(selectId)
        resultSet = cursor.fetchall()
        for x in resultSet:
            routineId = x[0]
        return routineId