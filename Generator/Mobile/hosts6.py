"""
NAME - hosts5
TYPE - Mobile - CUSTOM
INFO -
Allows ~ Reddit, Pinterest, Tumblr, Google Services, and Twitter
"""

import os


def generateFile():
    fileOutput = open("Mobile/hosts5", "w")
    keywords = ["# Pinterest", "# Tumblr", "# Reddit", "# Twitter"]
    with open("Sources/hosts.txt", "r") as mainFile:
        for line in mainFile:
            if line.strip() in keywords:
                while line.strip() != "":
                    line = mainFile.__next__()
            else:
                fileOutput.write(line)


def addCommon():
    fileOutput = open("Mobile/hosts5", "a")
    with open("Sources/Common.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            fileOutput.write(line)
        fileOutput.write("\n")


def callAll():
    print("---> Generating Mobile: hosts5")
    generateFile()
    addCommon()
    print("*** Done! ***")


if __name__ == "__main__":
    os.system('cmd /c "cls"')
    print("*********************************")
    print("Mobile - hosts5")
    print("*********************************")
    callAll()
