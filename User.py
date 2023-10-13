import random
from Bank import Bank

class User :
    def __init__(self, name, email, address, accType) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.accType = accType
        self.balance = 0
        self.loan_count = 2
        self.loan_amount = 0
        self.accNumber = random.randint(100000, 999999)
        self.transection = []
        self.is_bankrupt = False

    def __repr__(self) -> str:
        print("Welcome, your account is created successfully")
        print(f"Account Number : {self.accNumber}")

    def deposit(self, amount) :
        if amount > 0 :
            self.balance +=amount
            self.transection.append(('Deposit', amount))
            print(f"\nYour Deposit {amount} is Successful")
        else :
            print(f"\nYour Amount {amount} is Invalid, Please Give me Valid Amount")

    def withdraw(self, amount) :
        if amount > 0 and amount <= self.balance and self.is_bankrupt == False:
            self.balance -=amount
            self.transection.append(('Withdraw', amount))
            print(f"\nYour Withdrawl {amount} is Successful")
        elif self.is_bankrupt == True :
            print("\nThe Bank is Bankrupt")
        else :
            print(f"\nWithdrawal amount exceeded")

    def check_balance(self) :
        print(f"\nYour Available Balance is : {self.balance}")

    def check_transection(self) :
        if len(self.transection) == 0 :
            print("\nNo Transections Available")
        else :
            for tr in self.transection :
                print(tr)

    def take_loan(self, amount) :
        if self.loan_count > 0 :
            self.loan_count -= 1
            self.balance += amount
            self.loan_amount += amount
            self.transection.append(('Loan', amount))
            print(f"\nYour Loan Amount {amount} is Add to Main Balance Successfully")
        elif self.loan_count == -1 :
            print("Loan Feature is Currently Not Available")
        else :
            print("Your Loan Limit is Finish, Please Contact the Customer Service")

    def transfer_money(self, accNumber, amount) :
        if accNumber in Bank.accounts :
            if amount <= self.balance :
                Bank.accounts[accNumber].balance += amount
                self.balance -= amount
                print(f"\nYour Balance {amount} is Successfully Transferd")
            else : 
                print("\nYour Current Balance is Lessthen the amount, Please try anouther amount")
        else :
            print("\nAccount does not exist")



# user = User("Kodom Ali", "kodom@ali.com", "kodom toly", "Savings")
# user.deposit(2000)
# user.withdraw(1000)
# user.take_loan(20000)
# user.check_balance()
# user.check_transection()
