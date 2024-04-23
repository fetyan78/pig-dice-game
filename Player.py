class Player:
    """players class"""

    def __init__(self, name, computer):
        """"Initialize a player with a name and computer with true or false""""
        self.name = str(name)
        self.computer = bool(computer)