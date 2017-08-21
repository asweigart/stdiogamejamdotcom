class Story:
	#The file extension to use for story sections
	FILEEXTENSION = ".txt"
	
	#Takes the filename (without extension) of the start set of text
	def __init__(self, startDirectory):
		self.choices = []
		self.directory = startDirectory
	
	#call this to start running the story, starting with the startFilename, 
	#it will go until it hits a label called "end"
	def RunStory(self):
		self.currentLabel = "start"
		try:
			while(self.currentLabel != "end"):
				self.currentLabel = self.RunSection(self.currentLabel)
		except:
			print("Something went wrong, there's probably an issue with the files")
	
	def RunSection(self, sectionName):
		filename = "./" + self.directory + "/" + sectionName + self.FILEEXTENSION
		sectionChoices = []
		sectionChoiceIDs = []
		sectionChoiceLabels = []
		
		file = open(filename, "r")
		for line in file:
			#Parse the text that shows when listing the valid choices
			if line.startswith("{choiceText}"):
				sectionChoices = line.split(",")
				sectionChoices.pop(0)
			#Parse the choiceIDs
			elif line.startswith("{choiceIDs}"):
				sectionChoiceIDs = line.split()
				sectionChoiceIDs.pop(0)
			#Parse the labels
			elif line.startswith("{labels}"):
				sectionChoiceLabels = line.split()
				sectionChoiceLabels.pop(0)
			#Parse the conditional lines of text
			elif line.startswith("["):
				conditionalLine = line.split(" ", 1);
				condition = conditionalLine[0][1:-1]
				if(condition in self.choices):
					print(str.strip(conditionalLine[1]))
					raw_input()
			#Otherwise, just output the line!
			else:
				print(str.strip(line))
				raw_input()
		
		file.close()
		
		#Ask for input until the user inputs a valid choice
		choice = -1
		while(choice == -1):
			print("Would you like to:")
			for i in range(1, len(sectionChoices)+1):
				print(str(i) + ": " + sectionChoices[i-1])
			
			try:
				choiceInput = int(raw_input())
				if(choiceInput not in range(1, len(sectionChoices)+1)):
					choice = -1
				else:
					choice = choiceInput
			except ValueError:
				choice = -1
			
			if(choice == -1):
				print("That's not a valid choice!")
			
		#Add the choice to the choice list so that we can remember all the choices made
		self.choices.append(sectionChoiceIDs[choice-1])
		return sectionChoiceLabels[choice-1]
		