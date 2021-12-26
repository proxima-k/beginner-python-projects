
for i in range(1,1001):
    # >= 2 digits
    if len(str(i)) < 2:
        continue

    # prime
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter != 2:
        continue

    # cannot be 1 and 7
    one_seven = ["1", "7"]
    one_seven_counter = 0
    for x in str(i):
        if x in one_seven:
            one_seven_counter += 1
    if one_seven_counter != 0:
        continue

    # sum of all digits <= 10
    sum = 0
    for x in str(i):
        sum += int(x)
    if sum > 10:
        continue

    # sum of first 2 digits is odd
    str_ = str(i)                                ###### GLOBAL
    sum_ = int(str_[0]) + int(str_[1])
    if sum_ % 2 != 1:
        continue

    # 2nd to last digit is even  #2nd to last digit is > 1
    even_or_odd = int(str_[-2]) % 2
    greater_1 = int(str_[-2])
    if even_or_odd != 0:
        continue
    if greater_1 <= 1:
        continue

    # last digit = digits in a number
    totaldigits = len(str_)
    if int(str_[-1]) != totaldigits:
        continue


    print("The number is: {}".format(i))
