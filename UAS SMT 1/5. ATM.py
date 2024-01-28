class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited into your account.")
        self.check_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            self.check_balance()

def main():
    atm = ATM(1000)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
