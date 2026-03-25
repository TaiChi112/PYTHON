balance = 50000

while balance > 0:
    try:
        withdraw_str = input("withdraw : ")
        withdraw_amount = int(withdraw_str)

        if withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
            continue

        if withdraw_amount <= balance:
            balance -= withdraw_amount
        else:
            print("Insufficient fund.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Balance is 0")
