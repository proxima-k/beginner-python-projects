#https://github.com/jorgegonzalez/beginner-projects#change-calculator

def calculate_change(chge):
    dict_money = {"Quarter": 25,
                  "Dime": 10,
                  "Nickel": 5,
                  "Penny": 1}
    dict_change = {}

    if chge > 0:
        for x, y in dict_money.items():
            if chge > y:
                x_needed = chge // y
                chge %= y
                dict_change["{}(s) needed".format(x)] =  x_needed

    return dict_change

def ask_again():
    answer_yn = ["y", "n"]

    repeat_ask = input("Anything else to add?(Answer Y(Yes) or N(No)\n")

    while repeat_ask.lower() not in answer_yn:
        repeat_ask = input("You should answer y or n.\n")

    return repeat_ask

while True:
    money_g    = float(input("What's the money given?\n"))
    item_price = float(input("What's the price or total price of the item(s)?\n"))

    change_    = (money_g - item_price) * 100
    print("Total change: " + str((change_)) + "cents")


    dict_chnge_needed = calculate_change(change_)

    for x, y in dict_chnge_needed.items():
        print(x , int(y))

    if ask_again() == "n":
        break