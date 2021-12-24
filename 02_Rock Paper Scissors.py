import random

player_name = ""

com_list = ["Rock", "Paper", "Scissors"]

random_number = 0

bot_selection = ""

dict_score = {	"You" 		: 0,
				"Computer"	: 0	}

again_ = "yes"

def ask_name():
	
	ask = input("welcome to Rock Paper Scissors Game!\nWhat should i call you?\n")
	
	return ask

	
	
def naming():
	
	reply = input("Ok, {}. Rules are simple. Pick only one of these three:\nRock , Paper, Scissors.\n".format(player_name))
	
	return reply

	
def random_int():
	
	random_no = random.randint(0,2)
	
	return random_no

	
def pick_choice():
	
	return com_list[random_number]

	
def picking_winner():
	
	if selection.lower() != bot_selection.lower():
		if selection.lower() == "rock"    :
			if bot_selection.lower() == "paper":
				win_lose = "The Computer has Destroyed you. AHAHAHAH!!!"
			else:
				win_lose = "Congratz. You won!!!"
				
		if selection.lower() == "paper"   :
			if bot_selection.lower() == "scissors":
				win_lose = "The Computer has Destroyed you. AHAHAHAH!!!"
			else:
				win_lose = "Congratz. You won!!!"
				
		if selection.lower() == "scissors":
			if bot_selection.lower() == "rock":
				win_lose = "The Computer has Destroyed you. AHAHAHAH!!!"
			else:
				win_lose = "Congratz. You won!!!"
				
	else: 
		win_lose = "You chose the same as the computer!!"
	
	return win_lose
	
def casting_():
		
	print("You picked {}....".format(selection.capitalize()))
	print("and The Computer picked {}".format(bot_selection))
	
	print("So...  {}".format(results))

def ask_play():
	
	answer_yn = ["yes","no"]
	
	ask = input("Do you still want to play??(Answer Yes or No)\n")
	
	while ask.lower() not in answer_yn:
		ask = input("You should answer yes or no.\n")
	
	return ask
	
def score_record():
	if results == "The Computer has Destroyed you. AHAHAHAH!!!":
		dict_score["Computer"] += 1
	elif results == "Congratz. You won!!!":
		dict_score["You"] += 1
		
		
	
	
while again_.lower() == "yes":	
	player_name = ask_name()
	selection = naming()
	random_number = random_int()
	bot_selection = pick_choice()
	results = picking_winner()
	casting_()
	score_record()
	print("So, the scoreboard now is:" ,dict_score)
	again_ = ask_play()

print("Ok. See you next time!!")	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
