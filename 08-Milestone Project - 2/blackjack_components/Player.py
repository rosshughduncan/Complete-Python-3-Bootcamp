from .blackjack_functions import printadd, print_chips, calculate_bankroll
from colorama import Fore
from colorama import Back

class Player():
    def __init__(self, chips, name):
        # set up the chips for the player
        self.bankroll = chips
        # start with an empty deck of cards
        self.hand = []
        # set player's name
        self.name = name

    # print chips of the player
    def print_bankroll(self, currency):
        bank = 0

        printadd("Chips:  ")
        print_chips(self.bankroll)

        # Calculate player's total money
        calculate_bankroll(self.bankroll)

        # print player's money
        printadd(Fore.WHITE + "\n\nBank:      " + Back.WHITE + Fore.BLACK)
        # print money, setting colour back to default black and white
        printadd(f"{str(currency)}" + f"{str(bank)}" + Back.BLACK + Fore.WHITE)

    # print card hand
    def print_hand(self):
        printadd("Hand:      ")
        # iterate cards in hand
        for current_card in self.hand:
            # print hashes for each card
            printadd('??? ')
        print()

    # add card to hand
    def add_card(self, card):
        self.hand.append(card)

    # get name
    def get_name(self):
        return self.name
