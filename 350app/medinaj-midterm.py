## Jeremy Medina
## CS350 Midterm: Multi-Minigame package 10-4-2016
import sys
import random
list = ['Coin Flip','Dice Roller','Guess the Number']
gametype = '0'

def start():
	global gametype
	while gametype != '-1':
		print ("\n\nWelcome to Jeremy's Midterm Multi-minigame package!\nOur collection of games includes: (1) Coin Flip, (2) Dice Roller, (3) Guess the Number!")
		gametype = (raw_input("\nWhich game would you like to play? (ENTER -1 to quit): "))
		if (gametype == list[0]) | (gametype == '1'):
			coinflip(gametype)
		if (gametype == list[1]) | (gametype == '2'):
			diceroller(gametype)
		if (gametype == list[2]) | (gametype == '3'):
			guessnumber(gametype)
	print("\nThanks for playing! Goodbye!\n\n")
	sys.exit()

def coinflip(gametype):
	print("\nYou chose: Coin Flip!\n")
	flip = 'y'
	j=0
	k=0
	while (1):
		while flip == 'y':
			flip = raw_input("Would you like to flip a coin? (y/n): ")
			if flip == 'n':
				if (j>k):
					print("\nYou got Heads more times than Tails. The total amount of Heads was: "),j,("-- You had"),k,("Tails.")
				if (k>j):
					print("\nYou got Tails more times than Heads. The total amount of Tails was: "),k,("-- You had"),j,("Heads.")
				if ( ((j>0)&(k>0)) & (j==k) ):
					print("\nYou got as many Heads as you did for Tails!"),j,("&"),k
				diffGame = raw_input("\nWould you like to play a different game? (y or -1 to quit): ")
				if diffGame == 'y':
					start()
				if diffGame == '-1':
					print("\nThanks for playing! Goodbye!\n\n")
					sys.exit()
			coin = random.randint(1,2)
			if coin == 1:
				print ("Heads!")
				j+=1
			if coin == 2:
				print ("Tails!")
				k+=1
	
def diceroller(gametype):
	print("\nYou chose: Dice Roller!\n")
	roll = 'y'
	while(1):
		while (roll == 'y') | (roll == 1) | (roll == 2) | (roll == 3) | (roll == 4):
			roll = int(raw_input("How many dice would you like to roll? (You can roll between 1 and 4 dice at the same time, or '-1' to quit): "))
			if roll == -1:
				diffGame = raw_input("Would you like to play a different game? (y or -1 to quit): ")
				if diffGame == 'y':
					start()
				if diffGame == '-1':
					print("\nThanks for playing! Goodbye!\n\n")
					sys.exit()
			if roll == 1:
				dice1 = random.randint(1,6)
				value = (dice1)
				print ("\nYour dice rolled: "),dice1
				print ("The total value of your dice is: "),value,("\n")
			if roll == 2:
				dice1 = random.randint(1,6)
				dice2 = random.randint(1,6)
				value = (dice1+dice2)
				print ("\nYour dice rolled: "),dice1,(","),dice2
				print ("The total value of your dice is: "),value,("\n")
			if roll == 3:
				dice1 = random.randint(1,6)
				dice2 = random.randint(1,6)
				dice3 = random.randint(1,6)
				value = (dice1+dice2+dice3)
				print ("\nYour dice rolled: "),dice1,(","),dice2,(","),dice3
				print ("The total value of your dice is: "),value,("\n")
			if roll == 4:
				dice1 = random.randint(1,6)
				dice2 = random.randint(1,6)
				dice3 = random.randint(1,6)
				dice4 = random.randint(1,6)
				value = (dice1+dice2+dice3+dice4)
				print ("\nYour dice rolled: "),dice1,(","),dice2,(","),dice3,(","),dice4
				print ("The total value of your dice is: "),value,("\n")

def guessnumber(gametype):
	print("\nYou chose: Guess the Number!\n")
	guess = 'y'
	while (1):
		while guess != -1:
			guess = int(raw_input("Pick a number between 1 and 10, and see if you can guess my number! (1-10 or -1 to quit): "))
			if guess == -1:
				diffGame = raw_input("Would you like to play a different game? (y or -1 to quit): ")
				if diffGame == 'y':
					start()
				if diffGame == '-1':
					print("\nThanks for playing! Goodbye!\n\n")
					sys.exit()
			randNum = random.randint(1,10)
			if guess == randNum:
				print ("You guessed my number! The number chosen was: "),randNum,("\n")
			if guess != randNum:
				print ("You guessed incorrectly! The number I chose was: "),randNum,("\n")

start()
