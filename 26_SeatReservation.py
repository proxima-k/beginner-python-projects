# https://github.com/jorgegonzalez/beginner-projects#seat-reservation
# FINISH WITHIN ONE DAY - 24.3.20

class Seat:
    # INITIATE THE PROGRAM
    def __init__(self):
        self.list = ["-"] * 9
        self.main_event()
        print("\nHave a nice day!")

    # DISPLAYING THE SEATS
    def show(self):
        print("\n|----[CINEPLEX]----|")
        counter = 0
        for number, seat in enumerate(self.list,1):
            counter += 1
            if counter == 3:
                print(" " + str(number) + seat,end="\n")
                counter = 0
            else:
                print(" " + str(number) + seat,end="     ")

    # RESERVING THE SEATS
    def reserve_seats(self,selection):
        print("\n|---------------------------------------------------------|")
        for x in selection:
            if self.list[int(x)-1] == "X":
                print(f"-> Looks like the seat, {x} you wished to reserve has been occupied.")
            else:
                self.list[int(x)-1] = "X"
                print(f"-> Here's the tickets with the seat number,{x} you reserved.")

    # CHECKING IF THE SEATS ARE FULLY OCCUPIED
    def is_occupied(self):
        number_X = self.list.count("X")
        if number_X == 9:
            return True
        else:
            return False

    # ASK IF THE CASHIER WANTS TO RESERVE ANY SEATS FOR CUSTOMERS
    def is_reserve(self):
        print("\n|------------------------------|")
        answer = self.get_input("Do you wish to reserve again?\n(Type y or n)")
        while True:
            if answer.lower() == "y":
                return True
            elif answer.lower() == "n":
                return False
            else:
                answer = self.get_input("Just type y or n.")

    # MAIN EVENT
    def main_event(self):
        while True:
            # SHOWING SEATS
            self.show()

            # USER INPUT
            no_of_seats = self.get_input("Which seat(s) would you want to reserve??\n(e.g. If you want to reserve seat 1 and 5, you should type 15)")
            while True:
                if not no_of_seats.isdigit():
                    no_of_seats = self.get_input("Just type numbers")
                else:
                    break

            # RESERVING THE SEATS
            self.reserve_seats(no_of_seats)


            # CHECKING IF THE SEATS ARE FULLY OCCUPIED
            if self.is_occupied():
                print("\n|-----------------------------------|")
                print("- Looks like the seats are occupied.")
                break

            # RESERVE AGAIN?
            if not self.is_reserve():
                break

    # A FORMAT FOR GETTING INPUTS
    def get_input(self,sentence):
        return input(f"{sentence}\n>>> ")

program = Seat()