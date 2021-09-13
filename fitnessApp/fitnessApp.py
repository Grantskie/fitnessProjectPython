import os
import mysql.connector
import databaseTools
import aesthetics


cnx = mysql.connector.connect(user='scalaFitnessApp', password='ScalaFitness1!',
                                  host='127.0.0.1',
                                  database='fitnessapp')
cursor = cnx.cursor()


def openingScreen():
    os.system('cls')
    aesthetics.printHeader("Welcome to the Fitness App!")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderVertStr("1) Sign Up")
    aesthetics.printBorderVertStr("2) Login")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterExit()

def usernameCheck(username, cursor) -> bool:
    test = True
    testQuery = f"SELECT username FROM login WHERE username = \'{username}\'"
    #print(testQuery)
    cursor.execute(testQuery)
    for x in cursor:
        if(x != None):
            test = False
    return test

def signUpPage(cursor, cnx):
    os.system('cls')
    aesthetics.printHeader("Lets get you signed up!")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderVertStr("Enter a username")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterBack()
    username = input(">Input<")
    if username != '<':
        test = usernameCheck(username, cursor)
        if test == False:
            while True:
                os.system('cls')
                aesthetics.printHeader("That username has been taken")
                aesthetics.printBorderVert(1)
                aesthetics.printBorderVertStr("Enter a username")
                aesthetics.printBorderVert(1)
                aesthetics.printBorderHorz(1)
                aesthetics.printFooterBack()
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

def loginPage(cursor):
    checkTestPwd = False
    checkTestUser = False
    while True:
        os.system('cls')
        if checkTestUser == False:
            aesthetics.printHeader("Login")
        else:
            aesthetics.printHeader("Unknown username - Please create an account")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderVertStr("Enter your username")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderHorz(1)
        aesthetics.printFooterBack()
        username = input(">Input<")
        query = f"SELECT username, password FROM login WHERE username = \'{username}\'"
        cursor.execute(query)
        for x in cursor:
            if x[0] == None:
                checkTestUser = True
            else:
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

def mainPage(username):
    os.system('cls')
    aesthetics.printHeader(f"Welcome {username}")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderVertStr("1) Create Routine")
    aesthetics.printBorderVertStr("2) View Routines  ")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterLogout()

while True:
    openingScreen()
    userInput = input(">Input<")
    if userInput == '<':
        break
    elif userInput == '1':
        signUpPage(cursor, cnx)
    elif userInput == '2':
        username = loginPage(cursor)
        while True:
            mainPage(username)
            userInput = input(">Input<")
            if userInput == '<':
                break
            elif userInput == '1':
                pass
            elif userInput == '2':
                pass
            else:
                print("Please input an acceptable option")
    else:
        print("Please input an acceptable option")