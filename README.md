# Bank Account Management System

This Python code provides a basic level implementation of how a Bank Account Management System works. The `Account_Details` class allows users to create a bank account with an initial balance and perform transactions such as deposits and withdrawals.

## Features

1. Create a Bank Account: Users can create a bank account with their desired account name and initial balance.

2. Deposit Funds: Users can deposit money into their bank account, which will be added to the current balance.

3. Withdraw Funds: Users can withdraw money from their bank account, which will be deducted from the current balance.

4. Check Account Balance: Users can check their current account balance at any time.

## Code Explanation

The Python code consists of a class `Account_Details` and some supporting functions for displaying account details. Here's a breakdown of the code:

```python
class Account_Details():
    def __init__(self, account_name, current_balance):
        self.account_name = account_name
        self.current_balance = current_balance

    def savings(self, deposit_amount):
        self.current_balance += deposit_amount
        print(f"{deposit_amount} has been added to your Account.")

    def withdrawal(self, withdrawal_amount):
        self.current_balance -= withdrawal_amount
        print(f"{withdrawal_amount} has been debited from your Account.")

def Present_day_details():
    print(f"Hello, {Bank_details.account_name}, your current balance is {Bank_details.current_balance}.")

def New_balance():
    print(f"Your new balance is: {Bank_details.current_balance}")

Bank_details = Account_Details('Ayinde', 60000)

print(f"Welcome, {Bank_details.account_name}")
print("\n")
Present_day_details()

Bank_details.savings(5000)
New_balance()

print("\n")
Bank_details.withdrawal(25000)
New_balance()


# Instructions

1. Create an Account: To create a bank account, use the `Account_Details` class and provide a unique account name and an initial balance.

2. Deposit Funds: Use the `savings` method to deposit money into the account. Pass the amount you want to deposit as an argument to the method.

3. Withdraw Funds: Use the `withdrawal` method to withdraw money from the account. Pass the amount you want to withdraw as an argument to the method.

4. Check Account Balance: You can check your current account balance using the `Present_day_details` function to see the initial balance and `New_balance` function to see the balance after transactions.

## Note

This implementation is for demonstration purposes and lacks certain security measures present in real-world banking systems. It is essential to consider additional security measures, validation checks, and error handling when developing a complete and secure banking application.

