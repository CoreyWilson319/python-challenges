print("Welcome to Chase bank.")
print("Have a nice day!")


def bank(amount):
    balance = amount
    user_input = input(
        "What would you like to do? (deposit, withdraw, check_balance): ")
    if user_input == "deposit".lower():
        deposit_amount = int(input("How much would you like to deposit?: "))
        balance = balance + deposit_amount
        return print("You now have " + str(balance))
    if user_input == "withdraw".lower():
        withdraw_amount = int(input("How much would you like to withdraw?: "))
        if withdraw_amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - withdraw_amount
            return print("You have withdrawn " + str(withdraw_amount) + " You have " + str(balance) + " remaining!")

    if user_input == "balance.lower()":
        return print("You have " + balance + "remaining in your account")


bank(4000)
