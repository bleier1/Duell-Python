from player import Player
import random

class Computer(Player):
	
	def __init__(self):
		"""Default constructor"""
		self.playerName = "Computer"
		
	# *********************************************************************	
	# Function Name: play
	# Purpose: To let the computer play the game of Duell
	# Parameters:
	# self, the Computer the method is called on
	# board, the Board that is being played on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Use the score functions in Player to determine which move to make
	# 2) Check if a key die can be captured. If so, make the move
	# 3) Check if a key space can be captured. If so, make the move
	# 4) Check if the key die needs to be blocked. If so, make the move
	# 5) Check if the key space needs to be blocked. If so, make the move
	# 6) Check if a die can be captured. If so, make the move
	# 7) Otherwise, make a random move
	# Assistance Received: none
	# *********************************************************************
	
	def play(self, board):
		# The computer needs to decide which die to move. For this, it will look to see if specific scenarios are true or not.
		# The key die results in an immediate win, so find where the human's key die is. If it can be captured, do it.
		scoreResult = self.captureKeyDieScore(board, 'C')
		if (scoreResult[0] != 0):
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "keyDieCapture")
			return
		# Key space capture results in a win as well, so see if the computer can travel to it.
		scoreResult = self.captureKeySpaceScore(board, 'C')
		if (scoreResult[0] != 0):
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "keySpaceCapture")
			return
		# Should also recommend defensive moves, like blocking the key die...
		scoreResult = self.blockKeyDieScore(board, 'C')
		if (scoreResult[0] != 0):
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "blockKeyDie")
			return
		# Or blocking the key space...
		scoreResult = self.blockKeySpaceScore(board, 'C')
		if (scoreResult[0] != 0):
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "blockKeySpace")
			return
		# No reason to play defensively at this point. Seek a die capture.
		scoreResult = self.captureDieScore(board, 'C')
		if (scoreResult[0] != 0):
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "dieCapture")
			return
		# Otherwise, random move.
		else:
			scoreResult = self.randomMove(board, 'C')
			# Make the move.
			self.computerMakesMove(board, scoreResult[0], scoreResult[1], scoreResult[2], scoreResult[3], "random")
		
	# *********************************************************************	
	# Function Name: computerMakesMove
	# Purpose: To perform the move the computer wants to make
	# Parameters:
	# self, the Computer the method is called on
	# board, the Board that is being played on
	# dieRow, an integer containing the row of the die the computer wants to move
	# dieColumn, an integer containing the column of the die the computer wants to move
	# spaceRow, an integer containing the row of the space the computer wants to move to
	# spaceColumn, an integer containing the column of the space the computer wants to move to
	# strategy, a string containing the strategy the computer is using to make the move
	# Return Value: none
	# Local Variables:
	# spacesToMove, an integer containing the number on the top of the die to be moved
	# frontalMove and lateralMove, booleans that store whether or not a frontal or lateral move is initially possible
	# secondFrontalMove and secondLateralMove, booleans that store whether or not a frontal or lateral move is possible after a
	# 90 degree turn
	# rowRolls and columnRolls, integers that store how many spaces a die needs to move frontally and laterally to get to the
	# space
	# dieNameBefore and dieNameAfter, strings that store the name of the die before and after it is moved
	# Algorithm:
	# 1) Store the result of getDieTopNum() in spacesToMove.
	# 2) Calculate the rowRolls and columnRolls needed to move to the space.
	# 3) Store the name of the die before it is moved into dieNameBefore.
	# 4) Determine if the die can be moved frontally or laterally from the die coordinates, then again after a 90 degree turn.
	# 5) If both a frontal or lateral move is initially possible, choose which way to go at random.
	# 6) Make the move.
	# 7) Store the name of the die after it is moved into dieNameAfter.
	# 8) Call printMove() to print the move the computer just made to the window.
	# Assistance Received: none
	# *********************************************************************
	
	def computerMakesMove(self, board, dieRow, dieColumn, spaceRow, spaceColumn, strategy):
		# The spaces to move the die.
		spacesToMove = board.getDieTopNum(dieRow, dieColumn)
		# The amount of spaces needed to traverse to the given coordinates.
		rowRolls = abs(spaceRow-dieRow)
		columnRolls=abs(spaceColumn-dieColumn)
		# Boolean values for frontal and lateral moves.
		secondLateralMove = False
		secondFrontalMove = False
		# Name of the die before it is moved.
		dieNameBefore = board.getDieName(dieRow, dieColumn)
		# Random seed.
		random.seed(None)
		
		# Determine if the die can be moved laterally or frontally from its coordinates.
		frontalMove = self.canMoveFrontally(board, dieRow, dieColumn, spaceRow, spacesToMove, 'C')
		lateralMove = self.canMoveLaterally(board, dieRow, dieColumn, spaceColumn, spacesToMove, 'C')
		# Determine 90 degree turns.
		if (frontalMove):
			# If you can move frontally (at first) but you cannot move laterally afterwards and
			# the remaining number of spaces to travel is not 0, you cannot travel to that space.
			if ((not self.canMoveLaterally(board, spaceRow, dieColumn, spaceColumn, columnRolls, 'C')) and (columnRolls != 0)):
				secondLateralMove = False
			else:
				secondLateralMove = True
		if (lateralMove):
			# If you can move laterally (at first) but you cannot move frontally afterwards and
			# the remaining number of spaces to travel is not 0, you cannot travel to that space.
			if ((not self.canMoveFrontally(board, dieRow, spaceColumn, spaceRow, rowRolls, 'C')) and (rowRolls != 0)):
				secondFrontalMove = False
			else:
				secondFrontalMove = True
		
		# Check if both ways are possible. If so, the computer will randomly decide if it wants to move laterally or frontally.
		if ((frontalMove and secondLateralMove) and (lateralMove and secondFrontalMove)):
			# Generate the number 0 or 1 randomly. 0 = frontal move, 1 = lateral move.
			decision = random.randrange(0,2)
			if decision == 0:
				# Make the move.
				self.makeMove(board, dieRow, dieColumn, spaceRow, "frontally")
				self.makeMove(board, spaceRow, dieColumn, spaceColumn, "laterally")
				# Get the name of the die after it moves.
				dieNameAfter = board.getDieName(spaceRow, spaceColumn)
				# Print the computer's move.
				self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally", strategy)
				return
			else:
				# Make the move.
				self.makeMove(board, dieRow, dieColumn, spaceColumn, "laterally")
				self.makeMove(board, dieRow, spaceColumn, spaceRow, "frontally")
				# Get the name of the die after it moves.
				dieNameAfter = board.getDieName(spaceRow, spaceColumn)
				# Print the computer's move.
				self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally", strategy)
				return
		
		# If we can only move frontally, only move frontally.
		if frontalMove and secondLateralMove:
			# Make the move.
			self.makeMove(board, dieRow, dieColumn, spaceRow, "frontally")
			self.makeMove(board, spaceRow, dieColumn, spaceColumn, "laterally")
			# Get the name of the die after it moves.
			dieNameAfter = board.getDieName(spaceRow, spaceColumn)
			# Print the computer's move.
			self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally", strategy)
			return
			
		# If we can only move laterally, only move laterally.
		if lateralMove and secondFrontalMove:
			# Make the move.
			self.makeMove(board, dieRow, dieColumn, spaceColumn, "laterally")
			self.makeMove(board, dieRow, spaceColumn, spaceRow, "frontally")
			# Get the name of the die after it moves.
			dieNameAfter = board.getDieName(spaceRow, spaceColumn)
			# Print the computer's move.
			self.printMove(dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, "frontally", strategy)
			return
			
	# *********************************************************************	
	# Function Name: printMove
	# Purpose: To print the move the computer just made
	# Parameters:
	# self, the Computer the method is called on
	# dieNameBefore, a string containing the name of the die before it was moved
	# dieNameAfter, a string containing the name of the die after it was moved
	# dieRow, an integer containing the row of the die before it was moved
	# dieColumn, an integer containing the column of the die before it was moved
	# spaceRow, an integer containing the row of the die after it was moved
	# spaceColumn, an integer containing the column of the die after it was moved
	# direction, a string containing the direction the die initially moved in
	# strategy, a string containing the strategy the computer used to make the move
	# Return Value: none
	# Local Variables:
	# rowRolls and columnRolls, integers used to store the amount of spaces needed to move frontally and laterally to the space
	# Algorithm:
	# 1) Calculate the rowRolls and columnRolls needed to make the move.
	# 2) Print the name and coordinates of the die before it was moved.
	# 3) Use strategy to print the reasoning that the computer used to make the move.
	# 4) Print the direction that the computer rolled the die in and by how many spaces. Also print whether or not a 90 degree
	# turn was made or not.
	# 5) Use strategy to print the reasoning of why the die was rolled where it was rolled to.
	# 6) Print the new name of the die and where it is now located.
	# Assistance Received: none
	# *********************************************************************
	
	def printMove(self, dieNameBefore, dieNameAfter, dieRow, dieColumn, spaceRow, spaceColumn, direction, strategy):
		# Determine how many spaces were rolled frontally and laterally.
		rowRolls = abs(spaceRow-dieRow)
		columnRolls = abs(spaceColumn-dieColumn)
		
		# Start printing out the move.
		print("The computer picked " + str(dieNameBefore) + " at (" + str(dieRow) + "," + str(dieColumn) + ") to roll because ", end="")
		# The strategy is passed into the parameters from a successful score function.
		if (strategy == "keyDieCapture"):
			print("it was within distance of the human's key die.")
		if (strategy == "keySpaceCapture"):
			print("it was within distance of the human's key space.")
		if (strategy == "blockKeyDie"):
			print("the key die was in danger of being captured, and needed to be blocked.")
		if (strategy == "blockKeySpace"):
			print("the key space was in danger of being captured, and needed to be blocked.")
		if (strategy == "dieCapture"):
			print("it was within distance of a human's die that could be captured.")
		if (strategy == "random"):
			print("it could not determine a decisive move to make, so it made a move at random.")
			
		# Continue printing.
		print ("It rolled it ", end="")
		# Print the direction that the die was rolled in.
		if direction == "frontally":
			print("frontally by " + str(rowRolls), end="")
			# If columnRolls is not 0, it was also rolled laterally.
			if columnRolls != 0:
				print(" and laterally by " + str(columnRolls), end="")
		else:
			print("laterally by " + str(columnRolls), end="")
			# If rowRolls is not 0, it was also rolled frontally.
			if rowRolls != 0:
				print (" and frontally by " + str(rowRolls), end="")
		
		# Finish up printing...
		print(" because ", end="")
		if strategy == "keyDieCapture":
			print("it could capture the key die with this move.")
		if strategy == "keySpaceCapture":
			print("it could capture the key space with this move.")
		if strategy == "blockKeyDie":
			print("it could block the key die with this move.")
		if strategy == "blockKeySpace":
			print("it could block the key space with this move.")
		if strategy == "dieCapture":
			print("it could capture the die with this move.")
		if strategy == "random":
			print("the die was able to make this move without any problems.")
		
		print("The die is now " + str(dieNameAfter) + " at (" + str(spaceRow) + "," + str(spaceColumn) + ").")