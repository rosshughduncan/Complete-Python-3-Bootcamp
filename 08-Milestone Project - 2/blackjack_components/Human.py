from .blackjack_functions import printadd, valid_int
from .Player import Player

class Human(Player):
    def __init__(self, chips, name):
        Player.__init__(self, chips, name)

    # print_hand method where we are able to see the player's cards
    def print_hand(self):
        current_suite = ''
        printadd("Hand:      ")
        # iterate cards in hand
        for current_card in self.hand:
            current_suite = current_card.get_suite()
            # print suite symbol
            printadd(f"{current_suite}{current_card.get_order()}{current_suite} ")
        print()

    def place_bet(self):
        # reset bet from previous turn
        bet = []
        # set bet for each of the chip colours
        for i in range(len(CHIP_VALUES)):
            while True:
                bet.append(valid_int(f"Place your bet of {CHIP_VALUES[i][0]} chips: "))
                if bet[i] > self.bankroll[i]:
                    print("You have attempted to draw more chips than you have! Please try again.")
                    bet.pop()
                    continue
                else:
                    self.bankroll[i] -= bet[i]
                    break
        return bet

    def print_bet(self):
        printadd("\nBet:    ")
        print_chips(self.bet)
