print("Welcome to ABC Bank")
restart = 'T'
balance = 1000.00
chances = 3

while chances >= 0:
    pin = int(input("\nEnter PIN for verification:\n"))
    if pin == (1234):
        while restart not in ('n,', 'no','NO', 'N'):
            print("Menu: Please type the number of your choice\n")
            print('1. Type 1 to check your balance')
            print("2. Type 2 to quit\n")
            option = int(input('what would you like to check?'))
            if option == 1:
                print("Your balance is", balance)
                print("thank you for bank with us")
            elif option == 2:
                print("Please wait to get your card.\n")
                print("Thank you for banking with us.")
                quit()
            else:
                print("Please enter correct PIN.")
                restart('y')
    elif pin != ('1234'):
        print("You've entered the wrong pin!")
        chances = chances - 1
        if chances == 0:
            print('3 Attempts Alert, No More Tries')
            break










