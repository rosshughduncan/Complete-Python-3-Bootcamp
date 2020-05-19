from os import system
import random, sys

sys.path.insert(0, '/blackjack_components/')
from blackjack_components.Board import Board
from blackjack_components.Card import Card
from blackjack_components.Player import Player
from blackjack_components.Dealer import Dealer
from blackjack_components.Human import Human
#from blackjack_components.blackjack_functions import *

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
