from .Player import Player

class Dealer(Player):
    def __init__(self, chips, name):
        Player.__init__(self, chips, name)
