from board import Board

class BoardView(object):

	def __init__(self):
		"""Default constructor"""
		self.gameBoard = Board()
		
	# *********************************************************************	
	# Function Name: updateBoard
	# Purpose: To update the board contained in the class
	# Parameters:
	# self, the BoardView the function is called on
	# board, the Board that needs to be displayed to the window
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Assign the gameBoard value in the class to the Board in the parameters
	# Assistance Received: none
	# *********************************************************************
	
	def updateBoard(self, board):
		self.gameBoard = board
		
	# *********************************************************************	
	# Function Name: updateDisplay
	# Purpose: To update the display of the Board contained in the class to the window
	# Parameters:
	# self, the BoardView the function is called on
	# Return Value: none
	# Local Variables:
	# integers col, i, and j, which are used in for loops to help iterate through the board and create the appropriate display
	# Algorithm:
	# 1) Output the column numbers on the board using a for loop
	# 2) Use two for loops to iterate through the board, with the first loop outputting the row numbers before what is contained
	# in each row
	# 3) If there is a die on the space of the coordinates being visited in the for loop, output the name. Otherwise output 0
	# Assistance Received: none
	# *********************************************************************
	
	def updateDisplay(self):
		# Use a for loop to initialize the column numbers of the board.
		# Properly indent the column numbers first...
		print("\t",end="")
		for col in range (1,10): print(col,"\t",end="")
		print("")
		# Use a for loop to iterate through the spaces on the board
		for i in range (8,0,-1):
			# Display the row number
			print(str(i),"\t",end="")
			for j in range (1,10):
				# If there is a die on the space, print its name.
				if (self.gameBoard.isDieOn(i,j)): print(self.gameBoard.getDieName(i,j), "\t", end="")
				# Otherwise, just print 0.
				else: print("0\t", end="")
			print("")
