# https://github.com/jorgegonzalez/beginner-projects#scarnes-dice

from random import choice as rchoice
import time

# CLASS TO STORE PLAYER'S INFO
class Player:
    def __init__(self,name):
        self.name = name
        self.turn_score = 0
        self.total_score = 0

# CLASS FOR THE GAME
class Game:

    # INITIATE ATTRIBUTES
    def __init__(self):
        self.player_list = []
        self.dice = [1,2,3,4,5,6]
        self.winner = ""
        self.game_over = False

        # INITIATE THE GAME
        print("Welcome to Scarne's Dice!")
        self.get_player()

    # A FORMAT WHEN GETTING INPUT FROM USER
    def get_input(self, text):
        text = input(f"{text}>>> ")
        return text

    # GETTING THE NUMBER OF PLAYER, NAME OF THE PLAYERS
    def get_player(self):
        no_of_players = "alphabet"
        while not no_of_players.isdigit():
            no_of_players = self.get_input("How many players are there?\n")
        for i in range(int(no_of_players)):
            player_name = self.get_input(f"Name for Player {i+1}?\n")
            self.player_list.append(Player(player_name))
        self.start_game()

    # MAIN EVENT(ROLLING DICE)
    def roll_dice(self,player):
        player.turn_score = 0
        running = True
        while running:
            current_roll = rchoice(self.dice)
            player.turn_score += current_roll
            print(f"- You rolled {current_roll}!(Accumulated score: {player.turn_score})")
            if current_roll == 1:
                print("Oops. Looks like someone got a 1. No points for you!\nNext player!")
                break
            else:
                ask = self.get_input("Roll again or end turn? ")

                # ASKING TO ROLL AGAIN OR END TURN
                while True:
                    if ask == "r":
                        break
                    elif ask == "e":
                        player.total_score += player.turn_score
                        print(f"- Alright. Now you have a total score of {player.total_score}!!")
                        running = False
                        break
                    else:
                        ask = self.get_input("Type only r or e. ")

    # CHECK IF ANY PLAYER EXCEEDS OR EARNED 100 POINTS
    def game_over_check(self,player):
        if player.total_score >= 100:
            self.winner = player.name
            return True
        else:
            return False

    # DISPLAYING SCORES AND INTERACTION
    def start_game(self):
        print(f"\nSo we have {len(self.player_list)} players. Let's begin!")
        while not self.game_over:
            number = 1
            for player in self.player_list:
                print("\n--------------------")
                print(f"- Player {number}")
                print(f"- {player.name}'s turn.")
                print(f"- Current total score: {player.total_score}")
                self.roll_dice(player)
                self.game_over = self.game_over_check(player)
                number += 1
                time.sleep(1)
                if self.game_over == True:
                    break
        print("")
        print(f"- Looks like we got a winner!\n- Congrats, {self.winner}!!\n")

# ASKING WHETHER THE USER WANTS TO PLAY THE GAME AGAIN
def yesOrNo():
    y_n = input("Do you still want to play again?(y or n) >>>")
    if y_n == "y":
        return True
    elif y_n == "n":
        return False
    else:
        y_n = input("Do you still want to play again?(y or n) >>>")

# RUNNING THE GAME
game_run = True
while game_run:
    game = Game()
    game_run = yesOrNo()
