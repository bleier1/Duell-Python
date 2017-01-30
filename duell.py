#************************************************************
#* Name : Bryan Leier                                       *
#* Project : Duell Extra Credit: Python                     *
#* Class : CMPS 366 - Organization of Programming Languages *
#* Date : December 8, 2016                                  *
#************************************************************

from game import Game
import sys

# The entire game of Duell.
duellGame = Game()
# Integer value to determine if the player wants to play again.
playAgain = 1
# Boot to the welcome screen and have a variable to store the player's answer.
startScreenResult = duellGame.startScreen()
# If the player wants to play a new game, start a new game.
if startScreenResult == 1: duellGame.setUpGame()
# If the player wants to resume an old game, resume it.
if startScreenResult == 2:
	if (not duellGame.resumeGame()):
		print("There was an error restoring the save file. The program will now exit. Goodbye!")
		sys.exit("Bad file")
# Otherwise, the player wants to exit.
if startScreenResult == 3:
	print("The program will now exit. Goodbye!")
	sys.exit()

# Let's play the round.
# The result of the round will be stored in an integer.
roundResult = 0

# Play until the user doesn't want to play anymore.
while playAgain == 1:
	roundResult = duellGame.playRound()
	# If the result is 3, the user saved the game and the program must quit.
	if roundResult == 3: break
	# Increment the winner's win total.
	duellGame.registerWinner(roundResult)
	# Ask to play again.
	print("Would you like to play another round?")
	playAgain = input("Enter 1 to play again or 2 to quit: ")
	playAgain = int(playAgain)
	# If the input is not valid, ask again:
	while playAgain < 1 or playAgain > 2:
		playAgain = input("Input not recognized. Please enter a number that corresponds to the above choices: ")
		playAgain = int(playAgain)
	# If they want to play again, set up a new round.
	if playAgain == 1: duellGame.setUpGame()
	
# Display the tournament results.
if roundResult != 3: duellGame.displayResults()
print("The program will now exit. Goodbye!")