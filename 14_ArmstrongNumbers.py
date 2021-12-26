# https://github.com/jorgegonzalez/beginner-projects#armstrong-number

def check_input(input):
    try:
        val = int(input)
    except ValueError:
        try:
            val = float(input)
        except ValueError:
            val = False
    return val

def asking_input():
    while True:
        value = input("Please insert the number you wanted to test.\n")
        value = check_input(value)
        if value == False:
            print("Your input is not a number, please try again.")
        else:
            break
    return value

def armstrong_CHECK(number):
    value = 0
    for digit in str(number):
        value += int(digit) ** len(str(number))
    if value == number:
        print("It's an Armstrong Number!")
    else:
        print("It's not an Armstrong Number")


running = True
while running:
    val = asking_input()
    armstrong_CHECK(val)
    while True:
        y_n = input('Do you want to check another number?(y or n)\n')
        if y_n.lower() == "y":
            break
        elif y_n.lower() == "n":
            running = False
            break
        else:
            print("Please type only y or n.")
