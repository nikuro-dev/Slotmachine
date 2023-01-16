MAX_LINES = 3

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



def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance ,lines)
    
    
if __name__ == "__main__":
    main()