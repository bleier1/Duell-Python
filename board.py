from die import Die
from space import Space

class Board(object):
	
	def __init__(self):
		"""Default constructor"""
		initModel = []
		for i in range (0, 8):
			column = []
			for j in range (0, 9):
				column.append(Space.defaultSpace())
			initModel.append(column)
		self.boardModel = initModel
		
	# Getter for the top num on the die on the space:
	def getDieTopNum(self, row, column):
		return self.boardModel[row-1][column-1].getDieTopNum()
	
	# *********************************************************************	
	# Function Name: clearBoard
	# Purpose: To clear the board before setting up a new game
	# Parameters:
	# self, the board to call the function on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) For every space on the board, hasDie becomes false
	# Assistance Received: none
	# *********************************************************************
	
	def clearBoard(self):
		for i in range (8, 0, -1):
			for j in range (1, 10):
				self.boardModel[i-1][j-1].clearSpace()
	
	# *********************************************************************	
	# Function Name: setUpDice
	# Purpose: To set up the starting positions of dice in a game of Duell on the board
	# Parameters:
	# self, the board to call the function on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Place all of the dice in the Human's home row in the correct order
	# 2) Place all of the dice in the Computer's home row in the correct order
	# Assistance Received: none
	# *********************************************************************
	
	def setUpDice(self):
		# Place the human's dice.
		self.boardModel[0][0].placeDie(Die(5, 6, 'H'))
		self.boardModel[0][1].placeDie(Die(1, 5, 'H'))
		self.boardModel[0][2].placeDie(Die(2, 1, 'H'))
		self.boardModel[0][3].placeDie(Die(6, 2, 'H'))
		self.boardModel[0][4].placeDie(Die(1, 1, 'H'))
		self.boardModel[0][5].placeDie(Die(6, 2, 'H'))
		self.boardModel[0][6].placeDie(Die(2, 1, 'H'))
		self.boardModel[0][7].placeDie(Die(1, 5, 'H'))
		self.boardModel[0][8].placeDie(Die(5, 6, 'H'))
		# Place the computer's dice.
		self.boardModel[7][0].placeDie(Die(5, 6, 'C'))
		self.boardModel[7][1].placeDie(Die(1, 5, 'C'))
		self.boardModel[7][2].placeDie(Die(2, 1, 'C'))
		self.boardModel[7][3].placeDie(Die(6, 2, 'C'))
		self.boardModel[7][4].placeDie(Die(1, 1, 'C'))
		self.boardModel[7][5].placeDie(Die(6, 2, 'C'))
		self.boardModel[7][6].placeDie(Die(2, 1, 'C'))
		self.boardModel[7][7].placeDie(Die(1, 5, 'C'))
		self.boardModel[7][8].placeDie(Die(5, 6, 'C'))
		
	# *********************************************************************	
	# Function Name: placeDie
	# Purpose: To place the die passed into the parameters onto the row and column passed into the parameters on the board
	# Parameters:
	# self, the board to call the function on
	# die, a Die that will be placed on the board
	# row, an integer that corresponds to the row the die will be placed on
	# column, an integer that corresponds to the column the die will be placed on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Call placeDie on the row and column in boardModel (minus 1 to each to convert to array coordinates)
	# Assistance Received: none
	# *********************************************************************
	
	def placeDie(self, die, row, column):
		# Place the die on the board.
		self.boardModel[row-1][column-1].placeDie(die)
		
	# *********************************************************************	
	# Function Name: performRoll
	# Purpose: To make a die on the board roll in a specified direction to another space on the board
	# Parameters:
	# self, the board to call the function on
	# row, an integer that corresponds to the row of where the die is located and will move
	# column, an integer that corresponds to the column of where the die is located and will move
	# direction, a string that tells the function which direction to move the die
	# Return Value: boolean that determines if the roll was successfully performed
	# Local Variables:
	# none
	# Algorithm:
	# 1) Determine which direction the die wants to roll
	# 2) Roll in the direction specified by the string passed into the function and return true
	# 3) Otherwise, return false
	# Assistance Received: none
	# *********************************************************************
	
	def performRoll(self, row, column, direction):
		# Perform the roll.
		if direction == "up":
			self.boardModel[row-1][column-1].moveDie(self.boardModel[row][column-1], "up")
			return True
		if direction == "down":
			self.boardModel[row-1][column-1].moveDie(self.boardModel[row-2][column-1], "down")
			return True
		if direction == "left":
			self.boardModel[row-1][column-1].moveDie(self.boardModel[row-1][column-2], "left")
			return True
		if direction == "right":
			self.boardModel[row-1][column-1].moveDie(self.boardModel[row-1][column], "right")
			return True
		return False
		
	# *********************************************************************	
	# Function Name: isDieOn
	# Purpose: To determine the status of whether or not there is a die on the coordinates passed into the function
	# Parameters:
	# self, the board to call the function on
	# row, an integer that corresponds to the row of where the function will check for a die
	# column, an integer that corresponds to the column of where the function will check for a die
	# Return Value: a boolean that determines if there is a die on the coordinates or not
	# Local Variables:
	# none
	# Algorithm:
	# 1) Return the result of isSpaceOccupied() on the space located where row and column are in the boardModel array
	# Assistance Received: none
	# *********************************************************************
	
	def isDieOn(self, row, column):
		# Return the result of isSpaceOccupied on the space given by the coordinates.
		return self.boardModel[row-1][column-1].isSpaceOccupied()
		
	# *********************************************************************	
	# Function Name: isDiePlayerType
	# Purpose: To determine if the die on the coordinates passed into the function is of the player type passed into the function
	# Parameters:
	# self, the board to call the function on
	# row, an integer that corresponds to the row of where the function will check for a die
	# column, an integer that corresponds to the column of where the function will check for a die
	# playerChar, a character that corresponds to the player type of the die that will be checked
	# Return Value: a boolean that determines if there the die is of the player type playerChar
	# Local Variables:
	# none
	# Algorithm:
	# 1) Call getDiePlayerType() on the space located where row and column are in the boardModel array
	# 2) Compare that to playerChar
	# 3) Return true if it is the same, return false otherwise
	# Assistance Received: none
	# *********************************************************************
	
	def isDiePlayerType(self, row, column, playerChar):
		# If the die on the space is of the same player type as playerChar, return true. Otherwise, return false.
		if (self.boardModel[row-1][column-1].getDiePlayerType() == playerChar):
			return True
		else:
			return False
			
	# *********************************************************************	
	# Function Name: isKeyDie
	# Purpose: To determine if the die on the coordinates passed into the function is a key die or not
	# Parameters:
	# self, the board to call the function on
	# row, an integer that corresponds to the row of where the die is located
	# column, an integer that corresponds to the column of where the die is located
	# Return Value: a boolean that determines if there the die is a key die or not
	# Local Variables:
	# topNum and rightNum, integers that store the results of getTopNum() and getRightNum() respectively
	# Algorithm:
	# 1) Call spaceOccupied() on the space that corresponds to the row and column coordinates. Return false is that
	# function returns false
	# 2) Otherwise, there's a die on the space. Get the top and right numbers of the die on the space
	# 3) If those numbers are both 1, it's a key die. Return true. Otherwise return false
	# Assistance Received: none
	# *********************************************************************
	
	def isKeyDie(self, row, column):
		# Check if there is even a die on the space. If there isn't, return false.
		if (not (self.boardModel[row-1][column-1].isSpaceOccupied())):
			return False
		# Get the top number of the die occupying the space.
		topNum = self.boardModel[row-1][column-1].getDieTopNum()
		# Get the right number of the die occupying the space.
		rightNum = self.boardModel[row-1][column-1].getDieRightNum()
		# If they are both 1, this is a key die.
		if (topNum == 1 and rightNum == 1):
			return True
		else:
			return False
			
	# *********************************************************************	
	# Function Name: getDieName
	# Purpose: To return the name of the die on the coordinates passed into the function
	# Parameters:
	# row, an integer that corresponds to the row of where the die is located
	# column, an integer that corresponds to the column of where the die is located
	# Return Value: a string containing the name of the die on the space
	# Local Variables:
	# topNum and RightNum, integers that store the results of getTopNum() and getRightNum() respectively
	# Algorithm:
	# 1) Store the results of getTopNum() and getRightNum()/getLeftNum() in topNum and rightNum respectively
	# 2) If the player type of the die is H, get the rightNum. If the player type of the die is C, get the leftNum
	# 3) Return a string contatenating the character of the player type, and the top and right number converted to strings
	# Assistance Received: none
	# *********************************************************************
	
	def getDieName(self, row, column):
		# Get the top number of the die on the space.
		topNum = self.boardModel[row-1][column-1].getDieTopNum()
		# Get the right number of the die on the space... BUT:
		# If it's a human, get the rightNum. If it's a computer, get the leftNum.
		rightNum = 5
		playerType = self.boardModel[row-1][column-1].getDiePlayerType()
		if (playerType == 'H'):
			rightNum = self.boardModel[row-1][column-1].getDieRightNum()
		if (playerType == 'C'):
			rightNum = self.boardModel[row-1][column-1].getDieLeftNum()
		# Convert to string, concatenate, and return:
		dieName = str(playerType) + str(topNum) + str(rightNum)
		return dieName