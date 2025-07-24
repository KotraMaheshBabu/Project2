class Account:
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("{} deposited successfully.".format(amount))
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print("{} withdrawn successfully.".format(amount))
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print("Account Holder: {}.".format(self.name))
        print("Account Number: {}".format(self.acc_number))
        print("Balance: {}".format(self.balance))


# Derived class with polymorphism
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Savings Account: Cannot withdraw more than balance.")
        else:
            super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount):
        # Overriding for a different behavior
        if amount > (self.balance + 500):  # overdraft limit
            print("Current Account: Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print("{} withdrawn with overdraft.".format(amount))


# Function to run the bank system
def run_bank():
    accounts = {}
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                name = input("Enter account holder name: ")
                acc_number = input("Enter account number: ")
                acc_type = input("Enter account type (savings/current): ").lower()
                if acc_type == 'savings':
                    accounts[acc_number] = SavingsAccount(name, acc_number)
                elif acc_type == 'current':
                    accounts[acc_number] = CurrentAccount(name, acc_number)
                else:
                    print("Invalid account type.")

            elif choice == '2':
                acc_number = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_number].deposit(amount)

            elif choice == '3':
                acc_number = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_number].withdraw(amount)

            elif choice == '4':
                acc_number = input("Enter account number: ")
                accounts[acc_number].display_balance()

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except KeyError:
            print("Account not found.")
        except ValueError:
            print("Please enter a valid number.")
        except:
            print("An error occurred.")


# Run the program
run_bank()
