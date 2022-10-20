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

deposit()
