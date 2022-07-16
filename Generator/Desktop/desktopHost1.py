"""
NAME - hosts
TYPE - Desktop - CUSTOM
INFO -
Allows ~ Reddit, Pinterest, Tumblr, and Google Services
Blocks ~ Adobe, Luminar, and Edge Telemetry
"""

import os


def generateFile():
    keywords = ["# Pinterest", "# Tumblr", "# Reddit"]
    fileOutput = open("Desktop/hosts", "w")
    with open("Sources/hosts.txt", "r") as mainFile:
        for line in mainFile:
            if line.strip() in keywords:
                while line.strip() != "":
                    line = mainFile.__next__()
            else:
                fileOutput.write(line)


def addCommon():
    fileOutput = open("Desktop/hosts", "a")
    with open("Sources/Common.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def addDesktop():
    fileOutput = open("Desktop/hosts", "a")
    with open("Sources/Desktop.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def callAll():
    print("---> Generating Desktop: hosts")
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
