"""
NAME - hosts
TYPE - Desktop & Mobile DEFAULT
INFO -
Blocks ~ Desktop + Mobile + Social + Ad
"""

import os


def generateFile():
    fileOutput = open("hosts", "w")
    with open("Sources/hosts.txt", "r") as mainFile:
        for line in mainFile:
            fileOutput.write(line)


def addCommon():
    fileOutput = open("hosts", "a")
    with open("Sources/Common.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def addDesktop():
    fileOutput = open("hosts", "a")
    with open("Sources/Desktop.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def addMobile():
    fileOutput = open("hosts", "a")
    with open("Sources/Mobile.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def callAll():
    print("---> Generating Default: hosts")
    generateFile()
    addCommon()
    addDesktop()
    print("*** Done! ***")


if __name__ == "__main__":
    os.system('cmd /c "cls"')
    print("*********************************")
    print("Desktop - hosts")
    print("*********************************")
    callAll()
