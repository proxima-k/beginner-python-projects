# https://github.com/jorgegonzalez/beginner-projects#flames-game
import re, time

# STRIKING WORDS OUT
def strikeWords(person1,person2):
    for char in person1:
        for char2 in person2:
            if char == char2:
                person1 = re.sub(rf"{char}",'',person1,1)
                person2 = re.sub(rf"{char}",'',person2,1)
                break
    return person1, person2

# CALCULATION OF REMAINING WORDS
def calculateWords(person1,person2):
    return len(person1) + len(person2)

# STRIKING THE WORD "FLAMES"
def FLAMES(remainingNumber):
    remainingNo = remainingNumber
    arithmetic = 1
    string = "FLAMES"
    index = 0
    starting_WORD = string[index]
    while True:
        # REVERSING THE STRING
        string = string[::arithmetic]
        sw_index = string.index(starting_WORD)

        # GETTING THE INDEX OF THE LETTER TO BE REMOVED
        if remainingNo > len(string):
            index = remainingNo % len(string) - 1
            if index < 0:
                index = len(string) - 1
        elif remainingNo <= len(string):
            index = remainingNo - 1

        # TO SKIP BACK TO THE TOP OF THE STRING
        if (index+sw_index) > len(string) - 1:   # 2 + 0
            difference = len(string[sw_index:])
            index = index - difference
        else:
            index = index + sw_index

        # STRIKING OUT THE LETTER
        string = re.sub(rf"{string[index]}", "", string, 1)

        # EXITING
        if len(string) == 1:
            break
        else:
            # TAKING THE INDEX OF THE STARTING WORD
            if index != 0:
                starting_WORD = string[index-1]
            else:
                starting_WORD = string[-1]

            if arithmetic != -1:
                arithmetic *= -1
    return string
flamesDict = {"F": "Friends",
              "L": "Lovers",
              "A": "Affection",
              "M": "Marriage",
              "E": "Enemies",
              "S": "Siblings"}

# ASKING TO PLAY AGAIN
def ask():
    ask = input("Do you want to play again? (Type y or n)\n")
    while True:
        if ask.lower() == "y":
            return True
        elif ask.lower() == "n":
            return False
        else:
            ask = input("Just type y or n.\n")

running = True
while running:
    # NAME
    user1 = input("Person 1's name?\nEnter here: ").lower()
    user2 = input("Person 2's name?\nEnter here: ").lower()

    user1 = user1.replace(" ","")
    user2 = user2.replace(" ","")

    print(user1,"+",user2)
    # STIRKING WORDS OUT
    userleft1, userleft2 = strikeWords(user1,user2)
    remainingLetters = calculateWords(userleft1,userleft2)

    print("Analyzing...")
    time.sleep(3)

    flames = FLAMES(remainingLetters)
    print(f"Congrats!! You two are fitted for {flamesDict[flames]}!")

    ans = ask()
    if ans == True:
        pass
    elif ans == False:
        break