import os

def drawScreen(numpad):
    # clear the screen
    os.system('cls')
    print(f' {numpad[6]} ¦ {numpad[7]} ¦ {numpad[8]}')
    print('-----------')
    print(f' {numpad[3]} ¦ {numpad[4]} ¦ {numpad[5]}')
    print('-----------')
    print(f' {numpad[0]} ¦ {numpad[1]} ¦ {numpad[2]}')
    # line separarting cells from instructions
    print('')

def clearNumpad(numpad):
    # set every cell in numpad to numbers
    numpad = [i+1 for i in range(0, 9)]
    #numpad = [i+1 for i in range(0, 9)]
    # reset the cells left list
    return numpad

def validInputEmpty(inputStr):
    while inputStr == '':
        inputStr = input()
        # if input is still empty, warn user
        if inputStr == '':
            print('You have not entered anything. Please try again.')
    return inputStr

def checkXOrO(inputStr, players):
    inputStr = validInputEmpty(inputStr).upper()
    # get the correct input
    while inputStr != 'X' and inputStr != 'O':
        print('Invalid choice. Please enter X or O')
        inputStr = validInputEmpty(input()).upper()
    # set the boolean flag
    if inputStr == 'X':
        players[0]['piece'] = 'X'
        players[1]['piece'] = 'O'

    else:
        players[1]['piece'] = 'X'
        players[0]['piece'] = 'O'
    return players

def input1To9():
    valid = False
    inputNum = None
    inputStr = ''
    # check that the value is a number from 1 to 9
    while valid == False:
        inputStr = validInputEmpty(input())
        try:
            inputNum = int(inputStr)
            while inputNum not in range(0,10):
                print('Invalid number. Please enter a number between 1 and 9.')
                inputStr = validInputEmpty(input())
                inputNum = int(inputStr)
            else:
                valid = True
        # if int conversion does not work, the user has entered something other than a number
        except ValueError:
            print(ValueError)
            print('You have not entered a number. Please enter a number between 1 and 9.')
            inputStr = validInputEmpty(input())
    return inputNum

def findLine(numpad, cellRules, storedPieces):
    # store current position in numpad
    index = None
    # store flag for winner
    foundWinner = False

    # find any adjacent cells using the player's stored pieces
    for currentPiece in storedPieces:
        for currentRule in cellRules[currentPiece]:
            # move forward one position if it is possible to do so
            index = currentPiece + currentRule
            # find if this cell is taken up by the current player
            if index in storedPieces:
                # move to the next cell along if it's legal to do so
                if currentRule in cellRules[index]:
                    index += currentRule
                    # if we find another one of the player's cells here, then the player has won
                    if index in storedPieces:
                        foundWinner = True

    return foundWinner

def haveAGo2(numpad, piece, cellRules, storedPieces):
    # validate the input
    inputNum = input1To9()
    # convert cell number to 0 index
    index = inputNum - 1
    # tally for line length found
    tally = 0
    # containing cells we've already explored
    explored = []
    # storing the current rules allowed for each cell
    currentRules = []

    # do not insert a piece if it's occupied by the other player
    while numpad[index] == 'X' or numpad[index] == 'O':
        print('Cell occupied. Choose another number.')
        inputNum = input1To9()
        index = inputNum - 1

    # if it is legal to do so, insert the piece onto the board
    numpad.pop(index)
    numpad.insert(index, piece)
    storedPieces.append(index)

    return findLine(numpad, cellRules, storedPieces)

def validPlayAgain():
    inputChar = validInputEmpty(input())
    while inputChar != 'y' and inputChar != 'n':
        print('Invalid code. Please enter y or n.')
        inputChar = validInputEmpty(input())
    return inputChar == 'y'

def blankNumpad(numpad):
    numpad = clearNumpad(numpad)
    drawScreen(numpad)
    return numpad

def setNames(players):
    # set players' line to 0
    players[0]['line'] = 0
    players[1]['line'] = 0

    # Player 1 enters name and piece choice
    print('Player 1, please enter your name:')
    players[0]['name'] = validInputEmpty(input())
    print('Would you like X or O? (enter X or O)')

    # store each player's pieces
    players = checkXOrO(input(), players)

    # Player 2 enters name only
    print('\nThanks. Player 2, please enter your name:')
    players[1]['name'] = validInputEmpty(input())
    print(f"Thanks. You are {players[1]['piece']}.")

    return players

