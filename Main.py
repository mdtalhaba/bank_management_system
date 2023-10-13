from Bank import Bank
from Admin import Admin
from User import User

def main() :
    bank = Bank('Jonogoner Bank', "Dhaka")
    admin = Admin("Admin", "ad@min.com", "1234", "Adabor")
    bank.admin = admin
    

    while True :
        print(f"\n-------- Welcome to {bank.bank_name} ---------\n")
        print("   Chose an Option")
        print("   Option 1 : User")
        print("   Option 2 : Admin")
        print("   Option 3 : Exit\n")
        op1 = int(input("Press the Option : "))
        if op1  == 1 :
            print("\n   Option 1 : Allready have an account")
            print("   Option 2 : Create new account\n")
            op2 = int(input("Press the Option : "))
            if op2 == 1 :
                accNumber = int(input("Please give me your account number : "))
                if accNumber in bank.accounts :
                    print("\n\n-----Welcome to your account------")
                    print("\n    Chose an Option\n")
                    print("    Option 1 : Deposit")
                    print("    Option 2 : Withdraw")
                    print("    Option 3 : Check Balance")
                    print("    Option 4 : Check Transections")
                    print("    Option 5 : Take Loan")
                    print("    Option 6 : Transfer Money\n")
                    op3 = int(input("Please Give me an Option : "))
                    print("\n")
                    if op3 == 1 :
                        dp_amount = int(input("Please give your Deposit amount : "))
                        bank.accounts[accNumber].deposit(dp_amount)
                    elif op3 == 2 :
                        wd_amount = int(input("Please give your Withdraw amount : "))
                        bank.accounts[accNumber].withdraw(wd_amount)
                    elif op3 == 3 :
                        bank.accounts[accNumber].check_balance()
                    elif op3 == 4 :
                        bank.accounts[accNumber].check_transection()
                    elif op3 == 5 :
                        loan_amount = int(input("Please give your loan amount : "))
                        bank.accounts[accNumber].take_loan(loan_amount)
                    elif op3 == 6 :
                        recever = input("Please press receiver account number : ")
                        tf_amount = int(input("Please press transfer amount : "))
                        bank.accounts[accNumber].transfer_money(recever, tf_amount)
                    else :
                        print("\nInvalid Option, Please Give me Valid Option")
                else :
                    print("\nYour Account Number is Invalid, Please Give me Valid Account Number")
            elif op2 == 2 :
                name = input("Please Give me your Name : ")
                email = input("Please Give me your Email : ")
                address = input("Please Give me your Address : ")
                accType = input("Please Give me Account Type (savings/current) : ")
                user = User(name, email, address, accType)
                user.__repr__()
                bank.accounts[user.accNumber] = user
            else :
                print("\nInvalid Option, Please Give me Valid Option")
        elif op1 == 2 :
            print()
            admin_email = input("Please Give me your Email : ")
            admin_pass = input("Please Give me your Password : ")
            if bank.admin.email == admin_email :
                if bank.admin.password == admin_pass :
                    print("\n\n---------Welcome to Admin Panel---------")
                    print("\n    Chose an Option\n")
                    print("    Option 1 : Create Account")
                    print("    Option 2 : Delete Account")
                    print("    Option 3 : See User List")
                    print("    Option 4 : Check Total Balance")
                    print("    Option 5 : Check Total Loan")
                    print("    Option 6 : on/off Loan Feature\n")
                    op4 = int(input("Please Give me an Option : "))
                    if op4 == 1 :
                        print()
                        ac_name = input("Please Give me Account Name : ")
                        ac_email = input("Please Give me Account Email : ")
                        ac_address = input("Please Give me Account Address : ")
                        account_type = input("Please Give me Account Type (savings/current) : ")
                        admin.create_account(ac_name, ac_email, ac_address, account_type)
                    elif op4 == 2 :
                        ac_number = input("Please Give me Account Number : ")
                        admin.delete_account(ac_number)
                    elif op4 == 3 :
                        admin.see_user_list()
                    elif op4 == 4 :
                        admin.check_total_balance()
                    elif op4 == 5 :
                        admin.check_total_loan()
                    elif op4 == 6 :
                        print("    Option 1 : Loan Feature On")
                        print("    Option 2 : Loan Feature Off")
                        on_off = int(input("Please Chose an Option : "))
                        if on_off == 1 :
                            admin.on_off_loan_feature('on')
                        elif on_off == 2 :
                            admin.on_off_loan_feature('off')
                        else :
                            print("\nInvalid Option, Please Give me Valid Option")
                    else :
                        print("\nInvalid Option, Please Give me Valid Option")
                else :
                    print("\nInvalid Password, Please Give me Valid Password")
            else :
                print("\nInvalid Email, Please Give me Valid Email")
        elif op1 == 3 :
            break



if __name__ == '__main__' :
    main()