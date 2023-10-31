import os

# Function to initialize the balance
def initialize_balance():
    balance = 0
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as file:
            try:
                balance = float(file.read())
            except ValueError:
                balance = 0
    return balance

# Function to display the current balance
def display_balance(balance):
    print(f"Current Balance: ${balance:.2f}")

# Function to add a credit (deposit) to the balance
def add_credit(balance):
    try:
        credit = float(input("Enter the amount to deposit: $"))
        balance += credit
        print(f"Successfully deposited ${credit:.2f}")
        return balance
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return balance

# Function to add a debit (withdrawal) from the balance
def add_debit(balance):
    try:
        debit = float(input("Enter the amount to withdraw: $"))
        if balance - debit >= 0:
            balance -= debit
            print(f"Successfully withdrew ${debit:.2f}")
        else:
            print("Insufficient funds.")
        return balance
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return balance

# Function to save the balance to a file
def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))

# Main program loop
def main():
    balance = initialize_balance()
    print("Welcome to the Ursula Checkbook App!")

    while True:
        print("\nChoose an action:")
        print("1. View Current Balance")
        print("2. Add a Credit (Deposit)")
        print("3. Add a Debit (Withdrawal)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_balance(balance)
        elif choice == '2':
            balance = add_credit(balance)
        elif choice == '3':
            balance = add_debit(balance)
        elif choice == '4':
            save_balance(balance)
            print("Thank you for using the Ursula Checkbook App. Your balance has been saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


