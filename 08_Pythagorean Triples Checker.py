# https://github.com/jorgegonzalez/beginner-projects#pythagorean-triples-checker

def again():
    answer_yn = ["yes", "no"]

    repeat_ask = input("Do you still want to check any triangles?(Answer Yes or No)\n")

    while repeat_ask.lower() not in answer_yn:
        repeat_ask = input("You should answer yes or no.\n")

    return repeat_ask

print("Welcome to the pythagorean triples checker!")

while True:
    print("Type in the triangle's side. (No specific order)")

    _st = int(input("The 1st one?\n")) ** 2    #3
    _nd = int(input("2nd?\n")) ** 2            #4
    _rd = int(input("Last?\n")) ** 2           #5

    one_   = (_st == _nd + _rd)   #3**2 = 4**2 + 5**2 # False
    two_   = (_nd == _st + _rd)
    three_ = (_rd == _st + _nd)
    # print(one_)
    # print(two_)
    # print(three_)

    if one_ or two_ or three_:
        print("It's a pythagorean triangle!")
    else:
        print("It's not a pythagorean triangle.")

    reply = again()
    if reply.lower() == "no":
        break

input("Ok. Thanks for using this checker! Have a nice day.\nType anything to exit.\n")