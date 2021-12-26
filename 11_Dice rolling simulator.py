from tkinter import *
import random
import time

# Function that ask the user to continue using the app or not
def repeat():
    answer_yn = ["y", "n"]

    repeat_ask = input("\nDo you still want to roll dice(s) again?\nAnswer y(yes) or n(no).\n")

    while repeat_ask.lower() not in answer_yn:
        repeat_ask = input("You should answer y or n.\n")

    return repeat_ask

# Function that returns a list of randomly-generated numbers
def random_dice(noOfSides, noOfDices):

    list_generatedNumber = list()

    for x in range(1, noOfDices + 1):
        list_generatedNumber.append(random.randint(1, noOfSides))

    # print(list_generatedNumber)
    return list_generatedNumber

# Check if the number is available
def check(x,ask_1or2):
    if ask_1or2 == 1:
        while True:
            try:
                x = int(x)
                break
            except ValueError:
                x = input("You are not typing real numbers. Please type a real number.\n")
        return x


ask = input("Which one do you want to use? (Type numbers)\n(1) Dice Rolling Simulator\n(2) Dice Roller?\n")

if ask == "1":
    while True:
        # How many sides should the dice have?
        dice_sides = input("How many sides do you want your dice to have?\n")
        dice_sides = check(dice_sides, 1)

        # How many times the dice should be rolled?
        roll_times = input("How many times should the dice be rolled?\n")
        roll_times = check(roll_times, 1)

        # List that contains the results of the randomly-generated numbers
        results = random_dice(dice_sides, roll_times)

        # Storing the random numbers generated into a dictionary
        dict_value = {}
        for x in results:
            if not str(x) in dict_value:
                dict_value[str(x)] = 1
            else:
                dict_value[str(x)] += 1

        # Interactive
        print("Please wait for a moment...\nThe program is simulating the dice(s)...\n")
        time.sleep(1.5)

        # Printing
        for number, times in dict_value.items():
            percentage = (times / roll_times) * 100
            percentage = round(percentage, 2)
            print("Number: {} - Appeared {} time(s). Percentage: {}%".format(number, times,percentage))

        reply = repeat()
        if reply.lower() == "n":
            break

else:
    window = Tk()
    window.title("Dice Roller")

    frame = Frame(window, width=410, height=270)
    frame.pack_propagate(0)
    frame.pack(padx=5, pady=5)
    frame.configure(bg="black")

    # welcome!
    label_1 = Label(frame, text="Welcome to Dice Roller!", font="Fixedsys 20 bold", bg="black", fg="white")
    label_1.pack(pady=5, side=TOP)

    # question dice
    label_2 = Label(frame, text="How many dices?(Limit:1-4)", font="Fixedsys 15", bg="black", fg="white")
    label_2.pack()

    # dice number
    entry_no_of_dices = Entry(frame, width=10, font="Fixedsys")
    entry_no_of_dices.pack(pady=5)

    # text box
    output = Text(frame, width=28, height=4, bg="white", fg="black", font="Fixedsys 12")
    output.pack(pady=10)

    # submit dice number
    def roll():
        no_of_dices = entry_no_of_dices.get()
        output.delete(0.0, END)
        try:
            no_of_dices = int(no_of_dices)
            if not no_of_dices in range(1, 5):
                output.insert(END, "You can only use 1-4 dices!!")
            else:
                list_randint = random_dice(6, no_of_dices)
                for x, y in enumerate(list_randint, 1):
                    output.insert(END, "Dice {}: {}\n".format(x, y))

        except ValueError:
            output.insert(END, "Type real numbers please.")

    # button roll              #todo: MAKE IT ROLL AGAIN
    button_roll = Button(frame, text="ROLL", font="Fixedsys 12 bold", command=roll, bg="grey", fg="white")
    button_roll.pack(pady=7)

    # quit window
    def quit():
        window.destroy()

    button_quit = Button(frame, text="QUIT", font="Fixedsys 12 bold", command=quit, bg="grey", fg="white")
    button_quit.pack()

    window.mainloop()
