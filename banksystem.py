Menu = """
==============MENU==============

[1] - Deposit
[2] - Withdraw
[3] - Statement
[4] - Exit

================================
"""

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3

while True:
    option = input(f"Choose an option: {Menu}")
    
    if option == "1":
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            statement += f"Deposit: ${amount:.2f}\n"
        else:
            print("Invalid deposit amount.")
    
    elif option == "2":
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        
        if withdrawal_amount > balance:
            print("Insufficient balance.")
        elif withdrawal_amount > limit:
            print(f"Withdrawal exceeds the allowed limit of ${limit:.2f}.")
        elif withdrawal_count >= WITHDRAWAL_LIMIT:
            print(f"Daily withdrawal limit exceeded. Limit of {WITHDRAWAL_LIMIT} withdrawals.")
        elif withdrawal_amount > 0:
            balance -= withdrawal_amount
            withdrawal_count += 1
            statement += f"Withdrawal: ${withdrawal_amount:.2f}\n"
            statement += f"Remaining daily withdrawal limit: {WITHDRAWAL_LIMIT - withdrawal_count}\n"
        else:
            print("Invalid withdrawal amount.")
    
    elif option == "3":
        if statement == "":
            print("No transaction records.")
        else:
            print(f"Statement:\n{statement}")
    
    elif option == "4":
        print("Thank you for using our bank!")
        break
    
    else:
        print("Invalid option.")
