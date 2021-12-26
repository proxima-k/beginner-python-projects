welcome_ = input("Type anything to access to the lyrics of 99 Bottles Of Beer.\n")

no_o_bottles = 99
while no_o_bottles > 1:
    print("{} bottles of beer on the wall, {} bottles of beer.".format(str(no_o_bottles), str(no_o_bottles)))
    no_o_bottles -= 1
    if no_o_bottles > 1:
        print("Take one down and pass it around, {} bottles of beer on the wall.\n".format(str(no_o_bottles)))
    else:
        print("Take one down and pass it around, {} bottle of beer on the wall.\n".format(str(no_o_bottles)))


print("{} bottle of beer on the wall, {} bottle of beer.".format(str(no_o_bottles), str(no_o_bottles)))
no_o_bottles = "no more"
print("Take one down and pass it around, {} bottles of beer on the wall.\n".format(str(no_o_bottles)))

print("{} bottles of beer on the wall, {} bottles of beer.".format(no_o_bottles, no_o_bottles).capitalize())
no_o_bottles = 99
print("Go to the store and buy some more, {} bottles of beer on the wall.".format(str(no_o_bottles)))


