from User import User
from Bank import Bank

class Admin :
    def __init__(self, name, email, password, address) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address

    def create_account(self, name, email, address, accType) :
        user = User(name, email, address, accType)
        Bank.accounts[user.accNumber] = user

    def delete_account(self, accNumber) :
        if accNumber in Bank.accounts :
            Bank.accounts.pop(accNumber)
        else :
            print("Invali Account Number, Please Give me Valid Account Number")

    def see_user_list(self) :
        print("\n---------------------- All User Account List -------------------\n")
        for acc in Bank.accounts.values() :
            print(f"Name : {acc.name}, Email : {acc.email}, Address : {acc.address}, Acount Number : {acc.accNumber}")

    def check_total_balance(self) :
        total_balance = 0
        for acc in Bank.accounts.values() :
            total_balance += acc.balance
        print(total_balance)

    def check_total_loan(self) :
        total_loan = 0
        for acc in Bank.accounts.values() :
            total_loan += acc.loan_amount
        print(total_loan)

    def on_off_loan_feature(self, flag) :
        if flag == 'on' :
            for acc in Bank.accounts.values() :
                acc.loan_count = 2
        else :
            for acc in Bank.accounts.values() :
                acc.loan_count = -1









# i = 0
# for key, val in Bank.accounts.items() :
#     i = key
#     print(key, val)
# admin.delete_account(i)
# for key, val in Bank.accounts.items() :
#     i = key
#     print(key, val)