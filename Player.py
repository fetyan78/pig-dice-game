class Player:
    """players class"""

    def __init__(self, name, computer):
        """Initialize a player with a name and computer with true or false"""
        self.name = str(name)
        self.computer = bool(computer)
    
    def get_is_computer(self):
        """check if the player is a computer"""
        return self.computer
    
    def get_name(self):
        """get player name"""
        return self.name
    
    def set_name(self, name):
        """set player name"""
        self.name = str(name)
