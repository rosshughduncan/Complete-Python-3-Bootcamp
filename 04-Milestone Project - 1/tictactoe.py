import os

def drawScreen(numpad):
    # clear the screen
    os.system('cls')
    print('left: -1 ¦ right: +1 ¦ up: +3 ¦ down: -3 ¦ left-up: +2 ¦ left-down: -4 ¦ right-up: +4 ¦ right-down: -2\n')
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

def checkXOrO(inputStr):
    inputStr = validInputEmpty(inputStr).upper()
    # get the correct input
    while inputStr != 'X' and inputStr != 'O':
        print('Input choice. Please enter X or O')
        inputStr = validInputEmpty(input()).upper()
    # set the boolean flag
    if inputStr == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def input1To9():
    valid = False
    inputNum = None
    inputStr = ''
    # check that the value is a number from 1 to 9
    while valid == False:
        inputStr = validInputEmpty(input())
        try:
            inputNum = int(inputStr)
            while inputNum not in range(0,9):
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

def haveAGo(numpad, piece, cellRules):
    tally = 0

    # validate the input
    inputNum = input1To9()
    # insert the piece at the specified cell
    index = inputNum - 1

    # do not insert a piece if it's occupied by the other player
    while numpad[index] == 'X' or numpad[index] == 'O':
        print('Cell occupied. Choose another number.')
        inputNum = input1To9()
        index = inputNum - 1
        #print(f'INPUT IS {inputNum}')
    # if it is legal to do so, insert the piece onto the board
    numpad.pop(index)
    numpad.insert(index, piece)
    tally = 1
    #tally += 1
    #print(tally)
    drawScreen(numpad)

    # check if there is a cell adjacent to this one that can be filled
    # if another one of the player's pieces has been found, add this to the tally
    # only add cells to the tally if we haven't explored it yet
    for moveCode in cellRules[index]:
        # looking for the first piece
        # we move to the adjacent cell
        print(f'move code now: {moveCode}')
        index += moveCode
        print(f'index now: {index}')
        print(f'cell contents: {numpad[index]}\n')
        if numpad[index] == piece:
            tally += 1
            print(f'tally now: {tally}\n')
            # move to the next adjacent cell to find a third piece
            if moveCode in cellRules[index]:
                index += moveCode
                print(f'index now: {index}\n')
                if numpad[index] == piece:
                    tally += 1
                    print(f'tally now: {tally}\n')
                else:
                    tally -= 1
            else:
                tally -= 1
        # reset the position for next iteration of loop
        index = inputNum - 1

    print(f'FINAL TALLY: {tally}')
    return tally

def validPlayAgain():
    inputChar = validInputEmpty(input())
    while inputChar != 'y' and inputChar != 'n':
        print('Invalid code. Please enter y or n.')
        inputChar = validInputEmpty(input())
    return inputChar == 'y'

# *************
# Main function
# *************
def playGame():
    # ******************
    # Initial variables
    # ******************
    # numpad holder
    numpad = []
    players = ({'name': '', 'line': 0}, {'name': '', 'line': 0})
    keepPlaying = True
    winner = -1
    currentPlayer = 0
    numSet = None
    # Direction rules for each cell
    # left: -1 ¦ right: +1 ¦ up: +3 ¦ down: -3 ¦ left-up: +2 ¦ left-down: -4 ¦ right-up: +4 ¦ right-down: -2
    rules = {0: (3, 4, 1), 1: (-1, 2, 3, 4, 1), 2: (-1, 2, 3), 3: (3, 4, 1, -2, -3), 4: (-1, 2, 3, 4, 1, -2, -3, -4), 5: (-1, 2, 3, -3, -4), 6: (1, -2, -3), 7: (-1, 1, -2, -3, -4), 8: (-1, -3, -4)}

    # ****************************
    # Function calls and gameplay
    # ****************************
    numpad = clearNumpad(numpad)
    drawScreen(numpad)

    # Player 1 enters name and piece choice
    print('Welcome to Tic Tac Toe.\nPlayer 1, please enter your name:')
    players[0]['name'] = validInputEmpty(input())
    print('Would you like X or O? (enter X or O)')

    # store each player's pieces in an array
    pieces = checkXOrO(input())

    # Player 2 enters name only
    print('\nThanks. Player 2, please enter your name:')
    players[1]['name'] = validInputEmpty(input())
    print(f'Thanks. You are {pieces[1]}.')

    # play the game while keep playing is true
    while keepPlaying:
        winner = -1
        # play while we have no winner
        while winner == -1:
            print(pieces)
            print(f"Ross line before: {players[0]['line']}")
            print(f"\n{players[currentPlayer]['name']}, please enter a square number:")
            # determine the line created by the player
            players[currentPlayer]['line'] += haveAGo(numpad, pieces[currentPlayer], rules)
            # check if the board has been filled (hence a draw)
            numSet = set(numpad)
            print(f"Ross line after: {players[0]['line']}")
            if numSet == ['X', 'O'] or numSet == ['O', 'X']:
                print('The game has been drawn.')
                break
            # if either player has drawn a line of 3, select a winner
            elif players[currentPlayer]['line'] >= 3:
                winner = currentPlayer
            # change player
            if currentPlayer == 0:
                currentPlayer = 1
            else:
                currentPlayer = 0

        # announce the winner
        print(f"Contragulations, {players[winner]['name']}, you won!")

        # ask if they want to play again
        print('Would you like to play again? (enter y or n)')
        keepPlaying = validPlayAgain()

    print('Thanks for playing.')

playGame()
