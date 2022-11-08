"""
NAME - utils
TYPE - Utility
INFO -
Utilty function which converts tab to white space 
for hosts file taken from the Excel sheet
"""

import os 

def editCommon():
	# Create a new file with similar name
	fileOutput = open("Sources/Common2.txt","w")
	with open("Sources/Common.txt", "r") as addFile:
		for line in addFile:
			new_line = line.replace('\t', ' ')
			fileOutput.write(new_line)
		fileOutput.write("\n")
  # Delete the old file
	os.remove("Sources/Common.txt")
	# Rename new file back to Common.txt
	fileOutput.close()
	old_file = os.path.join("Sources", "Common2.txt")
	new_file = os.path.join("Sources", "Common.txt")
	os.rename(old_file, new_file)

def editDesktop():
	# Create a new file with similar name
	fileOutput = open("Sources/Desktop2.txt","w")
	with open("Sources/Desktop.txt", "r") as addFile:
		for line in addFile:
			new_line = line.replace('\t', ' ')
			fileOutput.write(new_line)
		fileOutput.write("\n")
  # Delete the old file
	os.remove("Sources/Desktop.txt")
	# Rename new file back to Desktop.txt
	fileOutput.close()
	old_file = os.path.join("Sources", "Desktop2.txt")
	new_file = os.path.join("Sources", "Desktop.txt")
	os.rename(old_file, new_file)

def editMobile():
	# Create a new file with similar name
	fileOutput = open("Sources/Mobile2.txt","w")
	with open("Sources/Mobile.txt", "r") as addFile:
		for line in addFile:
			new_line = line.replace('\t', ' ')
			fileOutput.write(new_line)
		fileOutput.write("\n")
  # Delete the old file
	os.remove("Sources/Mobile.txt")
	# Rename new file back to Mobile.txt
	fileOutput.close()
	old_file = os.path.join("Sources", "Mobile2.txt")
	new_file = os.path.join("Sources", "Mobile.txt")
	os.rename(old_file, new_file)

def callAll():
	print("---> Cleaning up Sources files")
	editCommon()
	editDesktop()
	editMobile()

if __name__ == "__main__":
	os.system('cmd /c "cls"')
	print("*********************************")
	print("Utils - Cleaning Up")
	print("*********************************")
	callAll()