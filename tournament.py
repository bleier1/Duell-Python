from player import Player

class Tournament(object):
	
	def __init__(self):
		"""Default constructor"""
		self.humanWins = 0
		self.computerWins = 0
		
	# Getters
	
	def getHumanWins(self):
		return self.humanWins
		
	def getComputerWins(self):
		return self.computerWins
		
	# *********************************************************************	
	# Function Name: addHumanPoint
	# Purpose: To add a point to the human wins in the tournament
	# Parameters:
	# self, the Tournament the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Increment humanWins by one
	# Assistance Received: none
	# *********************************************************************
	
	def addHumanPoint(self):
		self.humanWins += 1
		
	# *********************************************************************	
	# Function Name: addComputerPoint
	# Purpose: To add a point to the computer wins in the tournament
	# Parameters:
	# self, the Tournament the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Increment computerWins by one
	# Assistance Received: none
	# *********************************************************************
	
	def addComputerPoint(self):
		self.computerWins += 1
		
	# *********************************************************************	
	# Function Name: printWins
	# Purpose: To print the amount of wins each player has to the window
	# Parameters:
	# self, the Tournament the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Print the amount of wins the computer has in the tournament
	# 2) Print the amount of wins the human has in the tournament
	# Assistance Received: none
	# *********************************************************************
	
	def printWins(self):
		print("Computer Wins: " + str(self.computerWins))
		print("")
		print("Human Wins: " + str(self.humanWins))
		print("")