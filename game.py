from tournament import Tournament
from human import Human
from computer import Computer
from boardview import BoardView
from board import Board
from die import Die
import random
import os.path

class Game(object):

	def __init__(self):
		"""Default constructor"""
		self.gameTournament = Tournament()
		self.gameBoard = Board()
		self.gameDisplay = BoardView()
		self.humanPlayer = Human()
		self.computerPlayer = Computer()
		self.currentPlayer = ""
		self.nextPlayer = ""
		
	# *********************************************************************	
	# Function Name: startScreen
	# Purpose: To display the start of the program and see what the user wants to do
	# Parameters:
	# self, the Game the method is called on
	# Return Value: an integer that represents what the player wants to do
	# Local Variables:
	# userInput, an integer that stores the user's answer to the start screen's squestion
	# Algorithm:
	# 1) Print the name of the game
	# 2) Ask the user if they would like to begin a new game, continue a saved game, or quit the program
	# 3) Accept input until the input is valid
	# 4) Return the number that the user inputs
	# Assistance Received: none
	# *********************************************************************
	
	def startScreen(self):
		# Input that determines what the user wants to do upon booting the game.
		userInput = 0
		# Print a welcome message.
		print("Welcome to Duell! The Game of Champions!")
		print("")
		# Ask the user what they want to do.
		print("What would you like to do? Enter the corresponding number to make your decision:")
		print("1: Begin a new game")
		print("2: Continue a saved game")
		print("3: Quit")
		print("")
		# Enter a while loop and let the player decide what they want to do:
		while (userInput < 1 or userInput > 3):
			userInput = input("")
			userInput = int(userInput)
			# Check for valid input.
			if (userInput < 1 or userInput > 3):
				# If not, ask again.
				print("Input not recognized. Please enter a number that corresponds to the options above.")
		
		# Return the input that the user entered.
		return userInput
		
	# *********************************************************************	
	# Function Name: setUpGame
	# Purpose: To set up a new round of Duell
	# Parameters:
	# self, the Game the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Call setUpDice() to set up the dice on the board in the appropriate starting positions
	# 2) Call updateBoard() to update the BoardDisplay object
	# 3) Determine who goes first in the game using determineFirstMove()
	# Assistance Received: none
	# *********************************************************************
	
	def setUpGame(self):
		# Clear the dice on the board.
		self.gameBoard.clearBoard()
		# Set up the dice on the board.
		self.gameBoard.setUpDice()
		# Update the BoardView.
		self.gameDisplay.updateBoard(self.gameBoard)
		# Determine who goes first.
		self.determineFirstMove()
		
	# *********************************************************************	
	# Function Name: determineFirstMove
	# Purpose: To determine who will go first in a new round of Duell
	# Parameters:
	# self, the Game the method is called on
	# Return Value: none
	# Local Variables:
	# player1DieToss and player2DieToss, integers that will contain a random number between 1 and 6
	# Algorithm:
	# 1) Store random numbers in player1DieToss and player2DieToss
	# 2) Output to the window that a die toss is occurring to determine who goes first
	# 3) If the numbers are the same, keep generating random numbers until they are not
	# 4) Output what each player rolled
	# 5) If player1DieToss is higher, the human will go first
	# 6) Otherwise, the computer will go first
	# 7) Assign to the currentPlayer pointer the winner of the die toss, and the loser to nextPlayer
	# Assistance Received: none
	# *********************************************************************
	
	def determineFirstMove(self):
		# Random seed.
		random.seed(None)
		# Die toss results of the players.
		humanDieToss = random.randrange(1,7)
		computerDieToss = random.randrange(1,7)
		print("The round will begin with a die toss. The player with the highest number goes first.")
		# If the players happen to roll the same number, another toss must be performed.
		while humanDieToss == computerDieToss:
			print("Both players rolled a " + str(humanDieToss) + "! Re-rolling...")
			humanDieToss = random.randrange(1,7)
			computerDieToss = random.randrange(1,7)
		print("The Human rolled a " + str(humanDieToss) + " and the Computer rolled a " + str(computerDieToss) + ".")
		
		# Print the winner of the toss.
		if humanDieToss > computerDieToss:
			print("The Human goes first!")
			self.currentPlayer = "Human"
			self.nextPlayer = "Computer"
		else:
			print("The Computer goes first!")
			self.currentPlayer = "Computer"
			self.nextPlayer = "Human"
		
	# *********************************************************************	
	# Function Name: resumeGame
	# Purpose: To resume a game saved to a text file
	# Parameters:
	# self, the Game the method is called on
	# Return Value: a boolean that stores whether or not the game was successfully restored
	# Local Variables:
	# filename, a string that stores the filename of the text file to restore from
	# textFile, the text file to be read from
	# lineBuff, a string that stores a line in a text file
	# Algorithm:
	# 1) Ask the user for the filename of the text file they want to restore their game from
	# 2) Append .txt to the end of the filename
	# 3) Try opening the file. If the file cannot be opened, there is an error. Return false
	# 4) Read the first line of the file. If it is not "Board:" it is an invalid file. Return false
	# 5) Continue reading the next 8 lines, which should be the rows of the board. Call restoreBoard() for each row
	# 6) Get the next couple of lines, skipping over a blank line. Call restorePlayerWins() on the most recent line to restore
	# computer wins
	# 7) Get the next couple of lines, skipping over a blank line. Call restorePlayerWins() on the most recent line to restore
	# human wins
	# 8) Get the next couple of lines, skipping over a blank line. Call restorePlayer() on the most recent line to restore
	# the next player of the game
	# 9) Close the file, update the BoardView, and return true
	# Assistance Received: none
	# *********************************************************************
	
	def resumeGame(self):
		# Ask for the filename.
		filename = input("Please enter the name of the file you want to read from (without .txt): ")
		filename = str(filename)
		# Append .txt to the end
		filename += ".txt"
		
		# First make sure the file exists. If it doesn't, return False for an error.
		if (not os.path.isfile(filename)):
			return False
		
		# The file to be read from. Open it at the same time.
		textFile = open(filename, "r")
		# Buffer to store the line currently being read in the text file.
		lineBuff = ""
		
		# Read the first line from the file.
		lineBuff = textFile.readline()
		lineBuff = lineBuff.rstrip()
		# The very first line should be "Board:". If not, it is an invalid file.
		if (lineBuff != "Board:"):
			print("lineBuff = " + str(lineBuff))
			return False
		
		# Continue reading. The next 8 lines should be board spaces.
		for i in range(8,0,-1):
			lineBuff = textFile.readline()
			lineBuff = lineBuff.lstrip()
			lineBuff = lineBuff.rstrip()
			# If the board is unable to be restored, return False for an error.
			if (not self.restoreBoard(lineBuff, i)):
				return False
		
		# Get the next couple of lines. Skip over one because it will be blank.
		lineBuff = textFile.readline()
		lineBuff = textFile.readline()
		lineBuff = lineBuff.lstrip()
		lineBuff = lineBuff.rstrip()
		# Restore the amount of wins for the computer player.
		if (not self.restorePlayerWins(lineBuff)): return False
		# Get the next couple of lines. Skip over one because it will be blank.
		lineBuff = textFile.readline()
		lineBuff = textFile.readline()
		lineBuff = lineBuff.lstrip()
		lineBuff = lineBuff.rstrip()
		# Restore the amount of wins for the human player.
		if (not self.restorePlayerWins(lineBuff)): return False
		# Get the next couple of lines. Skip over one because it will be blank.
		lineBuff = textFile.readline()
		lineBuff = textFile.readline()
		lineBuff = lineBuff.lstrip()
		lineBuff = lineBuff.rstrip()
		# Assign the next player to be the current player.
		if (not self.restorePlayer(lineBuff)): return False
		
		# Close the file.
		textFile.close()
		# Update the BoardView.
		self.gameDisplay.updateBoard(self.gameBoard)
		# No errors. Return true.
		return True
		
	# *********************************************************************	
	# Function Name: restoreBoard
	# Purpose: To restore the status of the board to what it looks like in the text file
	# Parameters:
	# self, the Game the method is called on
	# buff, a string that contains a row on the board
	# row, an integer that contains the number of the row that will be restored on the board
	# Return Value: a boolean that signifies whether or not the board could be successfully restored
	# Local Variables:
	# parsedText, a list that will store the current elements after parsing
	# topNum and rightNum, integers that store the top and right numbers of a die that will be placed on the board
	# i, an integer that iterates through a for loop
	# Algorithm:
	# 1) Parse into parsedText using split()
	# 2) If the first character of the first element in parsedText is H or C, it's a die. Convert the top and right numbers into ints and store them
	# in topNum and rightNum, then place the die on the board
	# 3) If it's a 0, it's an empty space. Do nothing
	# 4) If it's anything else, it's not recognized by the program and will return false
	# 5) If there were no problems, return true
	# Assistance Received: none
	# *********************************************************************
	
	def restoreBoard(self, buff, row):
		# Parse into parsedText.
		parsedText = buff.split()
		parsedText = list(filter(None, parsedText))
		# Enter a loop to get all of the elements in parsedText.
		for i in range(1,10):
			# Get the current space being visited.
			currentSpace = parsedText[i-1]
			# If it is a die name, initialize the die on the board.
			if currentSpace[0] == 'H' or currentSpace[0] == 'C':
				# Get the top and right numbers of the die.
				topNum = int(currentSpace[1])
				rightNum = int(currentSpace[2])
				# Place the die on the board.
				self.gameBoard.placeDie(Die(topNum, rightNum, currentSpace[0]), row, i)
			# If it's a 0, don't place anything, it's an empty space.
			elif currentSpace[0] == "0":
				pass
			else:
				# Not recognized, return an error.
				return False
		# Everything seems to have went well.
		return True
        
	# *********************************************************************	
	# Function Name: restorePlayerWins
	# Purpose: To restore the amount of wins the player has on the board
	# Parameters:
	# self, the Game the method is called on
	# buff, a string that contains a line in the file
	# Return Value: a boolean that signifies whether or not the wins could be successfully restored
	# Local Variables:
	# parsedText, a list that will store the elements in buff after parsing
	# playerName, a string that will store the name of the player
	# winAmount, an integer containing how many times the player has won
	# i, an integer that iterates through a for loop
	# Algorithm:
	# 1) Parse into parsedText using split()
	# 2) Determine who the player is. If it's Human or Computer, keep going. Otherwise, return false
	# 3) Convert to an int and store in winAmount
	# 4) Iterate through a for loop to increment the amount of wins that the player has
	# 5) Return true if all went well
	# Assistance Received: none
	# *********************************************************************
	
	def restorePlayerWins(self, buff):
		# Parse into parsedText.
		parsedText = buff.split()
		parsedText = list(filter(None, parsedText))
		# The player's name.
		playerName = parsedText[0]
		# Check if the name is valid.
		if playerName == "Human" or playerName == "Computer":
			# It's good!
			pass
		# Otherwise, it isn't.
		else: return False
		# The third element should be how many times the player won.
		winAmount = int(parsedText[2])
		# If the amount is somehow negative, return false.
		if winAmount < 0: return False
		# Restore the amount of wins to the player.
		for i in range (0,winAmount):
			if playerName == "Human": self.gameTournament.addHumanPoint()
			else: self.gameTournament.addComputerPoint()
		# Everything went well. Return true.
		return True
		
	# *********************************************************************	
	# Function Name: restorePlayer
	# Purpose: To restore the next player in the game
	# Parameters:
	# self, the Game the method is called on
	# buff, a string that contains a line in the file
	# Return Value: a boolean that signifies whether or not the player could be successfully restored
	# Local Variables:
	# parsedText, a list that will store the elements being parsed
	# Algorithm:
	# 1) Parse into parsedText and check the name of the next player in the list
	# 2) If the name is not Human or Computer, it is invalid. Return false
	# 3) Determine the player. If parsedText is Human, the human is the current player. Otherwise, it's the computer
	# 4) Assign the pointers appropriately
	# 5) Return true if there were no problems
	# Assistance Received: none
	# *********************************************************************
	
	def restorePlayer(self, buff):
		# Parse into parsedText.
		parsedText = buff.split()
		parsedText = list(filter(None, parsedText))
		# If the third element in parsedText is not "Human" or "Computer," the file is invalid
		if (parsedText[2] == "Human" or parsedText[2] == "Computer"):
			# Determine who the player is.
			if parsedText[2] == "Human":
				# Assign the next player.
				self.currentPlayer = "Human"
				self.nextPlayer = "Computer"
			else:
				self.currentPlayer = "Computer"
				self.nextPlayer = "Human"
		else: return False
		
		# Everything went well, return true
		return True
		
	# *********************************************************************	
	# Function Name: playRound
	# Purpose: To go through a round of Duell
	# Parameters:
	# self, the Game the method is called on
	# Return Value: an integer that represents either a human or computer win, or if the game was saved to a file
	# Local Variables:
	# winCondition, an integer that stores the result of checkWinCondition for how the game was won
	# saveAnswer, an integer that stores the answer of whether or not the user wants to save
	# Algorithm:
	# 1) Display the board, the wins of each player, and who is making the next move.
	# 2) While there is no win condition, play through the game.
	# 3) currentPlayer makes a move and the BoardDisplay is updated and printed to the window.
	# 4) If a win condition is detected, the loop will exit.
	# 5) Otherwise, the user will be asked to save the game and the answer stored in saveAnswer. If they choose to save,
	# they will be asked for a filename to save it to. winCondition will be assigned a value that signifies a save game exit
	# and will exit the loop.
	# 6) Otherwise, switch the players and start from the beginning of the while loop.
	# 7) Check the value stored in winCondition for the type of victory. A human win results in returning 1, with 2 for the
	# computer. The function will also output who won the game and how they did.
	# Assistance Received: none
	# *********************************************************************
	
	def playRound(self):
		# The winCondition that will determine if the round is over.
		winCondition = 0
		# Display the board.
		self.gameDisplay.updateDisplay()
		# Display each player's wins.
		self.gameTournament.printWins()
		# Display the next player.
		print("Next Player: " + str(self.currentPlayer))
		print("")
		while winCondition == 0:
			# Make a turn.
			if (self.currentPlayer == "Human"): self.humanPlayer.play(self.gameBoard)
			else: self.computerPlayer.play(self.gameBoard)
			# Update the display.
			self.gameDisplay.updateBoard(self.gameBoard)
			self.gameDisplay.updateDisplay()
			# Print the wins.
			self.gameTournament.printWins()
			# Display the next player.
			print("Next Player: " + str(self.nextPlayer))
			# Check for a win conditon.
			winCondition = self.checkWinCondition()
			# If there is a win condition, break.
			if winCondition > 0: break
			# Otherwise, ask if the human wants to save.
			saveAnswer = 0
			while saveAnswer < 1 or saveAnswer > 2:
				saveAnswer = input("Save your progress? Press 1 to continue playing or 2 to save and quit: ")
				saveAnswer = int(saveAnswer)
				# If the input is invalid, ask again.
				if (saveAnswer < 1 or saveAnswer > 2): print("Input not recognized. Please enter an appropriate number.")
				# If the user wants to save, save and exit the game.
				if (saveAnswer == 2):
					self.saveFile()
					# Exit the loop by letting winCondition be 5.
					winCondition = 5
					break
			# Switch players
			self.switchPlayers()
			print("")
		# Now determine the type of victory/endgame scenario and then return a number that corresponds to adding to a win total.
		# 1 = human win by key die capture. 2 = computer win by key die capture. 3 = human win by key space capture. 4 = computer win by
		# key space capture. 5 = saved game
		if winCondition == 1:
			print("The human has captured the computer's key die. The human wins!")
			return 1
		if winCondition == 2:
			print("The computer has captured the human's key die. The computer wins!")
			return 2
		if winCondition == 3:
			print("The human has captured the computer's key space. The human wins!")
			return 1
		if winCondition == 4:
			print("The computer has captured the human's key space. The computer wins!")
			return 2
		if winCondition == 5:
			print("The game has been successfully saved.")
			return 3
	
	# *********************************************************************	
	# Function Name: registerWinner
	# Purpose: To properly increment the win amount of the player who won the game
	# Parameters:
	# self, the Game the method is called on
	# roundResult, an integer that stores the number that corresponds to who won the game
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) If roundResult is 1, call addHumanPoint()
	# 2) Otherwise, call addComputerPoint()
	# Assistance Received: none
	# *********************************************************************
	
	def registerWinner(self, roundResult):
		if roundResult == 1:
			# human win
			self.gameTournament.addHumanPoint()
		else:
			# computer win
			self.gameTournament.addComputerPoint()
			
	# *********************************************************************	
	# Function Name: displayResults
	# Purpose: To display the results of the tournament and who won overall
	# Parameters:
	# self, the Game the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Print the amount of wins for each player
	# 2) If the human won more than the computer, print that the human was won the tournament
	# 3) If the computer won more than the human, print that the computer was won the tournament
	# 4) If both players won the same amount of times, print that the tournament ends in a draw
	# Assistance Received: none
	# *********************************************************************
	
	def displayResults(self):
		print("The final results of this tournament are:")
		# Display each player's wins.
		self.gameTournament.printWins()
		# If the human has more wins than the computer, the human wins.
		if self.gameTournament.getHumanWins() > self.gameTournament.getComputerWins(): print("The Human is this tournament's winner! Congratulations!")
		# If the computer has more wins than the human, the computer wins.
		elif self.gameTournament.getComputerWins() > self.gameTournament.getHumanWins(): print("The Computer is this tournament's winner! Congratulations!")
		# Otherwise, they're tied.
		else: print("Both players have the same amount of wins. The tournament ends in a draw!")
		
	# *********************************************************************	
	# Function Name: saveFile
	# Purpose: To save the progress of the game to a text file
	# Parameters:
	# self, the Game the method is called on
	# Return Value: none
	# Local Variables:
	# fileName, a string that stores the name of the file that will be saved to
	# textFile, the file that is being created/written to
	# i and j, integers that iterate through for loops
	# Algorithm:
	# 1) Get input from the user on what they would like the filename of the file to be and store it in fileName
	# 2) Append .txt to the end of fileName
	# 3) Open the file using textFile
	# 4) Scan through the board and output what it looks like to the text file
	# 5) Output the number of wins each player has to the text file
	# 6) Output the player that is going next to the text file
	# 7) Close the file
	# Assistance Received: none
	# *********************************************************************
	
	def saveFile(self):
		# Ask the user to create a name for the text file.
		filename = input("Please enter a name for the file you want to save (without .txt): ")
		filename = str(filename)
		filename += ".txt"
		# Open the file.
		textFile = open(filename, "w")
		
		# Start writing the appropriate format to the text file.
		# Files always start with how the board looks.
		textFile.write("Board:\n\t")
		# Now scan the board for dice.
		for i in range(8,0,-1):
			for j in range(1,10):
				# If there is a die on the space, output its name to the file.
				if self.gameBoard.isDieOn(i,j): textFile.write(self.gameBoard.getDieName(i,j)+"\t")
				# Otherwise, it's an empty pass
				else: textFile.write("0\t")
			textFile.write("\n\t")
		
		# Output the number of wins each player has.
		textFile.write("\n")
		textFile.write("Computer Wins: " + str(self.gameTournament.getComputerWins()) + "\n\n")
		textFile.write("Human Wins: " + str(self.gameTournament.getHumanWins()) + "\n\n")
		# Output the next player.
		textFile.write("Next Player: " + str(self.nextPlayer))
		
		
		# We're done! Close the file.
		textFile.close()
		
	# *********************************************************************	
	# Function Name: switchPlayers
	# Purpose: To switch the players so that the next player can make their turn
	# Parameters:
	# self, the Game the method is called on
	# Return Value: none
	# Local Variables:
	# none
	# Algorithm:
	# 1) Determine who the currentPlayer is
	# 2) Assign nextPlayer to currentPlayer
	# 3) Assign currentPlayer to nextPlayer
	# Assistance Received: none
	# *********************************************************************
	
	def switchPlayers(self):
		# If current player is human, switch
		if self.currentPlayer == "Human":
			self.nextPlayer == "Human"
			self.currentPlayer = "Computer"
			return
		# If current player is computer, switch
		else:
			self.nextPlayer = "Computer"
			self.currentPlayer = "Human"
			
	# *********************************************************************	
	# Function Name: checkWinCondition
	# Purpose: To see if a win condition exists on the board
	# Parameters:
	# self, the Game the method is called on
	# Return Value: an integer that corresponds to the type of victory on the board
	# Local Variables:
	# keyDieResult, an integer that stores the result whose key die is no longer on the board
	# Algorithm:
	# 1) Check the key spaces of each player. If there is a die of an enemy type occupying the key space of a player, the game is
	# over
	# 2) If not, check for the key dice of each player. If a player's key die is missing from the board, the game is over
	# 3) Otherwise, if no win conditions exist, return 0
	# Assistance Received: none
	# *********************************************************************
	
	def checkWinCondition(self):
		# Check if key dies are on the board first.
		keyDieResult = self.isKeyDieOnBoard()
		# If the result is 1, the computer's key die is captured and the human wins the game.
		if keyDieResult == 1: return 1
		# If it's 2, the human's key die is captured and the computer wins the game.
		if keyDieResult == 2: return 2
		# Otherwise, it returned 0, which means both key dice are on the board.
		# Now check the key spaces.
		if self.gameBoard.isDieOn(1,5):
			# If the die on the space is not of human type, the computer wins the game.
			if self.gameBoard.isDiePlayerType(1, 5, 'C'): return 2
		if self.gameBoard.isDieOn(8,5):
			# If the die on the space is not of computer type, the human wins the game.
			if self.gameBoard.isDiePlayerType(8, 5, 'H'): return 1
		# Otherwise, no win conditions currently exist. Return 0.
		return 0
		
	# *********************************************************************	
	# Function Name: isKeyDieOnBoard
	# Purpose: To determine if there is a key die missing from the board or not
	# Parameters:
	# self, the Game the method is called on
	# Return Value: an integer that corresponds to a player's key die missing on the board
	# Local Variables:
	# humanKeyDie and computerKeyDie, booleans that contain whether or not a key die is missing
	# i and j, integers that iterate through for loops
	# Algorithm:
	# 1) Scan the board for the key dice
	# 2) If there is a die on the space, check if it's the key die. If it is, check the playerType of it
	# 3) If it's a human key die, humanKeyDie becomes true. If it's a computer key die, computerKeyDie becomes true
	# 4) If the computer's key die is missing, return 1. If the human's is missing, return 2. Otherwise return 0 if they are both
	# on the board
	# Assistance Received: none
	# *********************************************************************
	
	def isKeyDieOnBoard(self):
		# Initialize boolean values for the key dice of each player and if they exist on the board.
		humanKeyDie = False
		computerKeyDie = False
		# Search the board for the dice.
		for i in range(8,0,-1):
			for j in range (1,10):
				# If there is a key die on the space, check its player type
				if self.gameBoard.isKeyDie(i, j):
					# If it is a human type, humanKeyDie is true.
					if self.gameBoard.isDiePlayerType(i, j, 'H'): humanKeyDie = True
					# If it is a computer type, computerKeyDie is true.
					if self.gameBoard.isDiePlayerType(i, j, 'C'): computerKeyDie = True
		# If both are true, return 0.
		if humanKeyDie and computerKeyDie: return 0
		# If humanKeyDie is present but computer's is not, return 1.
		if humanKeyDie and (not computerKeyDie): return 1
		# If humanKeyDie is not present but computer's is, return 2.
		if (not humanKeyDie) and computerKeyDie: return 2