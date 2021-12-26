# https://github.com/jorgegonzalez/beginner-projects#turn-based-pokemon-style-game
# FINISHED IN ONE DAY - 27(10p.m.), 28 MAR 2020(1.47p.m.)
import random, time

class Move:
    def __init__(self,name,health_change):
        self.move_name = name
        self.health_change_range = list(health_change)

class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100

class Game:
    # INITIALIZE ALL OBJECTS
    def __init__(self):
        # Moves
        self.first_move = Move("Fire Punch", range(18, 26))
        self.second_move = Move("Thunder Strike", range(10, 36))
        self.third_move = Move("Holy Coke", range(16, 26))
        self.move_dict = {"1": self.first_move,
                          "2": self.second_move,
                          "3": self.third_move}

        # Players
        self.computer_obj = Player("Computer")
        self.player_name = self.get_input("First things first.\nWhat's your name, player?")
        self.player_obj = Player(self.player_name)
        self.players_list = [self.player_obj, self.computer_obj]


        # START GAME
        print("Alright, let's get started!")
        time.sleep(2)
        self.start_game()

    # HEALTH CHECK <= 0
    def health_check(self):
        for player in self.players_list:
            if player.health > 100:
                player.health = 100
            elif player.health < 0:
                player.health = 0
                return True
        return False

    # DISPLAYING THE HEALTH OF PLAYERS
    def printing_health(self):
        for player in self.players_list:
            print(f"- {player.name}'s health: {player.health}")

    # SELECTED MOVE
    def move_ANALYSIS(self,player,target_player,move_number):
        move = self.move_dict[str(move_number)]
        health_change = random.choice(move.health_change_range)

        print(f"{player.name} choose {move.move_name}!")

        if move.move_name == "Holy Coke":
            player.health += health_change
            print(f"Recovering {health_change} health.")
        else:
            target_player.health -= health_change
            print(f"Dealing {health_change} damage.")

    # PLAYERS TURN PROCEDURE
    def player_turn(self):
        # SELECT MOVE
        self.printing_health()
        print("\nHere's what you can do:")
        for x, y in self.move_dict.items():
            if y.move_name == "Holy Coke":
                print(x, y.move_name,f"({y.health_change_range[0]}-{y.health_change_range[-1]} Heal)")
            else:
                print(x, y.move_name,f"({y.health_change_range[0]}-{y.health_change_range[-1]} Damage)")

        # ASKING FOR INPUT
        selected_move = self.get_input("- Pick your move.(Type numbers only.)")
        while True:
            if selected_move not in ["1","2","3"]:
                selected_move = self.get_input("- Just pick a number of one of the moves.")
            else:
                break
        self.move_ANALYSIS(self.player_obj,self.computer_obj,selected_move)
    def bot_turn(self):
        self.printing_health()
        print("The computer is selecting a move...")
        time.sleep(2)
        # INCREASING CHANCE TO CAST HEAL
        if self.computer_obj.health <= 35:
            random_move = random.choices([1,2,3],weights=[5,5,11])[0]
        else:
            random_move = random.randint(1,3)
        self.move_ANALYSIS(self.computer_obj,self.player_obj,random_move)

    #### FORMAT FOR GETTING INPUT
    def get_input(self,string):
        return input(f"{string}\n>>> ")

    # MAIN EVENT
    def start_game(self):
        # TAKING TURNS
        game_running = True
        while game_running:
            for player in self.players_list:
                print(f"\n|------[{player.name}'s Turn]-------|")
                if player.name == "Computer":
                    self.bot_turn()
                else:
                    self.player_turn()

                # CHECK IF ANY PLAYER'S HEALTH HAS REACHED 0
                if self.health_check():
                    game_running = False
                    time.sleep(2)
                    print("")
                    break

                time.sleep(2)

        # END OF GAME
        print("|-----[End of Game]-----|")
        self.printing_health()
        time.sleep(2)
        if self.player_obj.health == 0:
            print("Looks like your health has reached 0.")
            print("- You lost T_T")
        else:
            print(f"{self.computer_obj.name}'s health reached 0.")
            print("- Congrats! You won!!")
        print("")

# IF PLAYER WANTS TO PLAY AGAIN
def again_():
    ask = input("Do you want to play again?(Type y or n)\n>>> ")
    while True:
        if ask.lower() == "y":
            return True
        elif ask.lower() == "n":
            return False
        else:
            ask = input("Just type y or n.\n>>> ")

print("- Welcome to a game similar to Pokemon!")
print("- Rules are same, each will take turns to pick a move.")
print("- You'll be facing a bot named Computer!\n")
running = True
while running:
    game = Game()
    running = again_()
print("Ok. Bye! Have a nice day!!")