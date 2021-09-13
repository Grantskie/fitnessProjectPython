borderLength = 100


def printBorderVert(borderCount: int):
    bordVert = "|"
    for i in range(borderCount):
        for j in range(borderLength - 2):
            bordVert += " "
        bordVert += "|"
        print(bordVert)
        bordVert = "|"


def printBorderVertStr(borderStr: str):
    half = int((borderLength - 2 - len(borderStr)) / 2)
    bordVert = "|"
    additionalSpace = len(borderStr) % 2
    for i in range(half):
        bordVert += " "
    bordVert += borderStr
    for i in range(half):
        bordVert += " "
    if (additionalSpace == 1):
        bordVert += " "
    bordVert += "|"
    print(bordVert)


def printBorderHorz(borderCount):
    bordHorz = "+"
    for i in range(borderCount):
        for j in range(borderLength - 2):
            bordHorz += "-"
        bordHorz += "+"
        print(bordHorz)
        bordHorz = "+"


def printHeader(headStr: str):
    printBorderHorz(1)
    printBorderVertStr(headStr)
    printBorderHorz(1)

def printFooterBack():
    printBorderVertStr("< Back                                                  ")
    printBorderHorz(1)

def printFooterExit():
    printBorderVertStr("< Exit                                                  ")
    printBorderHorz(1)

def printFooterBackFor():
    printBorderVertStr("< Back                                         Forward >")
    printBorderHorz(1)

def printFooterLogout():
    printBorderVertStr("< Logout                                               >")
    printBorderHorz(1)