# https://github.com/jorgegonzalez/beginner-projects#palidrome

def check_palindrome(no):
    str_number = str(no)
    str_reverse = ''
    for i in str_number:
        str_reverse = i + str_reverse

    if str_number == str_reverse:
        print("It's a Palindrome!")
    else:
        print("It's not a palindrome.")

number = input("What number shall you check??\n")

check_palindrome(number)