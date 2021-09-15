

class User:
    def __init__(self, username, cursor):
        self.username = username
        self.cursor = cursor
        self.routineArray = self.generateRoutines()

    def generateRoutines(self):
        routineArray = []
        query = f"SELECT DISTINCT routineName FROM routine WHERE username = \'{self.username}\'"
        self.cursor.execute(query)
        resultSet = self.cursor.fetchall()
        for x in resultSet:
            routineArray.append(x[0])
        return routineArray

    def updateRoutines(self):
        self.routineArray = self.generateRoutines()

    def getRoutines(self):
        return self.routineArray