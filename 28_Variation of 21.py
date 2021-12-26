# https://github.com/jorgegonzalez/beginner-projects#a-variation-of-21
# Finished on 31 Mar 2020(One day)
import random, time

class Suit:
    def __init__(self,name):
        self.name = name
        self.card_list = ["Ace", "2", "3", "4", "5",
                          "6", "7", "8", "9", "10",
                          "Jack", "Queen", "King"]
        self.card_dict = {}
        self.dict_score()

    # Creates a dict with score values
    def dict_score(self):
        for x in self.card_list:
            if x == "Ace":
                self.card_dict[x] = 1
            elif (x == "Jack"
                    or x == "Queen"
                    or x == "King"):
                self.card_dict[x] = 10
            else:
                self.card_dict[x] = int(x)

class Game:
    def __init__(self):
        self.game_score = 100
        self.main_event()

    def main_event(self):
        # Printing intro
        print("|---[Variation of 21]---|")
        print("Welcome player.")
        print("This game is slightly same with the game Blackjack.")
        print("But with a twist.")
        print("If you don't understand the rules.")
        print("Please read it here.\nhttps://github.com/jorgegonzalez/beginner-projects#a-variation-of-21")
        print("Let's begin.")
        input("Press enter to continue.")
        # Five rounds
        for x in range(5):
            self.spade = Suit("Spades")
            self.heart = Suit("Hearts")
            self.club = Suit("Clubs")
            self.diamond = Suit("Diamonds")
            print(f"\n|-----[Round {x+1}]-----|")
            print(f"@ Your current total score: {self.game_score}")
            print("Drawing cards...\n")
            time.sleep(3)

            # Drawing two cards
            self.round_score = 0
            for x in range(2):
                self.draw_card()
            self.display_rscore()

            # Draw or end turn session
            self.draw_end()

            # Subtraction of scores
            self.game_score -= (21 - self.round_score)

        self.display_gscore()
        print("\nThat's the end of the game. Have a nice day!!")

    def draw_card(self):
        card_suit = random.choice([self.spade,self.heart,self.club,self.diamond])
        name, score = random.choice(list(card_suit.card_dict.items()))
        card_suit.card_dict.pop(name)
        self.round_score += score
        # Displaying the drawn card
        print(f"---> You got a < {name} of {card_suit.name.lower()} >. ")

    # Display scores
    # round_score
    def display_rscore(self):
        print(f"@ You now have a round score of {self.round_score}")
    # game_score
    def display_gscore(self):
        print("\nThat's the end of the game!")
        print("Analysing rank...")
        time.sleep(2)
        print(f"So you have a total game score of {self.game_score}.")
        print(f"With that score, you got {self.ranking()}!")


    # Draw, End turn
    # Draw or end turn session
    def draw_end(self):
        draw_end = True
        while draw_end:
            draw_end = self.again()
            if draw_end == True:
                print("Drawing a card...")
                time.sleep(2)
                self.draw_card()
                self.display_rscore()
            if self.round_score > 21:
                self.round_score = 0
                print("Oops. Looks like you busted.")
                time.sleep(2)
                break
    # Ask the player to draw or end turn
    def again(self):
        ask = get_input('Do you want to draw again or end your turn?\n(Type "draw" or "end")')
        while True:
            if ask.lower() == "draw":
                return True
            elif ask.lower() == "end":
                return False
            else:
                ask = get_input('Just type draw or end.')

    def ranking(self):
        if self.game_score >= 90:
            rank = "A"
        elif self.game_score >= 80:
            rank = "B"
        elif self.game_score >= 70:
            rank = "C"
        elif self.game_score >= 60:
            rank = "D"
        elif self.game_score >= 50:
            rank = "F"
        else:
            rank = "nothing.\nBetter luck next time (0.<)"

        return rank

def get_input(string):
    return input(f"{string}\n>>> ")


game = Game()
