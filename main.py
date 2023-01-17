import random

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
ROWS = 3
COLS = 3
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnigs(columns, lines, bet, values):
    winnigs = 0
    winnig_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnigs += values[symbol] * bet
            winnig_lines.append(lines + 1)
    return winnigs, winnig_lines
    
    
def spin_slot_machine(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else :
                print(column[row],end=" ")
        print()

def deposit():
    while True:
        amount = input("what would you like to depozit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("amount must be greateer than zero")
        else:
            print("please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"enter number of lines that you want to bet on ?(1-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if  0 < lines <= MAX_LINES:
                break
            else:
                print("you have to bet at least one line")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount of bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number")
    return amount
def game(balance ):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance :
            print(f"you cant bet more than your balance you balance is ${balance}")
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. total bet amount is ${total_bet}")

    slots = spin_slot_machine(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnigs, winnig_lines = check_winnigs(slots, lines, bet, symbol_value)
    print(f"you won ${winnigs}")
    print(f"you won on lines:", *winnig_lines)
    return winnigs - total_bet

def main():
    balance = deposit()
    while True:
        print(f"currnet balance is ${balance}")
        spin = input("press enter to spin (press q to quit)")
        if spin == "q":
            print("game ended")
            break
        balance += game(balance)
    print(f"you left with ${balance}")       
if __name__ == "__main__":
    main()