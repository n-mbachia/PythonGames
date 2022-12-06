#!/usr/bin/python3
import random

print("this is a slot machine game, you can bet any value and choose your winning slot. Enjoy!!! ")

print("-**---***----*****----***---**-")

MAX_LINES = 3 # LINES ON THE SLOT MACHINE
MAX_BET = 100 # AMOUNT THAT CAN BE BET ON
MIN_BET = 1 # LEAST AMOUNT

# SLOTS ON MACHINE
ROWS = 3
COLS = 3

# THE DISPLAYON SLOTS MACHINE
symbol_count = {
    "A": 5,
    "B": 7,
    "C": 3,
    "D": 9
}

# THE VALUE OF EACH COUNT AS PER WINNING
symbol_value = {
    "A": 4,
    "B": 2,
    "C": 3,
    "D": 1
}

# THIS CHECKS IF PLAYER HAS WON AND ON WHICH LINE
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break #LEAVE BLOCK IF NO MATCH
        else: #BLOCK EXECUTED FOR WIN 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) # TO DIPSLAY WHICH SLOT WON

    return winnings, winning_lines


# THE FUNCTION TO SPIN SLOT MACHINE AND GET RANDOM VALUES
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # RETURNS KEYS AND VALUES IN DICT
        for _ in range(symbol_count):  # _ IS ANONYMOUS VARIABLE IN PYTHON
            all_symbols.append(symbol)

# MAKE A LOOP THAT SELECTS WHAT VALUE GOES IN WHICH COLUMN
    columns = []  # COLUMNS LIST DEFINED
    for _ in range(cols):  # GENERATE COLUMN FOR EVERY COLS
        # THIS CODE IS PICKING RANDOM VALUES FOR EACH COLUMN IN COLUMNS
        column = []
        current_symbol = all_symbols[:]  # MAKES COPY OF SYMBOLS LIST
        # LOOP THROUGH NUMBER OF VALUES TO BE GENERATED FROM LIST
        for _ in range(rows):
            value = random.choice(current_symbol)  # MAKES USE OF IMPORT
            current_symbol.remove(value)  # WE WANT TO REMOVE VALUES THAT HAVE BEEN SELECTED
            column.append(value)  # ADDS VALUE TO COLUMNS

        columns.append(column)  # ADDS VALUE TO OUR COLUMNS LIST

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            # THIS CODE WILL TRANSPOSE THE ROWS TO 3 COLUMNS
            if i != len(columns) - 1:
                print(column[row], end=" | ") # SEPERATOR ON MIDDLE ROW
            else:
                print(column[row], end="")

        print()  # NEW LINE AFTER EACH ROW


# FUNCTION TO ALLOW PLAYER TO DEPOSIT THEIR MONIES
def deposit():
    while True:
        amount = input("What amount would you like to depost? ")
        if amount.isdigit(): # CONFIRMS DIGIT 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            ("Please enter a number. ")
    return amount


# FUNCTION TO GET NUMBER OF LINES PLAYER WANTS TO PLACE BET ON
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= + lines <= + MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


# FUNCTION TO GET PLAYER TO PLACE THEIR BET
def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? ")
        if amount.isdigit():  # ENSURES IS NUMERAL
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # CHECKS TO ENSURE AMOUNT IS AS REQUIRED BY LIMITS
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET} . ")
        else:
            ("Please enter a number. ")
    return amount


# FUNCTION TO SPIN SLOT MACHINE WHEN ALL CONDITIONS ARE MET
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough amount to bet that amount, your current balance is {balance}")
        else:
            break
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You just won {winnings}")
    print(f"You won on lines", *winning_lines)  # * is known as unpack operator
    return winnings - total_bet

# BY CALLING TIS FUNCTION, THE CODE CAN IS RUN AND REPEATED


def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        attemps = input("Press enter to play (q to quit.)")
        if attemps == "q":
            break
        balance += spin(balance)

    print(f"You are left with {balance}")


main()

print("-**---***----*****----***---**-")