# *************
# Main function
# *************
def playGame():
    # ******************
    # Initial variables
    # ******************
    # numpad holder
    numpad = []
    players = ({'name': '', 'piece': '', 'storedPieces': []}, {'name': '', 'piece': '', 'storedPieces': []})
    keepPlaying = True
    winner = -1
    currentPlayer = 0
    numSet = None
    # Direction rules for each cell
    # left: -1 ¦ right: +1 ¦ up: +3 ¦ down: -3 ¦ left-up: +2 ¦ left-down: -4 ¦ right-up: +4 ¦ right-down: -2
    rules = {0: (3, 4, 1), 1: (-1, 2, 3, 4, 1), 2: (-1, 2, 3), 3: (3, 4, 1, -2, -3), 4: (-1, 2, 3, 4, 1, -2, -3, -4), 5: (3, -3, -4, -1, 2, 3, -3), 6: (1, -2, -3), 7: (-1, -2, 1, -4, -3), 8: (-1, -3, -4)}
    # storing a flag if we've found a winner
    foundWinner = False

    numpad = blankNumpad(numpad)

    # ****************************
    # Function calls and gameplay
    # ****************************
    print('Welcome to Tic Tac Toe.')

    # set initial players' names
    players = setNames(players)

    # play the game while keep playing is true
    while keepPlaying:
        winner = -1
        # play while we have no winner
        while winner == -1:
            # reset line to 0
            line = 0
            # intialise board and player values
            print(f"\n{players[currentPlayer]['name']}, please enter a cell number:")
            # determine the line created by the player
            foundWinner = haveAGo2(numpad, players[currentPlayer]['piece'], rules, players[currentPlayer]['storedPieces'])
            # check if the board has been filled (hence a draw)
            numSet = set(numpad)
            if numSet == ['X', 'O'] or numSet == ['O', 'X']:
                print('The game has been drawn.')
                break
            # if either player has drawn a line of 3, select a winner
            elif foundWinner:
                winner = currentPlayer
            # change player
            if currentPlayer == 0:
                currentPlayer = 1
            else:
                currentPlayer = 0

            drawScreen(numpad)

        # announce the winner
        print(f"Contragulations, {players[winner]['name']}, you won!")

        # ask if they want to play again
        print('Would you like to play again? (enter y or n)')
        keepPlaying = validPlayAgain()

        # refresh the screen if we want to play again
        if keepPlaying:
            numpad = blankNumpad(numpad)
            players = setNames(players)
            # set current player back to player 1
            currentPlayer = 0
            # set each player's stored cells to blank
            players[0]['storedPieces'] = []
            players[1]['storedPieces'] = []

    print('Thanks for playing.')

playGame()

# #def haveAGo(numpad, piece, cellRules, line, storedPieces):
# def haveAGo(numpad, piece, cellRules, storedPieces):
#
#     # validate the input
#     inputNum = input1To9()
#     # insert the piece at the specified cell
#     index = inputNum - 1
#     # tally for line length found
#     tally = 0
#     # containing cells we've already explored
#     explored = []
#     # storing the current rules allowed for each cell
#     currentRules = []
#
#     # do not insert a piece if it's occupied by the other player
#     while numpad[index] == 'X' or numpad[index] == 'O':
#         print('Cell occupied. Choose another number.')
#         inputNum = input1To9()
#         index = inputNum - 1
#         #print(f'INPUT IS {inputNum}')
#     # if it is legal to do so, insert the piece onto the board
#     numpad.pop(index)
#     numpad.insert(index, piece)
#     storedPieces.append(index)
#     explored.append(index)
#     #print(f"stored pieces: {storedPieces}")
#     print(f"index: {index}")
#     #input()
#
#     #tally += 1
#     #print(tally)
#     drawScreen(numpad)
#
#     # check if there is a cell adjacent to this one that can be filled
#     # if another one of the player's pieces has been found, add this to the tall
#     for moveCode in cellRules[index]:
#         currentRules = list(cellRules[index])
#         print(f"current move code: {moveCode}")
#         # looking for the first piece
#         # we move to the adjacent cell
#         index += moveCode
#         print(f"cell: {index} rules before: {currentRules}")
#         if numpad[index] == piece:
#         #if index in storedPieces and numpad[index] == piece:
#             # only add cells to the tally if the player has placed their piece there
#             if index not in explored:
#                 tally = 1
#                 explored.append(index)
#             print(f"\nExplored cells: {explored}\n")
#             # if we have found a piece, we can only move back in the opposite direction
#             # remove rules which we cannot use
#             # if we go up, we can only go down
#             # if we go right up, we can only go left-down
#             # if we go right, we can only go left
#             # if we go right down, we can only go left up
#             # if we go down, we can only go up
#             # if we go left down, we can only go right up
#             # if we go left, we can only go right
#             # if we go left up, we can only go right down
#             # left: -1 ¦ right: +1 ¦ up: +3 ¦ down: -3 ¦ left-up: +2 ¦ left-down: -4 ¦ right-up: +4 ¦ right-down: -2
#             allowedRule = moveCode * - 1
#             for i in currentRules:
#                 if i != allowedRule or i != moveCode:
#                     currentRules.remove(i)
#             print(f"\nallowed rule: {currentRules}\n")
#             #rules = [moveCode, moveCode * -1]
#
#             # go to the next iteration if we can't go any further
#             if moveCode not in currentRules:
#                 continue
#
#             print(f"\nRules after: {currentRules}\n")
#
#             print(f"index: {index}")
#             print(f"tally: {tally}")
#             # if we are able to move to the next adjacent cell to check it, do so
#             if moveCode in currentRules:
#                 index += moveCode
#                 print(f"cell: {index} cell rules: {currentRules}")
#
#                 if numpad[index] == piece:
#                 #if index in storedPieces and numpad[index] == piece:
#                     #if index not in explored:
#                     if index not in explored:
#                         tally = 2
#                         print(f"index: {index}")
#                         print(f"tally: {tally}")
#                         # prevent iteration through other cells if the player has won
#                         break
#                     #explored.append(index)
#
#
#         # reset the position for next iteration of loop
#         index = inputNum - 1
#     return tally
