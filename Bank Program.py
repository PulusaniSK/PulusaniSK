def show_balance(balance):
    """
    Display the current balance.
    """
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    """
    Prompt the user to enter an amount to deposit.
    Return the amount if it's valid, otherwise return 0.
    """
    while True:
        print("*********************")
        try:
            amount = float(input("Enter an amount to deposit: "))
            print("*********************")
            if amount < 0:
                print("*********************")
                print("That's not a valid amount.")
                print("*********************")
            else:
                return amount
        except ValueError:
            print("*********************")
            print("Please enter a valid number.")
            print("*********************")

def withdraw(balance):
    """
    Prompt the user to enter an amount to withdraw.
    Return the amount if it's valid, otherwise return 0.
    """
    while True:
        print("*********************")
        try:
            amount = float(input("Enter an amount to withdraw: "))
            print("*********************")
            if amount > balance:
                print("*********************")
                print("Insufficient funds.")
                print("*********************")
            elif amount < 0:
                print("*********************")
                print("Amount must be greater than 0.")
                print("*********************")
            else:
                return amount
        except ValueError:
            print("*********************")
            print("Please enter a valid number.")
            print("*********************")

def main():
    """
    Main function to run the banking program.
    """
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice.")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()
