"""
NAME - hosts
TYPE - Mobile - DEFAULT
INFO -
Blocks ~ Ad + social media + Google Play Services.
(Blocking Google Services will create issues on
the working of Play Store, Maps, Backups, etc.)
"""

import os


def generateFile():
    fileOutput = open("Mobile/hosts", "w")
    with open("Sources/hosts.txt", "r") as mainFile:
        for line in mainFile:
            fileOutput.write(line)


def addCommon():
    fileOutput = open("Mobile/hosts", "a")
    with open("Sources/Common.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def addMobile():
    fileOutput = open("Mobile/hosts", "a")
    with open("Sources/Mobile.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def callAll():
    print("---> Generating Mobile: hosts")
    generateFile()
    addCommon()
    addMobile()
    print("*** Done! ***")


if __name__ == "__main__":
    os.system('cmd /c "cls"')
    print("*********************************")
    print("Mobile - hosts")
    print("*********************************")
    callAll()
