class Die(object):
		
	def __init__(self, topInput, rightInput, player):
		"""Constructor that allows specification for the number on top and right of the die."""
		# Dice can be controlled by either a human (H) or computer (C). It is not valid otherwise.
		if (player == 'H' or player == 'C'):
			self.playerType = player
		else:
			self.playerType = 'N'
		# If both topInput and rightInput are 1, this is a key die and thus each side must be 1.
		if (topInput == 1 and rightInput == 1):
			self.topNum = topInput
			self.rightNum = rightInput
			self.leftNum = 1
			self.playerFacingNum = 1
			self.bottomNum = 1
			self.awayFacingNum = 1
			return
		# Otherwise, initialize each side to the same numbers of the default constructor.
		self.topNum = 1
		self.rightNum = 5
		self.playerFacingNum = 3
		self.bottomNum = 7 - self.topNum
		self.leftNum = 7 - self.rightNum
		self.awayFacingNum = 7 - self.playerFacingNum
		# Now we will adjust each side so that they match the inputs passed into the constructor's parameters. This will
		# be done by rotating the die until the sides appropriately match the topInput and rightInput.
		# First, check the inputs. If they are not valid, then don't change anything about the die.
		if ((topInput < 1 or topInput > 6) or (rightInput < 1 or rightInput > 6)):
			self.topNum = 1
			self.rightNum = 5
		# Otherwise, it's a legal die. Go ahead and adjust the sides appropriately.
		else:
			# Make the topInput the topNum on the die.
			self.rotateToTopNum(topInput)
			# Make the rightInput the rightNum on the die.
			self.rotateToRightNum(rightInput)
		# If it's a computer die, the die needs to be rotated twice so that the point of view of the computer player has
		# the appropriate right side of the die.
		if (self.playerType == 'C'):
			self.rotateLeft()
			self.rotateLeft()
			
	# Alternate constructor that does not take sides:
	@classmethod
	def defaultDie(cls):
		return cls(1, 5, 'N')
	
	# Various getters...
	
	def getTopNum(self):
		return self.topNum
		
	def getRightNum(self):
		return self.rightNum
		
	def getLeftNum(self):
		return self.leftNum
		
	def getPlayerType(self):
		return self.playerType
	
	# *********************************************************************	
	# Function Name: moveUp
	# Purpose: To "roll" the die upwards and update each side appropriately to simulate a die being rolled up
	# Parameters:
	# self, the Die to call the function on
	# Return Value: none
	# Local Variables:
	# temp - stores the topNum of the die
	# Algorithm:
	# 1) Initialize temp to store the topNum of the die
	# 2) Switch every integer that needs to be switched around. topNum becomes the number that faces the player
	# 3) playerFacingNum becomes the number on the bottom
	# 4) bottomNum becomes the number that was facing away from the player
	# 5) awayFacingNum becomes the number on the top of the die, which was stored in temp
	# Assistance Received: none
	# *********************************************************************
	
	def moveUp(self):
		# Initialize a temporary int to store the value of a number on the die.
		temp = self.topNum
		self.topNum = self.playerFacingNum
		self.playerFacingNum = self.bottomNum
		self.bottomNum = self.awayFacingNum
		self.awayFacingNum = temp
		
	# *********************************************************************	
	# Function Name: moveDown
	# Purpose: To "roll" the die downwards and update each side appropriately to simulate a die being rolled down
	# Parameters:
	# self, the Die to call the function on
	# Return Value: none
	# Local Variables:
	# temp - stores the topNum of the die
	# Algorithm:
	# 1) Initialize temp to store the topNum of the die
	# 2) Switch every integer that needs to be switched around. topNum becomes the number that faces the player
	# 3) awayFacingNum becomes the number on the bottom
	# 4) bottomNum becomes the number that was facing towards the player
	# 5) playerFacingNum becomes the number on the top of the die, which was stored in temp
	# Assistance Received: none
	# *********************************************************************
	
	def moveDown(self):
		# Initialize a temporary int to store the value of a number on the die.
		temp = self.topNum
		self.topNum = self.awayFacingNum
		self.awayFacingNum = self.bottomNum
		self.bottomNum = self.playerFacingNum
		self.playerFacingNum = temp
		
	# *********************************************************************	
	# Function Name: moveLeft
	# Purpose: To "roll" the die to the left and update each side appropriately to simulate a die being rolled to the left
	# Parameters:
	# self, the Die to call the function on
	# Return Value: none
	# Local Variables:
	# temp - stores the topNum of the die
	# Algorithm:
	# 1) Initialize temp to store the topNum of the die
	# 2) Switch every integer that needs to be switched around. topNum becomes the number on the right of the die
	# 3) rightNum becomes the number on the bottom
	# 4) bottomNum becomes the number that was on the left of the die
	# 5) leftNum becomes the number on the top of the die, which was stored in temp
	# Assistance Received: none
	# *********************************************************************
	
	def moveLeft(self):
		# Initialize a temporary int to store the value of a number on the die.
		temp = self.topNum
		self.topNum = self.rightNum
		self.rightNum = self.bottomNum
		self.bottomNum = self.leftNum
		self.leftNum = temp
		
	# *********************************************************************	
	# Function Name: moveRight
	# Purpose: To "roll" the die to the right and update each side appropriately to simulate a die being rolled to the right
	# Parameters:
	# self, the Die to call the function on
	# Return Value: none
	# Local Variables:
	# temp - stores the topNum of the die
	# Algorithm:
	# 1) Initialize temp to store the topNum of the die
	# 2) Switch every integer that needs to be switched around. topNum becomes the number on the left of the die
	# 3) leftNum becomes the number on the bottom
	# 4) bottomNum becomes the number that was on the right of the die
	# 5) rightNum becomes the number on the top of the die, which was stored in temp
	# Assistance Received: none
	# *********************************************************************
	
	def moveRight(self):
		# Initialize a temporary int to store the value of a number on the die.
		temp = self.topNum
		self.topNum = self.leftNum
		self.leftNum = self.bottomNum
		self.bottomNum = self.rightNum
		self.rightNum = temp
		
	# *********************************************************************	
	# Function Name: rotateLeft
	# Purpose: To "rotate" the die to the left and update each side appropriately to simulate a die being rotated to the left
	# Parameters:
	# self, the Die to call the function on
	# Return Value: none
	# Local Variables:
	# temp - stores the playerFacingNum of the die
	# Algorithm:
	# 1) Initialize temp to store the playerFacingNum of the die
	# 2) Switch every integer that needs to be switched around. playerFacingNum becomes the number on the left of the die
	# 3) leftNum becomes the number facing away from the player
	# 4) awayFacingNum becomes the number on the right of the die
	# 5) rightNum becomes the number that was facing the player, which was stored in temp
	# Assistance Received: none
	# *********************************************************************
	
	def rotateLeft(self):
		# Initialize a temporary int to store the value of a number on the die.
		temp = self.playerFacingNum
		self.playerFacingNum = self.leftNum
		self.leftNum = self.awayFacingNum
		self.awayFacingNum = self.rightNum
		self.rightNum = temp
		
	# *********************************************************************	
	# Function Name: rollDie
	# Purpose: To "roll" the die in the direction specified by the parameter
	# Parameters:
	# self, the Die to call the function on
	# direction, the direction that the die will move
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Determine the direction
	# 2) Move in the direction specified by the string
	# Assistance Received: none
	# *********************************************************************
	
	def rollDie(self, direction):
		if (direction == "up"):
			self.moveUp()
		if (direction == "down"):
			self.moveDown()
		if (direction == "left"):
			self.moveLeft()
		if (direction == "right"):
			self.moveRight()
	
	# *********************************************************************	
	# Function Name: rotateToTopNum
	# Purpose: To rotate the die so that the number passed into the parameter is on the top of the die
	# Parameters:
	# self, the Die to call the function on
	# topInput, the number that will end up on the top of the die
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Determine what number topInput is storing
	# 2) Rotate the die appropriately according to what that number is. The function assumes the top number on the die is
	# always 1
	# Assistance Received: none
	# *********************************************************************
	
	def rotateToTopNum(self, topInput):
		# If topInput is 1, nothing needs to be done.
		if (topInput == 1):
			return
		# If it's 2, it needs to be moved towards the right.
		if (topInput == 2):
			self.moveRight()
			return
		# If it's 3, it needs to be moved upwards.
		if (topInput == 3):
			self.moveUp()
			return
		# If it's 4, it needs to be moved downwards.
		if (topInput == 4):
			self.moveDown()
			return
		# If it's 5, it needs to be moved to the left.
		if (topInput == 5):
			self.moveLeft()
			return
		# If it's 6, it needs to be moved upward twice.
		if (topInput == 6):
			self.moveUp()
			self.moveUp()
			return
	
	# *********************************************************************	
	# Function Name: rotateToRightNum
	# Purpose: To rotate the die so that the number passed into the parameter is on the right of the die
	# Parameters:
	# self, the Die to call the function on
	# rightInput, the number that will end up on the right of the die
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) 1) While the rightNum of the die is not equal to the rightInput, rotate left until it is. The function assumes that
	# the right number is already on the left, right, towards, or away from the player
	# Assistance Received: none
	# *********************************************************************
	
	def rotateToRightNum(self, rightInput):
		# Rotate left until rightNum equals rightInput
		while (self.rightNum != rightInput):
			self.rotateLeft()