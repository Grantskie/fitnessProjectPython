import aesthetics
import os

def openingPage():
    os.system('cls')
    aesthetics.printHeader("Welcome to the Fitness App!")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderVertStr("1) Sign Up")
    aesthetics.printBorderVertStr("2) Login")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterExit()

def signUpPage(checkTest=True):
    os.system('cls')
    if checkTest is True:
        aesthetics.printHeader("Lets get you signed up!")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderVertStr("Enter a username")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderHorz(1)
        aesthetics.printFooterBack()
    else:
        aesthetics.printHeader("That username has been taken")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderVertStr("Enter a username")
        aesthetics.printBorderVert(1)
        aesthetics.printBorderHorz(1)
        aesthetics.printFooterBack()

def loginPage(checkTestUser):
    os.system('cls')
    if checkTestUser is False:
        aesthetics.printHeader("Login")
    else:
        aesthetics.printHeader("Unknown username - Please create an account or re-enter")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderVertStr("Enter your username")
    aesthetics.printBorderVert(1)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterBack()

def mainPage(username):
    os.system('cls')
    aesthetics.printHeader(f"Welcome {username}")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderVertStr("1) Create Routine")
    aesthetics.printBorderVertStr("2) View Routines  ")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterLogout()

def createRoutinePage():
    os.system('cls')
    aesthetics.printHeader("Let's build a routine!")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderVertStr("First, enter a name for your routine")
    aesthetics.printBorderVert(2)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterBack()

def viewRoutineCreationPage(routine):
    os.system('cls')
    aesthetics.printHeader(routine.getRoutineName())
    routine.displayRoutine()
    aesthetics.printBorderVertStr("Select a day")
    aesthetics.printFooterBackSave()

def viewRoutinePage(user):
    routineArray = user.getRoutines()
    os.system('cls')
    aesthetics.printHeader(f"{user.username}'s routines")
    aesthetics.printBorderVert(1)
    count = 1
    for x in routineArray:
        aesthetics.printBorderVertStr(f"{count}) {x}")
        count += 1
    aesthetics.printBorderVert(1)
    aesthetics.printBorderHorz(1)
    aesthetics.printFooterBack()

def viewSingleRoutinePage(routine):
    os.system('cls')
    aesthetics.printHeader(routine.getRoutineName())
    routine.displayRoutine()
    aesthetics.printFooterBack()