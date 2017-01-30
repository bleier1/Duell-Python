from die import Die

class Space(object):
	
	def __init__(self, die):
		"""Constructor that lets the die have a space on it"""
		self.dieOnSpace = die
		self.hasDie = True
		
	# Constructor that initializes a Space without a die on it.
	@classmethod
	def defaultSpace(cls):
		default = cls(Die.defaultDie())
		default.hasDie = False
		return default
		
	# Various getters...
	
	def isSpaceOccupied(self):
		return self.hasDie
		
	def getDieTopNum(self):
		return self.dieOnSpace.getTopNum()
		
	def getDieRightNum(self):
		return self.dieOnSpace.getRightNum()
		
	def getDieLeftNum(self):
		return self.dieOnSpace.getLeftNum()
		
	def getDiePlayerType(self):
		return self.dieOnSpace.getPlayerType()
		
	# *********************************************************************	
	# Function Name: placeDie
	# Purpose: To place a die on the space
	# Parameters:
	# self, the Space to call the function on
	# die, the Die that will be placed on the Space
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Assign the dieOnSpace to the Dice d that is passed into the parameters, then assign hasDie to true as there is
	# a die on the space
	# Assistance Received: none
	# *********************************************************************
	
	def placeDie(self, die):
		self.dieOnSpace = die
		# There is now a die on the space.
		self.hasDie = True
		
	# *********************************************************************	
	# Function Name: moveDie
	# Purpose: To move a die from one space to the other
	# Parameters:
	# self, the Space to call the function on
	# space, the Space to receive the die currently on self
	# direction, the direction that the die needs to roll in to reach the Space space
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Roll the die on the space in the direction specified in the parameter
	# 2) Place the die on this space to Space s
	# 3) Change this space's hasDie value to false as there is no longer a die on it
	# Assistance Received: none
	# *********************************************************************
	
	def moveDie(self, space, direction):
		# First, adjust the die in the direction that the die will roll in.
		self.dieOnSpace.rollDie(direction)
		# Now call placeDie to place the die on self to space.
		space.placeDie(self.dieOnSpace)
		# This space no longer has a die.
		self.hasDie = False
		
	# *********************************************************************	
	# Function Name: clearSpace
	# Purpose: To "clear" the space on the board
	# Parameters:
	# self, the Space to call the function on
	# Return Value: boolean that determines if the space has a die
	# Local Variables:
	# none
	# Algorithm:
	# 1) hasDie becomes false
	# Assistance Received: none
	# *********************************************************************
	
	def clearSpace(self):
		self.hasDie = False