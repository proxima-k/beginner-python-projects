# https://github.com/jorgegonzalez/beginner-projects#coin-estimator-by-weight

# import math # Was going to use math.ceil
import threading
from threading import Thread

# A class for the types of coins
class Coin_Type:
    def __init__(self, name, price, weight, coin_wrapper, totalweight_given):
        self.name = name
        self.price = price
        self.weight = weight
        self.coinWrapper = coin_wrapper
        self.totalweight = totalweight_given
        self.total_amount = totalweight_given / weight
        self.rounded_amount = round(self.total_amount)

    # Methods to print out the required objectives
    def coinsAmount(self):
        # total_amount = self.totalweight / self.weight
        print("You'll have approximately {} {}(s).".format(self.rounded_amount, self.name))

    def wrappersNeeded(self):
        # total_amount = self.totalweight / self.weight
        wrappers_needed = self.rounded_amount / self.coinWrapper
        # wrappers_needed = math.ceil(wrappers_needed)
        wrappers_needed = round(wrappers_needed)
        print("You'll need {} wrappers for your {}(s).".format(wrappers_needed, self.name))

    def totalMoney(self):
        total_value = (self.rounded_amount * self.price) / 100
        return total_value
        # print("You'll have approximately ${} from your {}(s).".format(total_value, self.name))

    # A method to run methods simultaneously / at the same time.
    def runAll(self):
        if __name__ == '__main__':
            Thread(target = self.coinsAmount()).start()
            Thread(target = self.wrappersNeeded()).start()
            # Thread(target = self.totalMoney()).start()
            print("")

# Function that change pounds to grams
def gramPound(variable_, weight):
    if weight.lower() == "g":
        pass
        return variable_
    elif weight.lower() == "p":
        var_ = variable_ * 454
        return var_

# Asking whether the weight should be measured in pounds or grams.
g_or_p = input("Are you weighing in grams(g) or pounds(p)?\nJust type g or p.\n")

# Asking about the weight of each type of coin.
penny_totalweight = float(input("What is the total weight of your penny(s)?\n"))
nickel_totalweight = float(input("What is the total weight of your nickel(s)?\n"))
dime_totalweight = float(input("What is the total weight of your dime(s)?\n"))
quarter_totalweight = float(input("What is the total weight of your quarter(s)?\n"))

# Making a list to change the unit of the weight of coins
# list_coins = [penny_totalweight, nickel_totalweight, dime_totalweight, quarter_totalweight]
# list_coins = gramPound(list_coins, g_or_p)

# Changing the unit from pounds to grams.
penny_totalweight   = gramPound(penny_totalweight, g_or_p)
nickel_totalweight  = gramPound(nickel_totalweight, g_or_p)
dime_totalweight    = gramPound(dime_totalweight, g_or_p)
quarter_totalweight = gramPound(quarter_totalweight, g_or_p)

# Types of coins to put into a class
coin_penny   = Coin_Type("penny", 1, 2.5, 50, penny_totalweight)
coin_nickel  = Coin_Type("nickel", 5, 5, 40, nickel_totalweight)
coin_dime    = Coin_Type("dime", 10, 2.268, 50, dime_totalweight)
coin_quarter = Coin_Type("quarter", 25, 5.67, 40, quarter_totalweight)

# Running all functions
coin_penny.runAll()
coin_nickel.runAll()
coin_dime.runAll()
coin_quarter.runAll()

# Printing the total value of all the money
total_value = coin_penny.totalMoney() + coin_nickel.totalMoney() + coin_dime.totalMoney() + coin_quarter.totalMoney()
print("You'll have approximately ${} from all of your money.".format(total_value))

