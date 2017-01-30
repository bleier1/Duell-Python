from player import Player
import random

class Human(Player):
	
	def __init__(self):
		"""Default constructor"""
		self.playerName = "Human"
		
	# *********************************************************************	
	# Function Name: play
	# Purpose: To let the human play the game of Duell
	# Parameters:
	# self, the Human the method is called on
	# board, the Board that is being played on
	# Return Value: none
	# Local Variables:
	# helpAnswer, an integer that stores input of whether the player wants the computer's help or not
	# dieRow and dieColumn, integers that store input of the die that the player wishes to move
	# spaceRow and spaceColumn, integers that store input of the space that the player wishes to move to
	# isValidMove, a boolean that determines if the move the player wants to make is valid or not
	# frontalMove and lateralMove, booleans that store whether or not a frontal or lateral move is initially possible
	# secondFrontalMove and secondLateralMove, booleans that store whether or not a frontal or lateral move is possible after a
	# 90 degree turn
	# rowRolls and columnRolls, integers that store how many spaces a die needs to move frontally and laterally to get to the
	# space
	# answer, a string that stores the answer of whether the player wants to initially move frontally or laterally
	# dieNameBefore and dieNameAfter, strings that store the names of a die before it is moved and after it is moved respectively
	# Algorithm:
	# 1) Ask the player if they want to make a move or get help from the computer. Store result in helpAnswer
	# 2) If helpAnswer is 2, call getHelp
	# 3) Otherwise, enter a while loop to get the coordinates of the die the player wants to move and the space they want to
	# move to
	# 4) Perform necessary checks for the die and space coordinates. If they do not pass, start at the beginning of the loop again
	# 5) Perform checks to see if the die is able to move to the space without problems. If they do not pass, start at the
	# beginning of the loop again
	# 6) See if the die can move laterally or frontally from its position. If it can, check to see if it can move again in a
	# 90 degree turn. Should they pass checks, isValidMove becomes true and the move can be made
	# 7) Get the name of the die before it is moved and store it in dieNameBefore
	# 8) If the human is able to move in either direction at first, ask them which direction they would like to move in
	# 9) Make the move, get the die name after it is moved, and store it in dieNameAfter
	# 10) Call printMove() to output the move that was just made to the window
	# Assistance Received: none
	# *********************************************************************
	
	def play(self, board):
		# Integer to store the answer of whether ot not the human wants help.
		helpAnswer = 0
		# See if the human wants help.
		while helpAnswer != 1:
			helpAnswer = input("Enter 1 to make a move or 2 to get a recommendation from the computer: ")
			# 1 means they want to play:
			if (int(helpAnswer) == 1): break
			# 2 means they want help:
			elif (int(helpAnswer) == 2): self.getHelp(board)
			# Otherwise, not a valid input:
			else: print("Invalid input, please try again.")
		# Boolean value of whether or not a move is valid.
		isValidMove = False
		# Enter a while loop to get the coordinates of the die you want to move and where to move it to:
		while (not isValidMove):
			# Get the coordinates of the die to move
			dieRow = input("Enter the row of the die you want to move: ")
			dieColumn = input("Enter the column of the die you want to move: ")
			spaceRow = input("Enter the row of the space you want to move to: ")
			spaceColumn = input("Enter the column of the space you want to move to: ")
			# Convert to integers
			dieRow = int(dieRow)
			dieColumn = int(dieColumn)
			spaceRow = int(spaceRow)
			spaceColumn = int(spaceColumn)
			# If the coordinates entered are greater than what should be accepted, don't accept them.
			if (dieRow < 1 or dieRow > 8):
				print("A die row cannot be " + str(dieRow) + ". Please enter valid coordinates.")
				continue
			if (dieColumn < 1 or dieColumn > 9):
				print("A die column cannot be " + str(dieColumn) + ". Please enter valid coordinates.")
				continue
			# Otherwise, check the space to see if the human can move from there.
			if (board.isDieOn(dieRow, dieColumn) and board.isDiePlayerType(dieRow, dieColumn, 'H')):
				pass
			else:
				print("You cannot move from (" + str(dieRow) + "," + str(dieColumn) + "). Please enter different coordinates.")
				continue
			# The die coordinates are valid. Check if a move can be made to the space coordinates entered.
			if (not self.canMoveToSpace(board, dieRow, dieColumn, spaceRow, spaceColumn, 'H')):
				print("You cannot move the die to (" + str(spaceRow) + "," + str(spaceColumn) + "). Please enter different coordinates.")
				continue
			else:
				isValidMove = True
		
		# We can make a move. Get the name of the die before it is moved.
		dieNameBefore = board.getDieName(dieRow, dieColumn)
		
		# Get the directions of possible moves.
		rowRolls = abs(spaceRow - dieRow)
		columnRolls = abs(spaceColumn - dieColumn)
		topNum = board.getDieTopNum(dieRow, dieColumn)
		lateralMove = self.canMoveLaterally(board, dieRow, dieColumn, spaceColumn, topNum, 'H')
		frontalMove = self.canMoveFrontally(board, dieRow, dieColumn, spaceRow, topNum, 'H')
		secondFrontalMove = False
		secondLateralMove = False
		if lateralMove:
			if ((not self.canMoveFrontally(board, dieRow, spaceColumn, spaceRow, rowRolls, 'H')) and rowRolls != 0): secondFrontalMove = False
			else: secondFrontalMove = True
		if frontalMove:
			if ((not self.canMoveLaterally(board, spaceRow, dieColumn, spaceColumn, columnRolls, 'H')) and columnRolls != 0): secondLateralMove = False
			else: secondLateralMove = True
		
		# If you can move frontally or laterally first, ask which direction to move in.
		# Player's answer to the direction:
		directionAnswer = 0
		if ((lateralMove and secondFrontalMove) and (frontalMove and secondLateralMove)):
			while ((directionAnswer != 1) and (directionAnswer != 2)):
				directionAnswer = input("Which direction would you like to go in first? Enter 1 for frontally or 2 for laterally: ")
				directionAnswer = int(directionAnswer)
				if (directionAnswer == 1):
					# Move frontally first, then laterally.
					self.makeMove(board, dieRow, dieColumn, spaceRow, "frontally")
					self.makeMove(board, spaceRow, dieColumn, spaceColumn, "laterally")
					# Get the new name of the die.
					dieNameAfter = board.getDieName(spaceRow, spaceColumn)
					# Print the move that was just made.
					self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally")
					return
				elif (directionAnswer == 2):
					# Move laterally first, then frontally.
					self.makeMove(board, dieRow, dieColumn, spaceColumn, "laterally")
					self.makeMove(board, dieRow, spaceColumn, spaceRow, "frontally")
					# Get the new name of the die.
					dieNameAfter = board.getDieName(spaceRow, spaceColumn)
					# Print the move that was just made.
					self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally")
					return
				else:
					# Input not recognized.
					print("Direction not recognized, please reenter where you want to go.")
			
		# If you can only move frontally, only move frontally.
		if (frontalMove and secondLateralMove):
			self.makeMove(board, dieRow, dieColumn, spaceRow, "frontally")
			self.makeMove(board, spaceRow, dieColumn, spaceColumn, "laterally")
			# Get the new name of the die.
			dieNameAfter = board.getDieName(spaceRow, spaceColumn)
			# Print the move that was just made.
			self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally")
		# If you can only move laterally, only move laterally.
		if (lateralMove and secondFrontalMove):
			self.makeMove(board, dieRow, dieColumn, spaceColumn, "laterally")
			self.makeMove(board, dieRow, spaceColumn, spaceRow, "frontally")
			# Get the new name of the die.
			dieNameAfter = board.getDieName(spaceRow, spaceColumn)
			# Print the move that was just made.
			self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally")
			
	# *********************************************************************	
	# Function Name: printMove
	# Purpose: To print the move that was just made by the human to the window
	# Parameters:
	# self, the Human the method is called on
	# dieNameBefore, a string containing the name of the die before it was moved
	# dieNameAfter, a string containing the name of the die after it was moved
	# dieRow, an integer containing the row of the die before it was moved
	# dieColumn, an integer containing the column of the die before it was moved
	# spaceRow, an integer containing the row of the die after it was moved
	# spaceColumn, an integer containing the column of the die after it was moved
	# direction, a string that stores the direction that the die first moved in
	# Return Value: none
	# Local Variables:
	# rowRolls and columnRolls, integers that store the amount of spaces that the die needed to move frontally and laterally
	# Algorithm:
	# 1) Calculate the rowRolls and columnRolls needed to move
	# 2) Print the name of the die before it was moved and where it originally was
	# 3) Use the direction passed into the function to determine how the die was first moved.
	# 4) Check if there was a 90 degree turn that was made by looking at rowRolls and columnRolls. If greater than 0, print
	# the number of spaces moved
	# 5) Print the rest of the sentence: the name of the die after it was moved and where it is now located
	# Assistance Received: none
	# *********************************************************************
	
	def printMove(self, dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, direction):
		# Integers to store spaces traversed in each row and column
		rowRolls = abs(spaceRow-dieRow)
		columnRolls = abs(spaceColumn-dieColumn)
		# Print the name of the die before it was moved
		print(str(dieNameBefore) + " was rolled from square (" + str(dieRow) + "," + str(dieColumn) + ") ", end="")
		# Use the direction passed into the function to determined how the die was rolled.
		if (direction == "frontally"):
			print("frontally by " + str(rowRolls), end="")
			# If columnRolls is not 0 then it was also moved laterally
			if (columnRolls != 0):
				print(" and laterally by " + str(columnRolls), end="")
		else:
			print("laterally by " + str(columnRolls), end="")
			# If rowRolls is not 0 then it was also moved frontally
			if (rowRolls != 0):
				print(" and frontally by "+ str(rowRolls), end="")
		# Display the rest of the sentence.
		print(" to square (" + str(spaceRow) + "," + str(spaceColumn) + "). The die is now " + str(dieNameAfter) + ".")
		
	# *********************************************************************	
	# Function Name: getHelp
	# Purpose: To get help from the computer on a move recommenation
	# Parameters:
	# self, the Human the method is called on
	# board, the Board that is being played on
	# Return Value: none
	# Local Variables:
	# dieRow and dieColumn, integers that store the coordinates of the die to move
	# spaceRow and spaceColumn, integers that store the coordinates of the space to move to
	# Algorithm:
	# 1) Call each score function in Player to help determine a move
	# 2) First try to see if a key die can be captured. If so, recommend the move
	# 3) Then try to see if a key space can be captured. If so, recommend the move
	# 4) Then try to see if the human's key die needs to be blocked. If so, recommend the move
	# 5) Then try to see if the human's key space needs to be blocked. If so, recommend the move
	# 6) Then try to see if an enemy die can be captured. If so, recommend the move
	# 7) Otherwise, just recommend a random move
	# Assistance Received: none
	# *********************************************************************
	
	def getHelp(self, board):
	
		# The computer will determine which of the human's dice that it could move. It needs to check for certain scenarios
		# to make the appropriate move. This is actually quite similar to how Computer.play() works, but it does not actually
		# make moves.
		# The key die results in an immediate win, so find where the human's key die is. If it can be captured, do it.
		scoreResult = self.captureKeyDieScore(board, 'H')
		if (scoreResult[0] != 0):
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "keyDieCapture")
			return
		# Key space capture results in a win as well, so see if the human can travel to it.
		scoreResult = self.captureKeySpaceScore(board, 'H')
		if (scoreResult[0] != 0):
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "keySpaceCapture")
			return
		# Should also recommend defensive moves, like blocking the key die...
		scoreResult = self.blockKeyDieScore(board, 'H')
		if (scoreResult[0] != 0):
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "blockKeyDie")
			return
		# Or blocking the key space...
		scoreResult = self.blockKeySpaceScore(board, 'H')
		if (scoreResult[0] != 0):
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "blockKeySpace")
			return
		# No reason to play defensively at this point. Seek a die capture.
		scoreResult = self.captureDieScore(board, 'H')
		if (scoreResult[0] != 0):
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "dieCapture")
			return
		# Otherwise, random move.
		else:
			scoreResult = self.randomMove(board, 'H')
			# Recommend a move.
			self.recommendMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "random")
			
	# *********************************************************************	
	# Function Name: recommendMove
	# Purpose: To print the move recommendation from the computer
	# Parameters:
	# self, the Human the method is called on
	# board, the Board that is being played on
	# dieRow, an integer that contains the row of the die to move
	# dieColumn, an integer that contains the column of the die to move
	# spaceRow, an integer that contains the row of the space to move to
	# spaceColumn, an integer that contains the column of the space to move to
	# strategy, a string that contains the strategy the computer is recommending
	# Return Value: none
	# Local Variables:
	# spacesToMove, an integer that stores the top number of the die located at (dieRow,dieColumn)
	# rowRolls and columnRolls, integers that store the amount of spaces needed to move frontally and laterally to the space
	# frontalMove and lateralMove, boolean values that store whether or not a frontal or lateral move is initially possible
	# secondFrontalMove and secondLateralMove, boolean values that store whether or not a frontal or lateral move is possible
	# after a potential 90 degree turn
	# Algorithm:
	# 1) Store the result of getDieTopNum in spacesToMove
	# 2) Calculate the rowRolls and columnRolls needed to move to (spaceRow,spaceColumn)
	# 3) Start printing the recommendation using getDieName to get the name of the die to move.
	# 4) Print the recommendation that goes with the strategy passed in the parameters.
	# 5) Use canMoveFrontally and canMoveLaterally to determine how the die can be moved and print how the human can move it.
	# 6) Print the reason for moving the die in that direction using the strategy passed in the parameters.
	# Assistance Received: none
	# *********************************************************************
	
	def recommendMove(self, board, dieRow, dieColumn, spaceRow, spaceColumn, strategy):
		# The spaces to move the die.
		spacesToMove = board.getDieTopNum(dieRow, dieColumn)
		# The amount of spaces needed to traverse the board.
		rowRolls = abs(spaceRow - dieRow)
		columnRolls = abs(spaceColumn - dieColumn)
		# Boolean values for frontal and lateral moves
		secondLateralMove = False
		secondFrontalMove = False
		# Random seed.
		random.seed(None)
		
		# Begin printing the recommenation.
		print("The computer recommends moving " + str(board.getDieName(dieRow, dieColumn)) + " at (" + str(dieRow) + "," + str(dieColumn) + ") because ", end="")
		# Print based on the strategy passed into the function.
		if (strategy == "keyDieCapture"):
			print("it is within distance of the computer's key die.")
		if (strategy == "keySpaceCapture"):
			print("it is within distance of the computer's key space.")
		if (strategy == "blockKeyDie"):
			print("the key die is in danger of being captured, and needs to be blocked.")
		if (strategy == "blockKeySpace"):
			print("the key space is in danger of being captured, and needs to be blocked.")
		if (strategy == "dieCapture"):
			print("it is within distance of a computer's die that can be captured.")
		if (strategy == "random"):
			print("the computer could not determine a decisive move to make, so it is making a move at random.")
		
		# Print the rest of the recommendation.
		print("It recommends rolling ", end="")
		
		# Determine if the die can be moved frontally or laterally.
		frontalMove = self.canMoveFrontally(board, dieRow, dieColumn, spaceRow, spacesToMove, 'H')
		lateralMove = self.canMoveLaterally(board, dieRow, dieColumn, spaceColumn, spacesToMove, 'H')
		# Determine if it can be moved in a 90 degree turn.
		if (frontalMove):
			if ((not self.canMoveLaterally(board, spaceRow, dieColumn, spaceColumn, columnRolls, 'H')) and columnRolls != 0):
				secondLateralMove = False
			else:
				secondLateralMove = True
		if (lateralMove):
			if ((not self.canMoveFrontally(board, dieRow, spaceColumn, spaceRow, rowRolls, 'H')) and rowRolls != 0):
				secondFrontalMove = False
			else:
				secondFrontalMove = True
		# Check if both directions are possible. If so, the computer will randomly decide whether to move frontally or laterally.
		if ((frontalMove and secondLateralMove) and (lateralMove and secondFrontalMove)):
			# Generate 0 or 1 randomly. 0 = frontal move, 1 = lateral move.
			decision = random.randrange(0,2)
			if (decision == 0):
				# Recommend frontal move first
				lateralMove = False
			else:
				# Recommend lateral move first
				frontalMove = False
		
		# Continue the recommendation...
		if (frontalMove and secondLateralMove):
			print("frontally by " + str(rowRolls), end="")
			# If you can also move laterally, describe that as well.
			if (columnRolls != 0): print(" and laterally by " + str(columnRolls), end="")
		if (lateralMove and secondFrontalMove):
			print("laterally by " + str(columnRolls), end="")
			# If you can also move frontally, describe that as well.
			if (rowRolls != 0): print(" and frontally by " + str(rowRolls), end="")
		
		# Finish it up.
		print(" because ", end="")
		
		# Look at the strategy passed into the function once more.
		if strategy == "keyDieCapture":
			print("it can capture the key die with this move.")
		if strategy == "keySpaceCapture":
			print("it can capture the key space with this move.")
		if strategy == "blockKeyDie":
			print("it can block the key die with this move.")
		if strategy == "blockKeySpace":
			print("it can block the key space with this move.")
		if strategy == "dieCapture":
			print("it can capture the die with this move.")
		if strategy == "random":
			print("the die is able to make this move without any problems.")
