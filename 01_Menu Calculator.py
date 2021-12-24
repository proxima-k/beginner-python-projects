food_drinks = [  "Chicken Strips", 
			     "French Fries", 
				 "Hamburger", 
				 "Hot Dog", 
				 "Large Drink", 
				 "Medium Drink", 
				 "Milk Shake", 
				 "Salad", 
				 "Small Drink"]


dict_price = {   "Chicken Strips": 3.50, 
			     "French Fries"  : 2.50, 
				 "Hamburger"     : 4.00, 
				 "Hot Dog"       : 3.50, 
				 "Large Drink"   : 1.75, 
				 "Medium Drink"  : 1.50, 
				 "Milk Shake"    : 2.25, 
				 "Salad"         : 3.75, 
				 "Small Drink"   : 1.25}
				 
total_price = 0

orders_dict = {}


def ready_order():

	print("\nWelcome. Here's the menu of our restaurant, Mr/Mrs.")			 
	for i in range(1,10):
		print(str(i) + " " + food_drinks[i - 1] + " $" + str(dict_price[food_drinks[i - 1]]))

	ready = input("If you are ready to order, just type OK.\n")
	
	while ready.lower() != "ok":
		ready = input("You should type ok when you are ready to order. \nTake your time.\n")

def ask_order():
	
	ask = input("What's your order? Type in numbers(1 to 9). \nIf you want the same item, type the same number. E.g. 4455)\n")
	return ask
	
def calculation():

	sub_price = 0
	
	for number in order:
	
		if int(number) in range(1,10):
			sub_price += dict_price[food_drinks[int(number) - 1]]
		else:
			print("Warning: This Food code cannot be found, skipping order.", number)
			
	return sub_price

def order_lists():

	sub_order_list = {}

	for number in order:
		if food_drinks[int(number) - 1] not in sub_order_list:	
			sub_order_list[food_drinks[int(number) - 1]] = 1
		else:
			sub_order_list[food_drinks[int(number) - 1]] += 1
	
	return sub_order_list
				
				
def listing_everything():
	
	print("Your order(s) is/are: ", orders_dict)
	print("The total price for your order is $" + str(total_price) + "\n")
	
def ask_again():
	
	answer_yn = ["yes", "no"]
	
	repeat_ask = input("Anything else to add?(Answer Yes or No)\n")

	while repeat_ask.lower() not in answer_yn:
		repeat_ask = input("You should answer yes or no.\n")

	return repeat_ask

	
def ask_order_2():
	
	ask = input("What's your order? Type in numbers. Same as before.\n")
	return ask
	
	
def order_lists_2():

	sub_order_list = orders_dict

	for number in order:
		if food_drinks[int(number) - 1] not in sub_order_list:	
			sub_order_list[food_drinks[int(number) - 1]] = 1
		else:
			sub_order_list[food_drinks[int(number) - 1]] += 1
	
	return sub_order_list	
	
	
while True:
	ready_order()
	order = ask_order()
	total_price += calculation()
	orders_dict = order_lists()
	listing_everything()

	while True:
		reply = ask_again()
		
		if reply == "yes":
			order = ask_order_2()
			total_price += calculation()
			orders_dict = order_lists_2()
			print("Okay. I will repeat your order(s) again.")
			listing_everything()
		
		else:
			break
		
	input("Okay. Type anything to exit.\nThanks for having your meal at our restaurant.\nHave a nice day!\n")

