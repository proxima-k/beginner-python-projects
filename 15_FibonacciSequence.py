# https://github.com/jorgegonzalez/beginner-projects#fibonacci-sequence

# LOOPING METHOD
def check_nterm_l(term):
    list_fs = [0,1]

    if term == 0:
        value_of_term = list_fs[0]
    elif term == 1:
        value_of_term = list_fs[1]
    else:
        for x in range(2,term+1):
            value_term = list_fs[x-2] + list_fs[x-1]
            list_fs.append(value_term)

        value_of_term = list_fs[-1]

    return(value_of_term)

# RECURSION METHOD
def check_nterm_r(term,list_fs=[0,1],x=2):
    if x < term:
        value_of_term = list_fs[x-2] + list_fs[x-1]
        list_fs.append(value_of_term)
        x += 1
        check_nterm_r(term,list_fs,x)
    else:
        value_of_term = list_fs[x-2] + list_fs[x-1]
        list_fs.append(value_of_term)

    # return list_fs
    return list_fs[-1]


print(check_nterm_l(10))
print(check_nterm_r(20))