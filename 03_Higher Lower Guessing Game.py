import random

random_no = 0

guesser_no = 0

guess_attempts = 1

answer_ = "yes"

def welcome():
	input("Welcome to the Guessing Game!\nIn this game, The computer will choose a number (1 to 100) for you to guess.\nIf your guess is incorrect, the computer will tell you whether the number is higher than your guess or lower.\nType anything to continue.\n")
	
def picking_random():
	return random.randint(1,100)
	
def guess():
	numb = input("The computer is picking ...\nAll right! Guess the number!\n")
	return numb
	
def ask_tp():
	return input("Great game! Do you wish to play again?(Answer Yes or No)\n")
	
welcome()	
while answer_.lower() == "yes":
	random_no = picking_random()
	guesser_no = int(guess())
	# if guesser_no > 100:
		# guesser_no = int(input("Out of range.\nGuess in range 1 - 100"))
	while guesser_no != random_no:
		if guesser_no > random_no:
			print("Guesses Taken: ", guess_attempts)
			guesser_no = int(input("Lower!!\n"))
			guess_attempts += 1
			
		elif guesser_no < random_no:
			print("Guesses Taken: ", guess_attempts)
			guesser_no = int(input("Higher!!!\n"))
			guess_attempts += 1

			
	print("Congratz! You guessed the number!", random_no)
	print("Your total number of guesses: ", guess_attempts)
	answer_ = ask_tp()
	guess_attempts = 1

input("Okay! See you next time.")	
