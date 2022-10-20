# All capitals mean constant value - something that is not going to change.
MAX_LINES = 3

# collecting user input : We need to get the deposit that the user
# is entering as well as their bet.

# making a function called deposit
def deposit():
    # there is a while loop here because we are going to continually ask
    # the user to enter a deposit amount until they give a valid amount.
    while True:
        amount = input("What would you like to deposit? $")
# now we need to check if this amount is actually a valid number. isdigit
# is going to tell us if this is a valid whole number. Negative numbers
# won't be true. 
        if amount.isdigit():
# By default the number the user enters will come as a string
# so we will convert it into a number(int)
            amount =int(amount)
# if amount is greater than 0 then we will break out of this while loop. 
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
# now we need to check if this amount is actually a valid number. isdigit
# is going to tell us if this is a valid whole number. Negative numbers
# won't be true. 
        if lines.isdigit():
# By default the number the user enters will come as a string
# so we will convert it into a number(int)
            lines =int(lines)
# if amount is greater than 0 then we will break out of this while loop. 
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

#I'm going to put our program in this function main so that if we end our
# program, we can just call this function again and it will rerun program.
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
