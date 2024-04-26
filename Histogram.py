class Histogram():
    def print_histogram(self,player1,player2):
        print("\n{} got the following score within thes game :\n"
              .format(player1.get_name()))
        self.print_asterisk(player1.get_scoreList())

        print("\n{} gReceived the following scores during the game :\n"
              .format(player2.get_name()))
        self.print_asterisk(player2.get_scoreList())

        print("\nNote that if there are 1 or 6 asterisks in a single row,"
              "means to start score from zero.")

    @staticmethod
    def print_asterisk(player_list):
        for score in player_list:
            print(score * " * ")