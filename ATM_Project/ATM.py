class ATM:
    def __init__(self):
        # Default variables
        self.balance = 40000

        self.cash = {
            100: 50,
            50: 20,
            20: 300,
            10: 0,
            5: 200,
            1: 10
        }

    # Display balance and available cash
    def display_balance(self):
        print("\n===== ATM INFORMATION =====")
        print(f"Account Balance: ${self.balance}")

        for denomination, quantity in self.cash.items():
            print(f"${denomination} bills: {quantity}")

    # Withdrawal method
    def withdraw(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            print("Invalid amount!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        total_cash = sum(
            denomination * quantity
            for denomination, quantity in self.cash.items()
        )

        if amount > total_cash:
            print("Sorry! The ATM has insufficient cash.")
            return

        remaining = amount
        withdrawn = {}

        # Calculate banknotes (largest to smallest)
        for denomination in sorted(self.cash.keys(), reverse=True):
            quantity = self.cash[denomination]
            count = min(remaining // denomination, quantity)

            withdrawn[denomination] = count
            remaining -= count * denomination

        # Check if exact change could be made
        if remaining > 0:
            print("ATM does not have the exact bill denominations to dispense this amount!")
            return

        # Update ATM cash
        for denomination, count in withdrawn.items():
            self.cash[denomination] -= count

        # Update account balance
        self.balance -= amount

        print("\n===== WITHDRAWAL SUCCESS =====")
        print(f"\n\tWithdrawn: ${amount}")

        print("\tYou have received:")
        for denomination, count in withdrawn.items():
            if count > 0:
                print(f"\t\t${denomination} x {count}")

        print(f"\tRemaining Balance: ${self.balance}")

    # Main menu
    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                self.display_balance()

            elif choice == "2":
                try:
                    amount = int(input("Enter amount: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input! Please enter a valid whole number without currency symbols.")

            elif choice == "3":
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid choice!")


# Run the ATM program
if __name__ == "__main__":
    atm = ATM()
    atm.menu()
