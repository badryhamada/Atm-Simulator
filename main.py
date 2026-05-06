from auth import login_system
from account import Account
from deposit import deposit
from withdraw import withdraw
from transactions import TransactionManager
from utils import print_line

# Setup system
account = Account("Ali", 1000)
transactions = TransactionManager()
PIN = "1234"


def main():
    print("=== ATM SYSTEM ===")

    # Login
    if not login_system(PIN):
        return

    while True:
        print_line()
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Account Info")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print(f"Balance: {account.get_balance()} EGP")

        elif choice == "2":
            amount = float(input("Enter amount: "))
            deposit(account, amount)
            transactions.add_transaction("Deposit", amount)

        elif choice == "3":
            amount = float(input("Enter amount: "))
            before = account.get_balance()
            withdraw(account, amount)

            if account.get_balance() != before:
                transactions.add_transaction("Withdraw", amount)

        elif choice == "4":
            transactions.show_history()

        elif choice == "5":
            account.show_account_info()

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option ❌")


if __name__ == "__main__":
    main()