from .blackjack_functions import CHIP_VALUES

class Chip():
    def __init__(self, colour):
        self.colour = colour
        # determine value of chip
        self.value = CHIP_VALUES[colour]
