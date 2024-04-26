import os
import platform
from pathlib import Path
import climage
import art
import tabulate

class Terminal:
    def __init__(self):
        self.assets_path = (Path(__file__).parent).joinpath('img')

    def display_title(self):
        return print(art.text2art("TWO  DICE  PIG", font="tarty3"))

    def display_intro_img(self):
        return print(
            climage.convert(
                f'{self.assets_path}/dice_intro.jpg',
                is_unicode=True,
                width=61,
                palette="gruvbox"
            )
        )

    def display_prompt(self, text):
        value = input(f"{text} > ")
        return value

    def display_intro_menu(self):
        return print(dedent("""\
                    - Player vs Player | (multiplayer)
                    - Player vs Bot | (bot)
                    - View game rules | (rules)
                    - Exit | (exit)\n"""))

    def display_computer_menu(self):
        return print("1. Easy\n2. Moderate\n3. Hard\n")

    def display_realtime_menu(self):
        return print(dedent("""\
                    1. Roll the dice
                    2. Pass
                    3. Change name
                    4. Exit current game\n"""))

    def display_rules(self):
        return print(dedent("""\
                    Here's a brief description of how to play the game:

                    The game is played by two players or against the computer, and each turn consists of a player rolling two six-sided dice.
                    The player's score for that turn is the sum of the numbers rolled on the dice.
                    The player can choose to roll again and add the new sum to their current score, or they can choose to end their turn and keep their current score.
                    If the player rolls a one on either of the dice, their turn ends and their score for that turn is zero.
                    If the player rolls a one on both of the dice, their turn ends and their entire score during that round will be lost.
                    The first player to reach a predetermined winning score (100 points) wins the game..\n"""))

    def display_dice(self, faces_tuple):
        dice1 = climage.convert(
            f'{self.assets_path}/dice_{faces_tuple[0]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        dice2 = climage.convert(
            f'{self.assets_path}/dice_{faces_tuple[1]}.png',
            is_unicode=True,
            is_truecolor=True,
            is_256color=False,
            width=12
        )
        return print(f'{dice1}\n{dice2}')
    def display_table(self, score_list):
        table=score_list
        headers=["Player","Score"]
        parsed_table = tabulate.tabulate(
            table,
            headers,
            tablefmt="heavy_outline"
        )
        return print(f'{parsed_table}\n')
    def display_winner(self,players_name):
        return print(art.text2art(f"{players_name}  Won!\n",
                                  font="Tarty1"))

    def display_clear(self):
        match (platform.system()):
            case 'Windows' | 'Windows':
                return os.system('cls')
            case _:
                return os.system('clear')
