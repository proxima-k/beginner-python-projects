# https://github.com/jorgegonzalez/beginner-projects#googlecase
# Finished within one day: 5 Apr 2020
import re

# INPUT
print("Type in the sentence you would like to turn into google case")
print("as well as camel case format.")
string_ = input(">>> ")

def google_case(sentence):
    sentence = sentence.upper()

    pattern = r"(\b[A-Z]+)"
    matches = re.finditer(pattern,sentence)

    for match in matches:
        correction = match.group()[0].lower() + match.group()[1:]
        sentence = re.sub(pattern,correction,sentence,1)

    return sentence

def camel_case(sentence):
    word_list = sentence.lower().split()
    for number, word in enumerate(word_list):
        if number == 0:
            pass
        else:
            word_list[number] = word_list[number].title()

    s = ""
    sentence = s.join(word_list)

    return sentence

# GOOGLE CASE
print()
print("Google case:")
print(google_case(string_))

# CAMEL CASE
print()
print("Camel case:")
print(camel_case(string_))