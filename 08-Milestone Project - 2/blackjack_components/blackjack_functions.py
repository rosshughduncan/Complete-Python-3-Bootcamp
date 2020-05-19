from colorama import Fore
from colorama import Back

# format for each colour: (score, colorama colour)
CHIP_VALUES = (('white', 1, Fore.WHITE), ('red', 5, Fore.RED),
               ('blue', 10, Fore.CYAN), ('green', 25, Fore.GREEN),
               ('yellow', 50, Fore.YELLOW))

def printadd(print_input):
    print(print_input, end = '')

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
    bank = 0
    for i in range(0, len(CHIP_VALUES)):
        bank += chips[i] * CHIP_VALUES[i][1]
    return bank
