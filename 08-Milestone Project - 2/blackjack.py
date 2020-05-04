from os import system
from colorama import Fore
from colorama import Back
import random

#**********
# Constants
#**********
# format for each colour: (score, colorama colour)
CHIP_VALUES = (('white', 1, Fore.WHITE), ('red', 5, Fore.RED),
               ('blue', 10, Fore.BLUE), ('green', 25, Fore.GREEN),
               ('yellow', 50, Fore.YELLOW))

#***************
# Custom objects
#***************
class Card():
    def __init__(self, suite, order):
        # define card suite
        self.suite = suite
        # define card number/face
        self.order = order
        # if card is a face card, it has a value of 10
        if order in ['jack', 'queen', 'king']:
            self.value = 10
        # if card is an ace, the human player can choose a value of 1 or 11
        # therefore it's marked as -1
        elif order == 'ace':
            self.value = -1
        # any other card has its normal assigned
        else:
            self.value = order

    def get_suite(self):
        return self.suite

    def get_order(self):
        return self.order

    def get_value(self):
        return self.value

class Chip():
    def __init__(self, colour):
        self.colour = colour
        # determine value of chip
        self.value = chip_values[colour]

class Player():
    def __init__(self, chips, name):
        # set up the chips for the player
        self.bankroll = chips
        # start with an empty deck of cards
        self.hand = []
        # set initial bet as nothing
        self.bet = None
        # set player's name
        self.name = name

    # print chips of the player
    def print_bankroll(self, currency):
        bank = 0

        printadd("Chips:  ")
        print_chips(self.bankroll)

        # Calculate player's total money
        for i in range(0, len(CHIP_VALUES)):
            bank += self.bankroll[i] * CHIP_VALUES[i][1]

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

    # hit method
    # def hit():
        # retrieve card from deck

        # check value of hand

class Dealer(Player):
    def __init__(self, chips, name):
        Player.__init__(self, chips, name)

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
        self.bet = []
        # set bet for each of the chip colours
        for chip_type in CHIP_VALUES:
            self.bet.append(valid_int(f"Place your bet of {chip_type[0]} chips: "))
        # move chips from bank to bet
        for i in range(0, self.bet):
            self.bankroll[i] -= self.bet[i]

    def print_bet(self):
        printadd("Bet:      ")
        print_chips(self.bet)

class Board():
    def __init__(self, players):
        # set up players
        self.players = players
        # deck of cards
        self.deck = [] # deck needs to be mutable
        # populate the deck
        for suite in ['\u2660', '\u2663', '\u2665', '\u2666']:
        #for suite in ['spades','clubs','hearts','diamonds']:
            # set for each suite
            self.deck.append(Card(suite, 'ace'))
            for num in range(2,11):
                self.deck.append(Card(suite, num))
            self.deck.append(Card(suite, 'jack'))
            self.deck.append(Card(suite, 'queen'))
            self.deck.append(Card(suite, 'king'))
        # enter player currency
        self.currency = valid_currency("Enter the game currency symbol: ")
        # start with entering chips for dealer and player


    def draw_board(self, showBets):
        # clear screen
        system('cls')

        # print each player's section
        for i in range(0, len(self.players)):
            print(f"========== {self.players[i].get_name()} ==========\n")
            self.players[i].print_bankroll(self.currency)
            print('\n')
            self.players[i].print_hand()
            # print bets if we want them to be shown
            if showBets:
                self.players[i].print_bet()
            print("\n")

    def deal(self):
        decksize = len(self.deck)
        # take cards from deck
        if decksize > 0:
            for i in range(0, len(self.players)):
                self.players[i].add_card(self.deck.pop(random.randint(0, decksize)))
        else:
            # if there are no cards left in the deck
            print("The deck is empty!")

    def place_bets(self):
        # go through players, only ask to place gets if they are a human
        for current_player in self.players:
            if type(current_player) == 'Human':
                print("I am here")
                current_player.place_bet()

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
        starting_chips = []
        for key in CHIP_VALUES:
            starting_chips.append(valid_int(f"Enter the number of {key[0]} chips for each player: "))
        game_board = Board((Dealer(starting_chips, 'Dealer'), Human(starting_chips, 'Human')))
        # deal cards to both players
        game_board.deal()
        # draw screen to begin without showing bets
        game_board.draw_board(False)

        # ask player to place a bet
        game_board.place_bets()
