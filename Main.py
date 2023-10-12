from Bank import Bank
from Admin import Admin

def main() :
    jonogoner_bank = Bank('Jonogoner Bank', "Dhaka")
    admin = Admin()
    user1 = admin.create_account("Kodom Ali", "kodom@ali.com", "kodom toly", "Savings")
    user2 = admin.create_account("Rustom Ali", "Rustom@ali.com", "kodom toly", "Savings")
    user1.deposit(1000)
    user2.deposit(3000)
    admin.on_off_loan_feature('off')
    user1.take_loan(20000)
    admin.check_total_balance()
    admin.check_total_loan()
    admin.on_off_loan_feature('on')
    user1.take_loan(20000)
    admin.check_total_balance()
    admin.check_total_loan()
    # for val in Bank.accounts.values() :
    #     print(val.balance)

if __name__ == '__main__' :
    main()