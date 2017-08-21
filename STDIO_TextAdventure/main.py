import sys
import os
from Story import Story

def PrintHeader():
	print "-----------------------------"
	print "STDIO Choice Adventure Engine"
	print "By Sam Tregillus and Victoria Cder"
	print "Made for the 2017 STDIO Game Jam at the Oakland MADE Museum"
	print "-----------------------------"
	
def PrintEnd():
	print "-----------------------------"
	print "THE END"
	print "-----------------------------"
	print "Press enter to exit"
	raw_input()

#Looks for all the directories in the current directory that have a "start.txt" in them, and lets the user select one
def ChooseStory():
	print "Choose a story:"
	
	dirs = [d for d in os.listdir(".\\") if os.path.isdir(d)]
	validDirs = []
	for i in range(0, len(dirs)):
		if(os.path.isfile(".//" + dirs[i] + "//start.txt")):
			validDirs.append(dirs[i])
	
	for i in range(0, len(validDirs)):
		print str(i+1) + ": " + validDirs[i]
	
	choice = -1
	while(choice == -1):
		choiceInput = raw_input()
		try:
			choice = int(choiceInput)		
		except ValueError:
			choice = -1
		
		if(choice < 1 or choice > len(validDirs)):
			print "Invalid entry"
			choice = -1
	
	return validDirs[choice-1]

def main():

	PrintHeader()
	
	dataDirectory = "data"
	if(len(sys.argv)==2):
		dataDirectory = sys.argv[1]
	else:
		dataDirectory = ChooseStory()

	theStory = Story(dataDirectory)
	
	
	
	theStory.RunStory()

	PrintEnd()

if __name__ == '__main__':
	main()
