import random
from os import system
from .Card import Card
from .blackjack_functions import is_human

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
            self.deck.append(Card(suite, 'A'))
            for num in range(2,11):
                self.deck.append(Card(suite, num))
            self.deck.append(Card(suite, 'J'))
            self.deck.append(Card(suite, 'Q'))
            self.deck.append(Card(suite, 'K'))
        # enter player currency
        #self.currency = valid_currency("Enter the game currency symbol: ")
        """
        This is for testing
        """
        self.currency = "£"
        # bet for player and dealer
        self.bet = None;

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
                if is_human(self.players[i]):
                    self.players[i].print_bet()
                else:
                    print("\nBet:       Matched")
            print("\n")

    def deal(self):
        decksize = len(self.deck)
        # take cards from deck
        if decksize > 0:
            for i in range(0, len(self.players)):
                print(str(decksize))
                self.players[i].add_card(self.deck.pop(random.randint(0, decksize - 1)))
        else:
            # if there are no cards left in the deck
            print("The deck is empty!")

    def place_bets(self):
        # go through players, only ask to place bets if they are a human
        current_bet = None
        for current_player in self.players:
            if is_human(current_player):
                current_bet = current_player.place_bet()
                """
                Future extension - for more than 2 players, calculate the highest bet of all players
                Make every player match the highest bet or fold
                # current_bank = calculate_bankroll(current_bet)
                # if current_bank > highest_bank:
                #     highest_bank = current_bank
                #     highest_bet = current_bet
                """
        self.bet = current_bet
