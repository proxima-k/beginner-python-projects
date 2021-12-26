# https://github.com/jorgegonzalez/beginner-projects#count-and-fix-green-eggs-and-ham

def check_char(char):
    if char.isalpha() == True:
        return False
    else:
        return True

def correct_I(sentence):
    t = 0
    n_o_correction = 0
    for char in sentence:
        index = sentence.index(char, t)
        if char == "i":
            if index == 0:
                bool_n = check_char(sentence[index+1])
                if bool_n == True:
                    sentence = "I" + sentence[index + 1:]
                    n_o_correction += 1
            else:
                bool_1 = check_char(sentence[index - 1])
                bool_2 = check_char(sentence[index + 1])
                if bool_1 and bool_2 == True:
                    sentence = sentence[:index] + "I" + sentence[index + 1:]
                    n_o_correction += 1
                elif sentence[index-2] in ('.','?','!'):
                    sentence = sentence[:index] + "I" + sentence[index + 1:]
                    n_o_correction += 1

        t += 1

    return sentence, n_o_correction

with open('geah_error.txt', 'r') as rf:
    with open('geah_correction.txt', 'w') as wf:
        total_noc = 0
        for line in rf:
            sentence,noc = correct_I(line)
            total_noc   += noc
            wf.write(sentence)
print(total_noc)

