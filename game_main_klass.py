import random
import time
from cmd import Cmd
import Terminal
import Computer
import Histogram
import Dice
import Player
import Scoreboard

terminal = Terminal()  # global usage

class Main(Cmd):
    prompt = ">> "

    def preloop(self):
        welcome()

    def do_multiplayer(self, _):
        player1, player2=create_players(True)
        scoreboard, dice=init_game(player1, player2)
        terminal.display_clear()

        tracker =1
        while not scoreboard.get_winner():
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker==1:
                print(f"It's {player1.get_name()}'s Turn\n")
            else:
                print(f"It's {player2.get_name()}'s Turn\n")

            choice=validate_option("Choose an option > ","Invalid option!")

            match(choice):
                case 1:
                    terminal.display_clear()
                    cast, sum_score = dice.roll(dice.faces).values()
                    terminal.display_dice(cast)
                    if tracker==1:
                        if (cast[0]==1) and (cast[1] ==1):
                            scoreboard.reset_score(player1.get_name())
                            tracker=2
                            continue
                        if (cast[0]==1) or (cast[1] ==1):
                            tracker=2
                            continue

                        scoreboard.update_score(player1.get_name(),sum_score)
                    else:
                        if (cast[0]==1) and (cast[1] ==1):
                            scoreboard.reset_score(player2.get_name())
                            tracker=1
                            continue

                        if (cast[0]==1) or (cast[1]==1):
                            tracker=1
                            continue

                        scoreboard.update_score(player2.get_name(),sum_score)
                case 2:
                    terminal.display_clear()
                    if tracker==1:
                        tracker=2
                        continue

                    tracker=1
                    continue
                case 3:
                    new_name = validate_name(
                        "Type a new name: ","Name is too short or already in use",
                        scoreboard)

                    if tracker=1:
                        scoreboard.update_name(player1.get_name(),new_name)
                        player1.set_name(new_name)
                    if tracker==2:
                        scoreboard.update_name(player2.get_name(),new_name)
                        player2.set_name(new_name)

                    terminal.display_clear()
                case 4:
                    break
        end_game(scoreboard)

    def do_bot(self, _):
        player1, player2=create_players(False)
        scoreboard, dice=init_game(player1,player2)
        terminal.display_clear()

        terminal.display_computer_menu()
        difficulty = validate_option("Choose computer difficulty -> ", "Invalid option!")
        bot = Computer(difficulty)
        terminal.display_clear()
        tracker=1
        while not scoreboard.get_winner():
            terminal.display_table(scoreboard.get_scores())
            terminal.display_realtime_menu()

            if tracker==2:
                terminal.display_clear()
                print(f"{player2.get_name()} turn")
                bot_decision=random.choice(bot.get_decision_list())

                if bot_decision=="Roll":
                    print(f"{player2.get_name()} chose to roll!\n")
                    cast,sum_score=dice.roll(bot.get_biased_list()).values()
                    terminal.display_dice(cast)

                    if (cast[0] ==1) and (cast[1] ==1):
                        scoreboard.reset_score(player2.get_name())
                        tracker=1
                        print(f"{player2.get_name()} Lost all points :(\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue
                    if (cast[0]==1) or (cast[1] ==1):
                        tracker = 1
                        print(f"{player2.get_name()} lost their turn :/\n")
                        time.sleep(4)
                        terminal.display_clear()
                        continue

                    scoreboard.update_score(player2.get_name(),sum_score)
                    terminal.display_table(scoreboard.get_scores())
                    time.sleep(4)
                    continue
                else:
                    print(f"{player2.get_name()} chose to pass..\n")
                    tracker=1
                    time.sleep(2)
                    terminal.display_clear()
                    continue
            else:
                print("It's your turn!\n")
                choice = validate_option("Choose an option > ", "Invalid option!")

                match(choice):
                    case 1:
                        terminal.display_clear()
                        cast, sum_score=dice.roll(dice.faces).values()
                        terminal.display_dice(cast)

                        if tracker==1:
                            if (cast[0] ==1) and (cast[1]== 1):
                                scoreboard.reset_score(player1.get_name())
                                print("You lost all your points :(")
                                tracker=2
                                time.sleep(4)
                                continue

                            if (cast[0]==1) or (cast[1] ==1):
                                print("You lost your turn and its points :/")
                                tracker=2
                                time.sleep(4)
                                continue

                            scoreboard.update_score(player1.get_name(), sum_score)
                    case 2:
                        if tracker==1:
                            tracker =2
                            continue
                    case 3:
                        new_name=validate_name(
                            "Type a new name: ",
                            "Name is too short or already in use",
                            scoreboard)

                        if tracker==1:
                            scoreboard.update_name(player1.get_name(), new_name)
                            player1.set_name(new_name)
                        terminal.display_clear()
                    case 4:
                        break
        end_game(scoreboard)

    def do_rules(self, _):
        terminal.display_rules()

    def do_credits(self, _):
        print(dedent("""\n
            This project is made by:
            Sara, Sondos and Ali\n
            You may also visit our github repository for more-
\n"""))

    def do_exit(self, _):
        print("See you later!\n")
        return True


def welcome():
    terminal.display_clear()
    terminal.display_title()
    terminal.display_intro_img()
    print("Welcome to Two-Dice Pig, where challenges await!!\n")
    terminal.display_intro_menu()
    print("Type 'help' to view available commands.\n")

def validate_option(prompt,error):
    while True:
        try:
            choice = int(input(prompt))
            if "difficulty" not in prompt:
                if not 0 < choice < 5:
                    raise ValueError
                return choice

            if not 0<choice<4:
                raise ValueError
            return choice
        except ValueError:
            print(error)
            continue

def validate_name(prompt,error,scoreboard):
    forbidden_names = ["Ali (computer)", "Sara (computer)",
                       "Sondos (computer)", "Kalle (computer)"]
    while True:
        name=str(input(prompt))
        if not scoreboard:
            if (len(name)<1) or (name in forbidden_names):
                print(error)
                continue
        else:
            if (len(name)<1 or scoreboard.get_player(name) or
                    name in forbidden_names):
                print(error)
                continue
        return name


def create_players(is_multiplayer):
    if is_multiplayer:
        player1_name=validate_name(
            "Type your name (Player 1): ",
            "Name too short",
            scoreboard=False)

        while True:
            player2_name=validate_name(
                "Type your name (Player 2): ",
                "Name too short or already in use",
                scoreboard=False)
            if player1_name==player2_name:
                print("The name cannot be the same as Player 2's.")
                continue
            break
        player1 = Player(player1_name, False)
        player2 = Player(player2_name, False)
        return player1,player2
    else:
        player1_name = validate_name(
            "Type your name (Player 1): ",
            "Name is too short or can't be used",
            scoreboard=False)

        player2_name=random.choice(
            ["Ali (computer)", "Sara (computer)", "Sondos (computer)", "Kalle (computer)"])

        player1=Player(player1_name, False)
        player2=Player(player2_name, True)
        return player1,player2


def init_game(player1,player2):
    scoreboard = Scoreboard([player1.get_name(), player2.get_name()])
    dice=Dice()
    return scoreboard, dice


def end_game(scoreboard):
    if scoreboard.get_winner():
        terminal.display_clear()
        terminal.display_winner(scoreboard.get_winner())
        terminal.display_table(scoreboard.get_scores())

if __name__ == '__main__':
    Main().cmdloop()
