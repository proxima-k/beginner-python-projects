# https://github.com/jorgegonzalez/beginner-projects#two-numbers

num_list = [15,2,7,11]
target = 9

def pairedNUMBER(list,target):
    for num in list:
        j = list.index(num) + 1 # 1,2,3
        while j < len(list):    # < 4
            if num + list[j] == target:
                return [list.index(num), j]
            else:
                j += 1
    return "No pair of numbers can sum up to the targeted number."

solution = pairedNUMBER(num_list,target)

print(solution)

