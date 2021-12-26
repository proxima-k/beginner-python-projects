list_base = ["0"    ,
             "1"    ,
             "2"    ,
             "3"    ,
             "4"    ,
             "5"    ,
             "6"    ,
             "7"    ,
             "8"    ,
             "9"    ,
             "A"    ,
             "B"    ,
             "C"    ,
             "D"    ,
             "E"    ,
             "F"    ]

# for i, j in enumerate(list_base):
#     print(, j)

# print(list(enumerate(list_base)))
def base_10(no_to_10, b_in, l_base):
    l_no = []
    result_value = 0
    for index in no_to_10:
        for i, j in enumerate(l_base):
            if j == index:
                l_no.append(i)
    l_no.reverse()
    for i, j in enumerate(l_no):
        result_value = result_value + ((b_in ** i) * j)

    return int(result_value)

def check_valid(no_, b_in, l_base):
    list_check = []
    for a in no_:
        for i, j in enumerate(l_base):
            if a == j:
                a = i

        if not a in range(0,b_in):
            # print("Error, your number entered is invalid in this base: {}".format(str(base_in)))
            list_check.append("F")      #True
        else:
            # print("Valid for the number you entered in this base: {}".format(str(base_in)))
            list_check.append("T")      #False

    if "F" in list_check:
        return False
    else:
        return True

def convert_again():
    answer_yn = ["yes", "no"]

    repeat_ask = input("Do you still want to convert any number??(Answer Yes or No)\n")

    while repeat_ask.lower() not in answer_yn:
        repeat_ask = input("You should answer yes or no.\n")

    return repeat_ask

def base_l_10(b_to,no_):
    str_     = ""
    while no_ >= b_to:
        remainder_ = int(no_ % b_to)
        str_ = str(remainder_) + str_
        number_ //= b_to
        number_ = int(number_)
        # print(str_)
        # print(number_)
    str_ = str(no_) + str_          # to add the last part
    print(str_)

def base_h_10(no_, b_to, l_base):
    str_    = ""
    while no_ >= b_to:
        remainder_ = int(no_ % b_to)
        for i, j in enumerate(l_base):
            if i == remainder_:
                remainder_ = j
        str_ = remainder_ + str_
        no_ //= b_to
        no_ = int(no_)

    for i, j in enumerate(l_base):
        if i == no_:
            no_ = j

    str_ = str(no_) + str_              #to add the last part
    print(str_)

while True:
    number_  = input("What's the number you'd like to convert?\n")
    base_in  = int(input("What's the base the number's in?\n"))
    base_to  = int(input("What's the base you'd like the number to change to?\n"))

    if check_valid(number_, base_in, list_base) == False:
        print("Error, your number entered is invalid in this base: {}".format(str(base_in)))
        # print(list_check)

    else:
        if base_in != 10:
            number_ = base_10(number_, base_in, list_base)
        else:
            number_ = int(number_)
        print("Base 10: " + str(number_))


        if base_to < 10:
            base_l_10(base_to, number_)

        elif base_to > 10:
            base_h_10(number_, base_to, list_base)

        else:
            print(str(int(number_)))

    reply = convert_again()
    if reply == "no":
        break

input("Thanks for using my base converter!\nType anything to exit.\n")

# expon_ = b_in ** (len(no_to_10) - 1)      #1 0 1
# result_value = 0
# for index in no_to_10:
#     for i, j in enumerate(l_base):
#         if j == index:
#             val_ = i * expon_
#     result_value += val_
#     expon_ /= b_in
# return int(result_value)