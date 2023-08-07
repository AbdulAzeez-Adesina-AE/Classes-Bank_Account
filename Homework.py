class Account_Details():
    def __init__(self, account_name, current_balance):
        self.account_name = account_name
        self.current_balance = current_balance

    def savings(self, deposit_amount):
        self.current_balance += deposit_amount
        print(f"{deposit_amount} has been added to your Account. ")    
    
    def withdrawal(self, withdrawal_amount):
        self.current_balance -= withdrawal_amount
        print(f"{withdrawal_amount} has been debited from your Account. ") 



#Printing out Old bank balance
def Present_day_details():
    print(f"Hello, {Bank_details.account_name} your current balance is {Bank_details.current_balance}. ")

#Printing out the new Bank balance
def New_balance():
    print(f"Your new balance is: {Bank_details.current_balance}")


# Creating an anonymous Bank user      
Bank_details = Account_Details('Ayinde', 60000)

# Performing Operations on this account.

print(f"Welcome, {Bank_details.account_name}")
print("\n")
Present_day_details()
#depositing 5000 into the account
Bank_details.savings(5000)
New_balance()
print("\n")
Bank_details.withdrawal(25000)
New_balance()




