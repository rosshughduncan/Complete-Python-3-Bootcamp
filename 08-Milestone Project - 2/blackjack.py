from os import system
from colorama import Fore
from colorama import Back
import random
import Board
#Board.path.append('/components')
import Card
#Card.path.append('/components')
import Player
#Player.path.append('/components')

#**********
# Constants
#**********
# format for each colour: (score, colorama colour)
CHIP_VALUES = (('white', 1, Fore.WHITE), ('red', 5, Fore.RED),
               ('blue', 10, Fore.CYAN), ('green', 25, Fore.GREEN),
               ('yellow', 50, Fore.YELLOW))

#*********************************
# Custom objects using CHIP_VALUES
#*********************************
class Chip():
    def __init__(self, colour):
        self.colour = colour
        # determine value of chip
        self.value = CHIP_VALUES[colour]

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

#*****************
# Custom functions
#*****************
def valid_int(message):
    input_str = valid_input(message)
    while True:
        try:
            to_return = int(input_str)
            break
        except (TypeError, ValueError):
            input_str = valid_input("That is not a whole number. Please try again: ")
            continue

    return to_return

def valid_input(message):
    input_str = input(message)
    while True:
        # check for empty input
        if len(input_str) == 0:
            input_str = input("You have not entered a value. Please try again: ")
            continue
        else:
            break
    return input_str

def printadd(print_input):
    print(print_input, end = '')

def print_hashes(bankroll, len_chip_values):
    for i in range(0, len_chip_values):
        # print a line without moving to a new line
        printadd("   ")
        # printing hashes around the numbers
        printadd(CHIP_VALUES[i][2])
        current_chip = f"{bankroll[i]}"
        for j in range(0, len(bankroll[i])):
            printadd('#')

def valid_currency(message):
    input_str = valid_input(message)
    while True:
        # allowed currency symbols
        if input_str in ['£', '$', '€']:
            return input_str
            break
        else:
            input_str = valid_input("That is not a valid currency symbol. Please try again: ")
            continue

def print_chips(chips):
    chips_str = [str(i) for i in chips]
    len_chip_values = len(CHIP_VALUES)
    print_hashes(chips_str, len_chip_values)
    printadd('\n        ')
    for i in range(0, len_chip_values):
        printadd('   ' + CHIP_VALUES[i][2] + chips_str[i])
    printadd('\n        ')
    print_hashes(chips_str, len_chip_values)

def is_human(player):
    return str(type(player)) == "<class '__main__.Human'>"

def calculate_bankroll(chips):
    for i in range(0, len(CHIP_VALUES)):
        bank += chips[i] * CHIP_VALUES[i][1]

#**************
# Main gameplay
#**************
if __name__ == "__main__":
    # mark if we want to keep playing
    keepPlaying = True
    # keep playing the game until the player says to stop
    while keepPlaying:
        # set up game board
        # ask number of chips for each player
        # starting_chips = []
        # for key in CHIP_VALUES:
        #     starting_chips.append(valid_int(f"Enter the number of {key[0]} chips for each player: "))
        """
        This is just for testing
        """
        starting_chips = [4, 4, 4, 4, 4]
        # playing with two players: a dealer and a human
        game_board = Board((Dealer(starting_chips, 'Dealer'), Human(starting_chips, 'Human')))
        # deal cards to both players
        game_board.deal()
        # draw screen to begin without showing bets
        game_board.draw_board(False)
        # ask player to place a bet
        game_board.place_bets()
        # draw board with bets
        game_board.draw_board(True)
        input()
