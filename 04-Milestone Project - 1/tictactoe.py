import os

def drawScreen(numpad):
    # clear the screen
    os.system('cls')
    print(f' {numpad[6]} ¦ {numpad[7]} ¦ {numpad[8]}')
    print(f' {numpad[3]} ¦ {numpad[4]} ¦ {numpad[5]}')
    print(f' {numpad[0]} ¦ {numpad[1]} ¦ {numpad[2]}')
    # line separarting cells from instructions
    print('')

def clearNumpad(numpad):
    # set every cell in numpad to blank
    numpad = [' ' for i in range(0, 9)]
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
        print('Please enter X or O')
        inputStr = validInputEmpty(input()).upper()
    # set the boolean flag
    if inputStr == 'X':
        return [inputStr, 'O']
    else:
        return ['O', inputStr]

# *************
# Main function
# *************
def playGame():
    # ******************
    # Initial variables
    # ******************
    # numpad holder
    numpad = []
    player1 = {'name': '', 'line': 0}
    player2 = {'name': '', 'line': 0}
    keepPlaying = True

    # ****************************
    # Function calls and gameplay
    # ****************************
    numpad = clearNumpad(numpad)
    drawScreen(numpad)

    # Player 1 enters name and piece choice
    print('Welcome to Tic Tac Toe.\nPlayer 1, please enter your name:')
    player1['name'] = validInputEmpty(input())
    print('Would you like X or O? (enter X or O)')

    # store each player's pieces in an array
    pieces = checkXOrO(input())

    # Player 2 enters name only
    print('\nThanks. Player 2, please enter your name:')
    player2['name'] = validInputEmpty(input())
    print(f'Thanks. You are {pieces[1]}.')



playGame()
