# withdraw.py - withdrawal functionality

def withdraw(account, amount: float):
    """
    Withdraw money with safety checks.
    """
    if amount <= 0:
        print("Invalid amount ❌")
        return account.balance

    if amount > account.balance:
        print("Insufficient balance ❌")
        return account.balance

    account.update_balance(-amount)

    print(f"Withdrawn: {amount} EGP ✔")
    print(f"Remaining Balance: {account.balance} EGP")

    return account.balance