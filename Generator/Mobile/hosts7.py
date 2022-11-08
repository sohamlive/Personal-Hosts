"""
NAME - hosts5_1
TYPE - Mobile - CUSTOM
INFO -
Allows ~ Reddit, Pinterest, Tumblr, Google Services, WhatsApp and Twitter
"""

import os


def generateFile():
    fileOutput = open("Mobile/hosts5_1", "w")
    keywords = ["# Pinterest", "# Tumblr", "# Reddit", "# Whatsapp", "# Twitter"]
    with open("Sources/hosts.txt", "r") as mainFile:
        for line in mainFile:
            if line.strip() in keywords:
                while line.strip() != "":
                    line = mainFile.__next__()
            else:
                fileOutput.write(line)


def addCommon():
    urls = ["0.0.0.0 twitter.com", "0.0.0.0 www.twitter.com"]
    fileOutput = open("Mobile/hosts5_1", "a")
    with open("Sources/Common.txt", "r") as addFile:
        fileOutput.write("\n")
        for line in addFile:
            if line.strip() in urls:
                line = addFile.__next__()
            fileOutput.write(line)
        fileOutput.write("\n")


def callAll():
    print("---> Generating Mobile: hosts5_1")
    generateFile()
    addCommon()
    print("*** Done! ***")


if __name__ == "__main__":
    os.system('cmd /c "cls"')
    print("*********************************")
    print("Mobile - hosts5_1")
    print("*********************************")
    callAll()
