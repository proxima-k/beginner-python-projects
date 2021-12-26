# https://github.com/jorgegonzalez/beginner-projects#hangman-game

import random

# IMPORTING
hangmanImage = [
"""+----+
|    |
|    
|   
|   
|
==========""",
"""+----+
|    |
|    O
|   
|   
|
==========""",
"""+----+
|    |
|    O
|    |
|   
|
==========""",
"""+----+
|    |
|    O
|   /|
|   
|
==========""",
"""+----+
|    |
|    O
|   /|\\
|   
|
==========""",
"""+----+
|    |
|    O
|   /|\\
|   / 
|
==========""",
"""+----+
|    |
|    O
|   /|\\
|   / \\
|
=========="""
]
with open("wordslist.txt", "r") as rf:
    words = rf.read()
    words_list = words.splitlines()

# GETTING RANDOM WORD
def getRandomWord(list):
    return random.choice(list)

# DISPLAY
def displayBoard(state,dash,statement):
    print("____________________")
    print(state)
    print("Number of correct guesses: {}".format(statement[0]))
    print("Number of wrong guesses: {}".format(statement[1]))
    print("Word to guess: " + dash)

# CHECKING IF THE USER TYPED ONLY ONE LETTER
def checkGuess(guess, aguess):
    while True:
        if guess == "QUIT":
            return guess
        else:
            if len(guess) != 1:
                guess = input("You are only allowed to type one letter.\nEnter here: ")
            elif guess in aguess:
                guess = input("You've already guessed that letter. Pick again.\nEnter here:")
            elif guess.isalpha() == False:
                guess = input("Type a LETTER.\nEnter here: ")
            else:
                return guess

# CHECKING FOR THE MATCHING WORDS
def checkWord(guess,dash,secret,aguess):
    t = 0
    for char in secret:
        if guess == char:
            index = secret.index(guess,t)
            if index == 0:
                dash = guess + dash[index+1:]
            elif index == (len(secret)-1) :
                dash = dash[:index] + guess
            else:
                dash = dash[:index] + guess + dash[index+1:]
        else:
            pass
        t += 1

    if guess in secret:
        boolean = True
    else:
        boolean = False

    aguess.append(guess)

    return dash, boolean, aguess

# REPLAY THE GAME
def replay():
    while True:
        ask = input("Do you want to play again? (Type y or n)\n")
        if ask == "y":
            running = True
            break
        elif ask == "n":
            running = False
            break
        else:
            ask = input("Type only y or n\n")

    return running

# GAME
def main_event():
    # VARIABLES
    wordToGuess = getRandomWord(words_list)
    dash_word = '-' * len(wordToGuess)
    alreadyGuessed = []
    chance = 0
    ended = False
    statementlist = [0,0]

    # GAME
    print("H A N G M A N")
    while True:
        # DISPLAY
        displayBoard(hangmanImage[chance],dash_word,statementlist)
        # INTERACTING WITH USER
        guess = input('Pick a letter! or type QUIT to exit the game.\nEnter here: ')

        # CHECKING IF THE USER IS FOLLOWING INSTRUCTIONS
        guess = checkGuess(guess,alreadyGuessed)

        # CHECKING THE WORD
        dash_word, correctOrWrong, alreadyGuessed = checkWord(guess,dash_word,wordToGuess,alreadyGuessed)

        # CHECKING THE GUESS IS CORRECT OR WRONG
        if correctOrWrong == False:
            chance += 1
            statementlist[1] += 1
        else:
            statementlist[0] += 1

        # ENDING THE GAME
        if chance == 6:
            print("_____________________")
            print(hangmanImage[chance])
            print("Oops. Looks like you've lost.")
            print("The word you were guessing was: {}".format(wordToGuess))
            print("Number of correct guesses: {}".format(statementlist[0]))
            print("Number of wrong guesses: {}".format(statementlist[1]))
            ended = True
        elif "-" not in dash_word:
            print("___________________")
            print("Congratz! You won!")
            print("The word was: {}".format(wordToGuess))
            print("Number of correct guesses: {}".format(statementlist[0]))
            print("Number of wrong guesses: {}".format(statementlist[1]))
            ended = True
        if ended == True:
            break

        # EXIT
        if guess == "QUIT":
            return True
            # break
        print()


# THE WHOLE GAME
running = True
while running:
    quit_game = main_event()
    if quit_game == True:
        break
    else:
        running = replay()

print("Thanks for playing!")
