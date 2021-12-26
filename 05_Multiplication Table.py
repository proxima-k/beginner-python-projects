print("Welcome to the Multiplication Table!")

size_of_table = input("Type in the size of the table you want.\n")
size_of_table = int(size_of_table)


spaces_needed = len(str(size_of_table * size_of_table)) + 2

# print(spaces_needed * ' ' + "hi")

# while True:
print(spaces_needed * ' ', end="")
for x in range(1, size_of_table + 1):
    vars_ = str(x)
    space_to_put = spaces_needed - len(vars_)
    print(x, end= " " * space_to_put)
#     if len(vars_) == 2:
#         print(x, end="    ")
#     else:
#         print(x, end="     ")
print(end="\n")
#     break


for i in range(1, size_of_table + 1):                   
    var_ = str(i)
    space_to_put = spaces_needed - len(var_)
    print(i, end= " " * space_to_put)

#     if len(var_) == 2:
#         print(  i , end = "    ")
#     elif len(var_) == 3:
#         print(  i , end = "   ")
#     else:
#         print(  i , end = "     ")

    for j in range(1, size_of_table + 1):
        var_2 = str( i * j )
        space_to_put = spaces_needed - len(var_2)
        print(i*j, end=" " * space_to_put)
#         if len(var_2) == 2:
#             print( i * j , end="    ")
#         elif len(var_2) == 3:
#             print( i * j , end="   ")
#         else:
#             print( i * j , end="     ")

        if j == size_of_table:
            print(end="\n")

exit_ = input("Type anything to exit!\n")


