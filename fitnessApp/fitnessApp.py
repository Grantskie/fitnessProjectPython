import os
import mysql.connector
import cliPages
import aesthetics
import User
import Routine

cnx = mysql.connector.connect(user='scalaFitnessApp', password='ScalaFitness1!',
                                  host='127.0.0.1',
                                  database='fitnessapp')
cursor = cnx.cursor()


def usernameCheck(username, cursor) -> bool:
    test = True
    testQuery = f"SELECT username FROM login WHERE username = \'{username}\'"
    #print(testQuery)
    cursor.execute(testQuery)
    for x in cursor:
        if(x != None):
            test = False
    return test

def signUp(cursor, cnx):
    cliPages.signUpPage()
    username = input(">Input<")
    if username != '<':
        test = usernameCheck(username, cursor)
        if test == False:
            while True:
                cliPages.signUpPage(test)
                username = input(">Input<")
                if username != '<':
                    test = usernameCheck(username, cursor)
                    if test == True:
                        break
                else:
                    break
        if username != '<':
            os.system('cls')
            aesthetics.printHeader("Enter a password")
            password = input(">Input<")
            insertUserQuery = f"INSERT INTO login(username, password) VALUES (\'{username}\',\'{password}\')"
            cursor.execute(insertUserQuery)
            cnx.commit()

def login(cursor):
    checkTestPwd = False
    checkTestUser = False
    while True:
        cliPages.loginPage(checkTestUser)
        username = input(">Input<")
        query = f"SELECT username, password FROM login WHERE username = \'{username}\'"
        cursor.execute(query)
        test = cursor.fetchall()
        if len(test) == 0:
            checkTestUser = True
        else:
            for x in test:
                passwordEntered = x[1]
                while True:
                    os.system('cls')
                    if checkTestPwd == False:
                        aesthetics.printHeader(f"Hi {username}! Please enter password")
                    else:
                        aesthetics.printHeader("Incorrect password. Please re-enter")
                    aesthetics.printFooterBack()
                    password = input(">Input<")
                    if password == '<':
                        break
                    if passwordEntered != password:
                        checkTestPwd = True
                    else:
                        return username
        if username == '<':
            break

def createRoutine(cursor, cnx):
    cliPages.createRoutinePage()
    userInput = input(">Input<")
    if userInput != '<':
        routine2 = Routine.Routine(username, userInput, cursor)
        while True:
            cliPages.viewRoutineCreationPage(routine2)
            userInput = input(">Input<")
            if userInput == '<':
                break
            elif userInput == '>':
                print('test')
                routine2.insertRoutine(cursor, cnx)
                break
            else:
                routine2.addDay(userInput)

def viewRoutine(user):
    cliPages.viewRoutinePage(user)


while True:
    cliPages.openingPage()
    userInput = input(">Input<")
    if userInput == '<':
        break
    elif userInput == '1':
        signUp(cursor, cnx)
    elif userInput == '2':
        username = login(cursor)
        user = User.User(username, cursor)
        while True:
            cliPages.mainPage(username)
            userInput = input(">Input<")
            if userInput == '<':
                break
            elif userInput == '1':
                createRoutine(cursor, cnx)
            elif userInput == '2':
                while True:
                    user.updateRoutines()
                    viewRoutine(user)
                    userInput = input(">Input<")
                    if userInput == '<':
                        break
                    routineList = user.getRoutines()
                    try:
                        if int(userInput) >= 1 or int(userInput) <= len(routineList) + 1:
                            routine = Routine.Routine(user.username, routineList[int(userInput) - 1], cursor)
                            cliPages.viewSingleRoutinePage(routine)
                            input("any")
                    except:
                        print("Please input an acceptable option")
            else:
                print("Please input an acceptable option")
    else:
        print("Please input an acceptable option")