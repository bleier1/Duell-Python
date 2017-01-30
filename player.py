from board import Board
import random

class Player(object):

	def __init__(self, name):
		"""Constructor that takes a name for the player"""
		self.playerName = name
		
	# "Default" constructor
	@classmethod
	def defaultPlayer(cls):
		return cls("N/A")
		
	# Getter for name
	def getPlayerName(self):
		return self.playerName
		
	# *********************************************************************	
	# Function Name: play
	# Purpose: A virtual function that will let the derived classes Human and Computer play the game of Duell
	# Parameters:
	# self, the Player the method is called on
	# board, the board to play on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# none
	# Assistance Received: none
	# *********************************************************************
	
	def play(self, board):
		pass
		
	# *********************************************************************	
	# Function Name: makeMove
	# Purpose: To make the move that the player wants to make on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, a Board passed by parameter that will be modified so the move can be appropriately made
	# dieRow, an integer containing the row of the die that will be moved
	# dieColumn, an integer containing the column of the die that will be moved
	# spaceCoordinate, an integer containing the row or column that the die will be moved to
	# direction, a string containing the direction that the die will move in to get to the spaceCoordinate
	# Return Value: none
	# Local Variables:
	# i, an integer used to iterate through for loops
	# Algorithm:
	# 1) Determine if the direction is moving frontally or laterally
	# 2) Perform a check to see if the spaceCoordinate is greater or less than dieRow or dieColumn
	# 3) Call performRoll() to roll in the appropriate direction determined by the check in the previous step
	# Assistance Received: none
	# *********************************************************************
	
	def makeMove(self, board, dieRow, dieColumn, spaceCoordinate, direction):
		# First determine whether to move frontally or laterally.
		if (direction == "frontally"):
			# Is the spaceCoordinate entered greater than the dieRow? If so, we must move upwards.
			if (spaceCoordinate > dieRow):
				for i in range(dieRow, spaceCoordinate):
					board.performRoll(i, dieColumn, "up")
			# Otherwise, move downwards.
			else:
				for i in range(dieRow, spaceCoordinate, -1):
					board.performRoll(i, dieColumn, "down")
		# Otherwise, move laterally.
		else:
			# Is the spaceCoordinate entered greater than the dieColumn? If so, we must move to the right.
			if (spaceCoordinate > dieColumn):
				for i in range(dieColumn, spaceCoordinate):
					board.performRoll(dieRow, i, "right")
			# Otherwise, move to the left.
			else:
				for i in range(dieColumn, spaceCoordinate, -1):
					board.performRoll(dieRow, i, "left")
					
	# *********************************************************************	
	# Function Name: canMoveLaterally
	# Purpose: To determine if a die can be moved laterally on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# dieRow, an integer containing the row of the die that will be checked
	# dieColumn, an integer containing the column of the die that will be checked
	# spaceColumn, an integer containing the column of the space that the die wants to move to
	# spacesToMove, an integer containing the amount of spaces the die will move to reach the column
	# playerType, a character containing the player type of the die that is being checked
	# Return Value: a boolean signifying whether or not a lateral move is possible
	# Local Variables:
	# i, an integer used to iterate through for loops
	# Algorithm:
	# 1) Check spacesToMove. If it's 0, the die cannot move anywhere. Return false
	# 2) Check dieColumn and spaceColumn. If they're the same, the die can only be moved frontally. Return false
	# 3) Check whether the lateral move is to the left or to the right
	# 4) For each space in between the dieColumn and spaceColumn, see if there is a die occupying any of them
	# 5) If spacesToMove isn't 1, a die cannot be placed there regardless of who owns the die. Return false
	# 6) Otherwise, if it's of an opponent's playerType, it can be captured and the die can be moved there. Return true
	# 7) But if it's one of the player's dice, you can't capture those. Return false
	# 8) Return true if there were no problems detected
	# Assistance Received: none
	# *********************************************************************
	
	def canMoveLaterally(self, board, dieRow, dieColumn, spaceColumn, spacesToMove, playerType):
		# First, if spacesToMove is 0, we can't move anywhere.
		if (spacesToMove == 0): return False
		# If dieColumn and spaceColumn are the same, we can only move frontally.
		if (dieColumn == spaceColumn): return False
		# We'll move to the right if the spaceColumn is greater than the dieColumn. Otherwise, we move to the left.
		if (spaceColumn > dieColumn):
			# Check all the spaces we want to visit:
			for i in range(dieColumn, spaceColumn):
				# Check if there is a die on the space.
				if (board.isDieOn(dieRow, i+1)):
					# If If spacesToMove is not 1, you cannot place the die there regardless of whether or not the die on it
					# is yours or the opponent's.
					if (spacesToMove != 1): return False
					# If it is, check the playerType of the die on it.
					else:
						# If it is not the playerType passed into the function, it is an opponent's die and can be captured.
						if (not (board.isDiePlayerType(dieRow, i+1, playerType))): return True
						# Otherwise, this is one of the player's own dice and thus cannot be captured or moved to.
						else: return False
				# If there is not, decrement spacesToMove
				spacesToMove -= 1
			# We can move this way.
			return True
		# Move to the left if this is not the case.
		else:
			# Check all the spaces we want to visit:
			for i in range(dieColumn, spaceColumn,-1):
				# Check if there is a die on the space.
				if (board.isDieOn(dieRow, i-1)):
					# If If spacesToMove is not 1, you cannot place the die there regardless of whether or not the die on it
					# is yours or the opponent's.
					if (spacesToMove != 1): return False
					# If it is, check the playerType of the die on it.
					else:
						# If it is not the playerType passed into the function, it is an opponent's die and can be captured.
						if (not (board.isDiePlayerType(dieRow, i-1, playerType))): return True
						# Otherwise, this is one of the player's own dice and thus cannot be captured or moved to.
						else: return False
				# If there is not, decrement spacesToMove
				spacesToMove -= 1
			# We can move this way.
			return True
	
	# *********************************************************************	
	# Function Name: canMoveFrontally
	# Purpose: To determine if a die can be moved frontally on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# dieRow, an integer containing the row of the die that will be checked
	# dieColumn, an integer containing the column of the die that will be checked
	# spaceRow, an integer containing the row of the space that the die wants to move to
	# spacesToMove, an integer containing the amount of spaces the die will move to reach the column
	# playerType, a character containing the player type of the die that is being checked
	# Return Value: a boolean signifying whether or not a frontal move is possible
	# Local Variables:
	# i, an integer used to iterate through for loops
	# Algorithm:
	# 1) Check spacesToMove. If it's 0, the die cannot move anywhere. Return false
	# 2) Check dieRow and spaceRow. If they're the same, the die can only be moved laterally. Return false
	# 3) Check whether the frontal move is upwards or downards
	# 4) For each space in between the dieRow and spaceRow, see if there is a die occupying any of them
	# 5) If spacesToMove isn't 1, a die cannot be placed there regardless of who owns the die. Return false
	# 6) Otherwise, if it's of an opponent's playerType, it can be captured and the die can be moved there. Return true
	# 7) But if it's one of the player's dice, you can't capture those. Return false
	# 8) Return true if there were no problems detected
	# Assistance Received: none
	# *********************************************************************
	
	def canMoveFrontally(self, board, dieRow, dieColumn, spaceRow, spacesToMove, playerType):
		# First, if spacesToMove is 0, we can't move anywhere.
		if (spacesToMove == 0): return False
		# If dieRow and spaceRow are the same, we can only move frontally.
		if (dieRow == spaceRow): return False
		# We'll move up if the spaceRow is greater than the dieRow. Otherwise, we move down.
		if (spaceRow > dieRow):
			# Check all the spaces we want to visit:
			for i in range(dieRow, spaceRow):
				# Check if there is a die on the space.
				if (board.isDieOn(i+1, dieColumn)):
					# If If spacesToMove is not 1, you cannot place the die there regardless of whether or not the die on it
					# is yours or the opponent's.
					if (spacesToMove != 1): return False
					# If it is, check the playerType of the die on it.
					else:
						# If it is not the playerType passed into the function, it is an opponent's die and can be captured.
						if (not (board.isDiePlayerType(i+1, dieColumn, playerType))): return True
						# Otherwise, this is one of the player's own dice and thus cannot be captured or moved to.
						else: return False
				# If there is not, decrement spacesToMove
				spacesToMove -= 1
			# We can move this way.
			return True
		# Move to the left if this is not the case.
		else:
			# Check all the spaces we want to visit:
			for i in range(dieRow, spaceRow,-1):
				# Check if there is a die on the space.
				if (board.isDieOn(i-1, dieColumn)):
					# If If spacesToMove is not 1, you cannot place the die there regardless of whether or not the die on it
					# is yours or the opponent's.
					if (spacesToMove != 1): return False
					# If it is, check the playerType of the die on it.
					else:
						# If it is not the playerType passed into the function, it is an opponent's die and can be captured.
						if (not (board.isDiePlayerType(i-1, dieColumn, playerType))): return True
						# Otherwise, this is one of the player's own dice and thus cannot be captured or moved to.
						else: return False
				# If there is not, decrement spacesToMove
				spacesToMove -= 1
			# We can move this way.
			return True
			
	# *********************************************************************	
	# Function Name: findKeyDie
	# Purpose: To get the coordinates of a key die on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the "owner" of the key die
	# Return Value: a tuple containing the coordinates of the key die
	# Local Variables:
	# i and j, integers used to iterate through for loops and determine the rows and columns
	# Algorithm:
	# 1) Iterate through the board using for loops
	# 2) If there's a key die on the space, check its player type
	# 3) If it's of playerType, return i and j in a tuple
	# Assistance Received: none
	# *********************************************************************
	
	def findKeyDie(self, board, playerType):
		# Use for loops to iterate through the board
		for i in range(8,0,-1):
			for j in range (1, 10):
				# If there is a key die on this space, check the player type:
				if (board.isKeyDie(i,j)):
					# If it is of the player type passed into the function, return its coordinates
					if (board.isDiePlayerType(i, j, playerType)): return (i, j)
					
	# *********************************************************************	
	# Function Name: canMoveToSpace
	# Purpose: To determine if a die can be moved to a space on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# dieRow, an integer containing the row of the die that will be checked
	# dieColumn, an integer containing the column of the die that will be checked
	# spaceRow, an integer containing the row of the space that the die wants to move to
	# spaceColumn, an integer containing the column of the space that the die wants to move to
	# playerType, a character containing the player type of the die that is being checked
	# Return Value: a boolean signifying whether or not a move is possible
	# Local Variables:
	# topNumber, an integer that stores the top number of the die located at (dieRow,dieColumn)
	# rowRolls and columnRolls, integers that store the number of spaces needed to move frontally and laterally respectively
	# frontalMove and lateralMove, booleans that store whether or not a frontal or lateral move is possible
	# secondFrontalMove and secondLateralMove, booleans that store whether or not a frontal or lateral move is possible after
	# a 90 degree turn
	# Algorithm:
	# 1) Get the topNumber, rowRolls, and columnRolls needed to check if a die can be moved
	# 2) If topNumber is not equal to rowRolls + columnRolls, a move is not possible. Return false
	# 3) Check if the coordinates of the space being moved to are valid (on the board). If not return false
	# 4) Check if the die can be moved frontally or laterally
	# 5) If it can't move either way return false
	# 6) If a frontal move is possible, check for a second lateral move. If it isn't possible and the remaining columnRolls
	# isn't 0, a move is not possible.
	# 7) Otherwise, a move is possible. Return true
	# 8) If a lateral move is possible, check for a second frontal move. If it isn't possible and the remaining rowRolls isn't
	# 0, a move is not possible.
	# 9) Otherwise, a movie is possible. Return true
	# 10) If the function has not returned true yet, a move is not possible. Return false
	# Assistance Received: none
	# *********************************************************************
	
	def canMoveToSpace(self, board, dieRow, dieColumn, spaceRow, spaceColumn, playerType):
		# Integer for the top number of a die.
		topNumber = board.getDieTopNum(dieRow, dieColumn)
		# Integers for the number of rolls needed to go to a space.
		rowRolls = abs(spaceRow-dieRow)
		columnRolls = abs(spaceColumn-dieColumn)
		
		# First, check to see if the topNumber is able to move enough spaces to travel to the coordinates.
		if (topNumber != rowRolls + columnRolls): return False
		# Now check to see if the coordinates the die wants to move to are valid positions.
		if ((spaceRow < 1 or spaceRow > 8) or (spaceColumn < 1 or spaceColumn > 9)): return False
		
		# Now check if the die can move there without any problems.
		frontalMove = self.canMoveFrontally(board, dieRow, dieColumn, spaceRow, topNumber, playerType)
		lateralMove = self.canMoveLaterally(board, dieRow, dieColumn, spaceColumn, topNumber, playerType)
		# If it cannot move either way at first, it cannot move to the space.
		if ((not frontalMove) and (not lateralMove)): return False
		# If it can move frontally, check to see if it can move laterally in a 90 degree turn.
		if (frontalMove):
			# If you can move frontally (at first) but you cannot move laterally afterwards and
			# the remaining number of spaces to travel is not 0, you cannot travel to that space.
			if ((not self.canMoveLaterally(board, spaceRow, dieColumn, spaceColumn, columnRolls, playerType)) and columnRolls != 0):
				# a move is not possible
				secondLateralMove = False
			# Otherwise, a move is possible
			else: return True
		# If it can move laterally, check to see if it can move frontally in a 90 degree turn.
		if (lateralMove):
			# If you can move laterally (at first) but you cannot move frontally afterwards and
			# the remaining number of spaces to travel is not 0, you cannot travel to that space.
			if ((not self.canMoveFrontally(board, dieRow, spaceColumn, spaceRow, rowRolls, playerType)) and rowRolls != 0):
				# a move is not possible
				secondFrontalMove = False
			# Otherwise, a move is possible
			else: return True
			
		# Otherwise, no possible moves
		return False
		
	# *********************************************************************	
	# Function Name: captureKeyDieScore
	# Purpose: To determine if a key die can be captured or not
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: a boolean signifying whether or not a key die capture is possible
	# Local Variables:
	# keyRow and keyColumn, integers containing the coordinates of the key die
	# i and j, integers used to iterate through for loops
	# Algorithm:
	# 1) Use findKeyDie() to get the coordinates of the enemy key die and put them into keyRow and keyColumn
	# 2) After finding the key die coordinates, scan the board for the player's dice
	# 3) For each die found that belongs to the player, see if it can move to the key die's coordinates
	# 4) If so, put i and j into a tuple with keyRow and keyColumn
	# 5) If nothing can be found, return a tuple of two 0s
	# Assistance Received: none
	# *********************************************************************
	
	def captureKeyDieScore(self, board, playerType):
		# First, find the coordinates of the key die
		if (playerType == 'H'): keyCoords = self.findKeyDie(board, 'C')
		else: keyCoords = self.findKeyDie(board, 'H')
		# Now scan the board for player dice positions
		for i in range(8,0,-1):
			for j in range(1,10):
				# See if the player's die is occupying the space
				if (board.isDieOn(i,j) and board.isDiePlayerType(i, j, playerType)):
					# Check if it can move to the key die without any problems. Return the coordinates if we can.
					if (self.canMoveToSpace(board, i, j, keyCoords[0], keyCoords[1], playerType)):
						return (i, j, keyCoords[0], keyCoords[1])
		# Capturing the key die is not possible
		return (0, 0)
		
	# *********************************************************************	
	# Function Name: captureKeySpaceScore
	# Purpose: To determine if a key space can be captured or not
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: a tuple with coordinates that signify whether a move is possible
	# Local Variables:
	# i and j, integers used to iterate through for loops
	# keyCoords, a tuple containing the coordinates of the key space of the opponent
	# Algorithm:
	# 1) Scan the board for the player's dice
	# 2) For each die found, check if it can move to the key space
	# 3) If so, return a tuple with appropriate coordinates
	# 4) If nothing can be found, return a tuple of 0s
	# Assistance Received: none
	# *********************************************************************
	
	def captureKeySpaceScore(self, board, playerType):
		# First, get the coordinates of the key space
		if (playerType == 'H'): keyCoords = (8, 5)
		else: keyCoords = (1, 5)
		# Scan the board for dice and see if they can capture the space
		for i in range(8,0,-1):
			for j in range(1,10):
				# See if a player's die is occupying the space
				if (board.isDieOn(i,j) and board.isDiePlayerType(i, j, playerType)):
					# Check if it can move there without any problems
					if (self.canMoveToSpace(board, i, j, keyCoords[0], keyCoords[1], playerType)):
						# Return coordinates if we can
						return (i, j, keyCoords[0], keyCoords[1])
		# Capturing the die is not feasible
		return (0,0)
	
	# *********************************************************************	
	# Function Name: blockKeyDieScore
	# Purpose: To determine if a key die capture needs to be blocked or not
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: a tuple with coordinates that signify whether a move is possible
	# Local Variables:
	# keyCoords, a tuple that will store the coordinates of the player's key die
	# opponentType, a character that stores the player type of the opponent of the player "calling" the function
	# i, j, playerRow, playerCol, a, b, c, and d, integers that iterate through for loops to scan the board
	# Algorithm:
	# 1) Use findKeyDie() to get the coordinates of the player's key die and put them into keyCoords
	# 2) Scan the board for the opponent's dice
	# 3) If a die is found and is able to move to the key die coordinates without problems, a block is necessary. Enter
	# more for loops
	# 4) Scan the board for the player's dice
	# 5) If a die is found, see if it can capture the die that threatens to capture the key die. If it can, create a tuple
	# with the current indices in the for loops and return the tuple
	# 6) Otherwise, see if the die can block the offending die's path
	# 7) If the offending die and the key die are in the same row, try to move to a space in between the columns that separate
	# them
	# 8) If the offending die and the key die are in the same column, try to move to a space in between the rows that separate
	# them
	# 9) If a blocking move is possible, create a tuple with the current indices in the for loops and return the tuple
	# 10) Otherwise, if all else fails, just try moving the key die away by one space in any direction, and return a tuple if possible
	# 11) Otherwise, return a tuple of two 0s
	# Assistance Received: none
	# *********************************************************************
	
	def blockKeyDieScore(self, board, playerType):
		# Store the key die coordinates and opponent's playerType
		keyCoords = self.findKeyDie(board, playerType)
		if (playerType == 'H'): opponentType = 'C'
		else: opponentType = 'H'
		# Scan the board for the opponent's dice
		for i in range(8,0,-1):
			for j in range(1,10):
				# See if an opponent's die is occupying the space
				if (board.isDieOn(i,j) and board.isDiePlayerType(i, j, opponentType)):
					# Check if it can move to the key die without any problems
					if (self.canMoveToSpace(board, i, j, keyCoords[0], keyCoords[1], opponentType)):
						# We need to block the capture/catch the offending die.
						# Scan the board for the player's dice.
						for playerRow in range(8,0,-1):
							for playerCol in range(1,10):
								# Check if the player's die is occupying the space
								if (board.isDieOn(playerRow, playerCol) and board.isDiePlayerType(playerRow, playerCol, playerType)):
									# Check if it can move to the offending die
									if (self.canMoveToSpace(board, playerRow, playerCol, i, j, playerType)):
										# The die can be captured.
										return (playerRow, playerCol, i, j)
									# Otherwise, try to block the die's path
									# See if the offending die and the key die are in the same row
									if (keyCoords[0] == i):
										# If the key die is to the left of the offending die, only search between those spaces:
										if (keyCoords[1] < j):
											for a in range(keyCoords[1], j):
												# Check if the die can move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, keyCoords[0], a, playerType)):
													# The die can be blocked.
													return (playerRow, playerCol, keyCoords[0], a)
										# Otherwise, it's to the right:
										else:
											for b in range(j, keyCoords[1], -1):
												# Check if the die can move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, keyCoords[0], b, playerType)):
													# The die can be blocked.
													return (playerRow, playerCol, keyCoords[0], b)
									# See if the offending die and the key die are in the same column
									if (keyCoords[1] == j):
										# If the key die is above the offending die, only search between those spaces:
										if (keyCoords[0] > i):
											for c in range(i,keyCoords[0]):
												# Check if the die can move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, c, keyCoords[1], playerType)):
													# The die can be blocked.
													return (playerRow, playerCol, c, keyCoods[1])
										# Otherwise, it's below the offending die.
										else:
											for d in range(keyCoords[0],i,-1):
												# Check if the die can move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, d, keyCoords[1], playerType)):
													# The die can be blocked.
													return (playerRow, playerCol, d, keyCoords[1])
						# When all else fails, try moving the key die away.
						# If they're in the same row, move to a different row.
						if (keyCoords[0] == i):
							# Try moving to the row below and the row above.
							if (self.canMoveToSpace(board, keyCoords[0], keyCoords[1], keyCoords[0]-1, keyCoords[1], playerType)):
								# Move there.
								return (keyCoords[0], keyCoords[1], keyCoords[0]-1, keyCoords[1])
							if (self.canMoveToSpace(board, keyCoords[0], keyCoords[1], keyCoords[0]+1, keyCoords[1], playerType)):
								# Move there.
								return (keyCoords[0], keyCoords[1], keyCoords[0]-1, keyCoords[1])
						# If they're in the same column, move to a different column.
						if (keyCoords[1] == j):
							# Try moving the column to the left and the column to the right.
							if (self.canMoveToSpace(board, keyCoords[0], keyCoords[1], keyCoords[0], keyCoords[1]-1, playerType)):
								# Move there.
								return (keyCoords[0], keyCoords[1], keyCoords[0], keyCoords[1]-1)
							if (self.canMoveToSpace(board, keyCoords[0], keyCoords[1], keyCoords[0], keyCoords[1]+1, playerType)):
								# Move there.
								return (keyCoords[0], keyCoords[1], keyCoords[0], keyCoords[1]+1)
		# Blocking is not possible.
		return (0,0)
	
	# *********************************************************************	
	# Function Name: blockKeySpaceScore
	# Purpose: To determine if a key space capture needs to be blocked or not
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: a tuple signifying whether or not a move is possible
	# Local Variables:
	# keyCoords, a tuple that will store the coordinates of the player's key space
	# opponentType, a character that stores the player type of the opponent of the player "calling" the function
	# i, j, playerRow, playerCol, a, b, c, and d, integers that iterate through for loops to scan the board
	# Algorithm:
	# 1) Store spaceRow and spaceColumn into keySpaceRow and keySpaceColumn
	# 2) Scan the board for the opponent's dice
	# 3) If a die is found and is able to move to the key space coordinates without problems, a block is necessary. Enter
	# more for loops
	# 4) Scan the board for the player's dice
	# 5) If a die is found, see if it can capture the die that threatens to capture the key space. If it can, assign appropriate
	# coordinates into a tuple and return it
	# 6) Otherwise, see if the die can block the offending die's path
	# 7) If the offending die and the key space are in the same row, try to move to a space in between the columns that separate
	# them
	# 8) If the offending die and the key space are in the same column, try to move to a space in between the rows that separate
	# them
	# 9) If a blocking move is possible, assign appropriate coordinates into a tuple and return it
	# 10) Otherwise, return a tuple of 0s
	# Assistance Received: none
	# *********************************************************************
	
	def blockKeySpaceScore(self, board, playerType):
		# Get the key space coordinates and the opponent's player type:
		if (playerType == 'H'):
			keyCoords = (1, 5)
			opponentType = 'C'
		else:
			keyCoords = (8, 5)
			opponentType = 'H'
		
		# See if any of the opponent's dice can occupy it
		for i in range(8,0,-1):
			for j in range(1,10):
				# See if an opponent's die is occupying the space
				if (board.isDieOn(i,j) and board.isDiePlayerType(i, j, opponentType)):
					# See if the die can move to the key space
					if (self.canMoveToSpace(board, i, j, keyCoords[0], keyCoords[1], opponentType)):
						# We need to create a problem/capture the offending die. Scan the board for the player's dice.
						for playerRow in range(8,0,-1):
							for playerCol in range(1,10):
								# See if the player's die is occupying the space.
								if (board.isDieOn(playerRow, playerCol) and board.isDiePlayerType(playerRow, playerCol, playerType)):
									# See if the die can move to the offending die's position.
									if (self.canMoveToSpace(board, playerRow, playerCol, i, j, playerType)):
										# Capture the die.
										return (playerRow, playerCol, i, j)
									# Otherwise try to block the path to the key die.
									# See if the offending die and the key space are in the same row.
									if (keyCoords[0] == i):
										# If the key space column is less than the column of the offending die, it's to the left:
										if (keyCoords[1] < j):
											for a in range(keyCoords[1],j):
												# If we can move to a spot between them, move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, keyCoords[0], a, playerType)):
													# Move there.
													return (playerRow, playerCol, keyCoords[0], a)
										# Otherwise, it's to the right:
										else:
											for b in range(j,keyCoords[0],-1):
												# If we can move to a spot between them, move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, keyCoords[0], b, playerType)):
													# Move there.
													return (playerRow, playerCol, keyCoords[0], b)
									# See if the offending die and the key space are in the same column.
									if (keyCoords[1] == j):
										# If the key space row is less than the row of the die, it's below the die:
										if (keyCoords[0] < i):
											for c in range(keyCoords[0],i):
												# If we can move to a spot between them, move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, c, keyCoords[1], playerType)):
													return (playerRow, playerCol, keyCoords[0], b)
										# Otherwise, it's above the die:
										else:
											for d in range(i, keyCoords[0], -1):
												# If we can move to a spot between them, move there.
												if (self.canMoveToSpace(board, playerRow, playerCol, d, keyCoords[1], playerType)):
													return (playerRow, playerCol, d, keyCoords[1])
		# Blocking is not possible.
		return (0,0)
		
	# *********************************************************************	
	# Function Name: captureDieScore
	# Purpose: To determine if a die can be captured or not
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: a tuple signifying whether or not a die capture is possible
	# Local Variables:
	# opponentType, a character used to store the player type of the opponent of the player "calling" the function
	# i and j, integers used to iterate through for loops
	# Algorithm:
	# 1) Scan the board for the opponent's dice
	# 2) For each die found, scan the board for the player's die
	# 3) For each player die found, see if it can capture the opponent's die
	# 4) If it can, store the coordinates into a tuple and return it
	# 5) Otherwise, if nothing can be found for any of the dice, return a tuple of 0s
	# Assistance Received: none
	# *********************************************************************
	
	def captureDieScore(self, board, playerType):
		# Store the opponent's player type.
		if (playerType == 'H'): opponentType = 'C'
		else: opponentType = 'H'
		# Scan the board for the opponent's dice.
		for i in range(8,0,-1):
			for j in range(1,10):
				# See if an opponent's die is occupying the space.
				if (board.isDieOn(i,j) and board.isDiePlayerType(i,j,opponentType)):
					# Scan the board for the player's dice.
					for playerRow in range(8,0,-1):
						for playerCol in range(1,10):
							# See if a player's die is occupying the space.
							if (board.isDieOn(playerRow, playerCol) and board.isDiePlayerType(playerRow, playerCol, playerType)):
								# See if the die can be moved to the space.
								if (self.canMoveToSpace(board, playerRow, playerCol, i, j, playerType)):
									return (playerRow, playerCol, i, j)
		# Capturing a die is not possible.
		return (0,0)
		
	# *********************************************************************	
	# Function Name: randomMove
	# Purpose: To make a random move on the board
	# Parameters:
	# self, the Player the method is caled on
	# board, the Board that is being played on
	# playerType, a character containing the player type of the player "calling" the function
	# Return Value: none
	# Local Variables:
	# alreadyChecked, a list of boolean values that corresponds to rows already checked on the board
	# randomRow, an integer that stores a random row value
	# rowRolls and columnRolls, integers that store the number of spaces needed to travel from the die's space to the random space
	# topNum, an integer that stores the topNumber of the die
	# Algorithm:
	# 1) Get a random number between 1 and 8.
	# 2) Check the alreadyChecked array to see if that row has already been checked or not.
	# 3) If not, search that row for one of the player's dice.
	# 4) If there is a die there, attempt to make a random move by getting the topNum and assigning it to rowRolls.
	# 5) Try to make the random move in every possible direction before decrementing rowRolls and incrementing columnRolls.
	# 6) Once a move can be made, assign the appropriate coordinates to a tuple and return it.
	# Assistance Received: none
	# *********************************************************************
	
	def randomMove(self, board, playerType):
		# Boolean value list to look at whether or not the row has already been checked.
		alreadyChecked = []
		for boolCheck in range(0,8):
			alreadyChecked.append(False)
		# Random seed.
		random.seed(None)
		# We will enter a semi-permanent while loop to let this perform to the best of its ability. The function
		# returns once a move has been successfully made.
		while True:
			# Get a random number between 1 and 8.
			randomRow = random.randrange(1, 9)
			# Look in the alreadyChecked list to see if the randomly generated number's row has been checked. If not,
			# search the row.
			if (not alreadyChecked[randomRow-1]):
				# Search the row to see if the player's dice are in it.
				for i in range(1,10):
					# If there is a die on the space of the playerType, attempt to make a random move.
					if (board.isDieOn(randomRow, i) and board.isDiePlayerType(randomRow, i, playerType)):
						# Initialize possible moves with row and column traversal.
						topNum = board.getDieTopNum(randomRow, i)
						rowRolls = topNum
						columnRolls = 0
						while (rowRolls > 0):
							# See if a move to the coordinates of the die plus/minus (to the left/right of) the row and column
							# rolls needed to travel is possible. There will be four different ways to move.
							if (self.canMoveToSpace(board, randomRow, i, randomRow+rowRolls, i+columnRolls, playerType)):
								# A move is possible.
								return (randomRow, i, randomRow+rowRolls, i+columnRolls)
							# Try randomRow - rowRolls.
							if (self.canMoveToSpace(board, randomRow, i, randomRow-rowRolls, i+columnRolls, playerType)):
								# A move is possible.
								return (randomRow, i, randomRow-rowRolls, i+columnRolls)
							# Try i - columnRolls.
							if (self.canMoveToSpace(board, randomRow, i, randomRow+rowRolls, i-columnRolls, playerType)):
								# A move is possible.
								return (randomRow, i, randomRow+rowRolls, i-columnRolls)
							# Try randomRow - rowRolls and i - columnRolls.
							if (self.canMoveToSpace(board, randomRow, i, randomRow-rowRolls, randomRow-columnRolls, playerType)):
								# A move is possible.
								return (randomRow, i, randomRow-rowRolls, i-columnRolls)
							# Otherwise, a move is not possible. Try different rows and columns to move by.
							rowRolls -= 1
							columnRolls += 1
				# Check off the row in the list, as it has been checked.
				alreadyChecked[randomRow-1] = True