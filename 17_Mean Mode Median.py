# https://github.com/jorgegonzalez/beginner-projects#mean-median-and-mode
import math

# METHOD FOR ROUNDING
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

# METHODS FOR CHECKING MEAN, MODE, MEDIAN
def check_MEAN(list, round_decimal=0):
    sum = 0
    n = len(list)
    for number in list:
        sum += number
    mean = sum / n
    rounded_mean = round_half_up(mean,round_decimal)
    if round_decimal == 0:
        rounded_mean = int(rounded_mean)
    return rounded_mean

def check_MEDIAN(list):
    list.sort()
    if len(list) % 2 != 0:
        median = list[int(len(list)/2)]
    else:
        median = list[int(len(list)/2) - 1], list[int(len(list)/2)]

    return median

def check_MODE(list):
    dict_MODE = {}
    for i in list:
        if i not in dict_MODE:
            dict_MODE[i] = 1
        else:
            dict_MODE[i] += 1

    largest_no = 0
    for x, y in dict_MODE.items():
        if y > largest_no:
            largest_no = y

    mode = []
    for x, y in dict_MODE.items():
        if largest_no == y:
            mode.append(x)
        else:
            pass

    mode.sort()
    return mode

# INPUT YOUR DESIRED LIST
list = [1,2,3,4,5,6,7,8]

print(check_MEAN(list,3))
print(check_MODE(list))
print(check_MEDIAN(list))