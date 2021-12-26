# https://github.com/jorgegonzalez/beginner-projects#factors-of-a-number

def factor(number_initial):

    # Counter for prime numbers
    counter = 0

    # Making a list of the factors of the number
    list_factor = list()

    # Making a string of factors of the number
    seperator = ', '

    # Changing the number into negative, only if it is a positive number
    if number_initial > 0:
        number = number_initial * -1
    elif number_initial < 0:
        number = number_initial
    else:
        print("Any number is the factor of 0")
        exit()

    # Adding Factors of the number into a list
    for x in range(number, (-1 * number) + 1):
        try:  # ZeroError
            factor_ = number % x
        except ZeroDivisionError:
            continue

    # Making a factors list
        if factor_ == 0:
            list_factor.append(str(x))

            # Checking whether if the number is a prime number or not
            if x > 0:
                counter += 1

    print("The factor(s) are:", seperator.join(list_factor))

    # Prime number
    if (counter == 2) and (number_initial > 0) == True:
        print("It's a prime number!")

no_ = input("What's the number you would like to know the factor(s) of it?\n")
no_ = int(no_)
factor(no_)



# def factor(number):    #todo: make sure to have only one for loop
#     counter = 0
#     if number > 0:
#         for x in range(1, number + 1):
#             if number % x == 0:
#                 counter +=1
#                 if x == number:
#                     print(str(x))
#                 else:
#                     print(str(x), end= ", ")
#
#         if counter == 2:
#             print("It's a prime number!")
#
#     elif number < 0:
#         for x in range(number, (-1 * number) + 1):
#             try:                                #ZeroError
#                 factor_ = number % x
#             except ZeroDivisionError:
#                 continue
#             if factor_ == 0:
#                 counter += 1
#                 if x == (-1 * number):
#                     print(str(x))
#                 else:
#                     print(str(x), end= ", ")
#
#     else:
#         print("Any number is the factor of 0")
#
# no_ = int(input("What's the number you would like to know the factors of it?\n"))
# factor(no_)