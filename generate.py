"""
Driver code to generate all the custom hosts file for Mobile and Desktop.
Put the source host file from Steven Black in the Sources folder along
with other hosts
----
Date - 16th July, 2022
"""
import os
import Generator.default
import Generator.utils
import Generator.Desktop.desktopHost1
import Generator.Mobile.hosts1
import Generator.Mobile.hosts2
import Generator.Mobile.hosts3
import Generator.Mobile.hosts4
import Generator.Mobile.hosts5
import Generator.Mobile.hosts6
import Generator.Mobile.hosts7

os.system('cmd /c "cls"')

print("***********************")
print("      Generate.py      ")
print("***********************")

# Clean up the sources folder
def step0():
    print("----- STEP 0 -----")
    print("Cleaning sources ...")
    Generator.utils.callAll()
    print("Done!\n")

# Create the directories
def step1():
    print("----- STEP 1 -----")
    print("Creating directories ...")
    if not os.path.exists("Desktop"):
        os.mkdir("Desktop")
    if not os.path.exists("Mobile"):
        os.mkdir("Mobile")
    print("Done!\n")


# Create the default hosts file for Desktop and Mobile
def step2():
    print("----- STEP 2 -----")
    print("Creating default hosts file ...")
    # TODO : Call the default hosts file generator
    Generator.default.callAll()
    print("Done!\n")


# Create the hosts file for Desktop
def step3():
    print("----- STEP 3 -----")
    print("Creating hosts file ...")
    Generator.Desktop.desktopHost1.callAll()
    print("Done!\n")


# Create the hosts file for Mobile
def step4():
    print("----- STEP 4 -----")
    print("Creating hosts file ...")
    Generator.Mobile.hosts1.callAll()
    Generator.Mobile.hosts2.callAll()
    Generator.Mobile.hosts3.callAll()
    Generator.Mobile.hosts4.callAll()
    Generator.Mobile.hosts5.callAll()
    Generator.Mobile.hosts6.callAll()
    Generator.Mobile.hosts7.callAll()
    print("Done!\n")


if __name__ == "__main__":
    print("\n")
    step0()
    step1()
    step2()
    step3()
    step4()
