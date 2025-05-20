class ATM:
    def __init__(self, balance=5000, pin=1234):
        self.balance = balance
        self.pin = pin
        self.is_authenticated = False
        self.attempts = 3
    
    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.is_authenticated = True
            return True
        else:
            self.attempts -= 1
            if self.attempts == 0:
                print("Card blocked.")
                return False
            print(f"Invalid PIN. {self.attempts} attempts remaining.")
            return False
    
    def check_balance(self):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return

        print(f"Current balance: Rs.{self.balance}")

    def deposit(self, amount):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return

        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrawn Rs.{amount}. New balance: Rs.{self.balance}")

    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    entered_pin = int(input("Enter your PIN: "))
    if atm.authenticate(entered_pin):
        atm.run()