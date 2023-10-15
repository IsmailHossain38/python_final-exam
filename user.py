class Bank:
    def __init__(self) -> None:
        self.total_balance = 10000
        self.loan_cnt =0
        self.loan_amount = 0
        self.loan_cnrtl = True
        self.total_accounts = {}
        self.bankrupt = False
        



class User(Bank):
    def __init__(self,name,email,address,acc_type,amount) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.amount = amount
        self.withdraw = 0
        self.balance = 0
        self.balance +=amount 
        self.deposit = 0
        
        super().__init__()


    def money_deposit(self,money):
        if self.bankrupt == False:
            self.balance +=money
            self.deposit += money
            self.total_balance +=money
        else:
            print("the bank is bankrupt !\n")

    def withdraw_money(self,amount):
        if self.bankrupt == False:
            if self.balance >=amount:
                self.balance-=amount
                self.withdraw +=amount
                self.total_balance-=amount
                print("withdraw successfull!\n")
            else:
                print("Withdrawal amount exceeded\n")
        else:
            print("the bank is bankrupt !\n")


    def check_balance(self):
        return self.balance

    def history(self):
        return f'name : {self.name} \n balance : {self.balance} \n deposit : {self.deposit} \n withdraw : {self.withdraw} '

    def get_loan(self,amount):
        if self.loan_cnrtl== True:
            if self.loan_cnt <=2:
                self.total_balance -=amount
                self.balance +=amount
                self.loan_amount+=amount
                self.loan_cnt +=1
                print("get Loan successfull! \n")
            else:
                print("you can't get loan 3 times!\n")
        else:
            print("You can't\n")
    def transfer_money(self,receiver_acc_no,amount):
        for k,v in  self.total_accounts.items():
            if k == receiver_acc_no:
                self.withdraw(amount)
                self.money_deposit(amount)
                print("transfer successfull !")
                break
            else:
                print("Account does not exist\n")
        
                


class Admin(Bank):
    def __init__(self) -> None:
        super().__init__()

    def create_acc(self,name,email,address,acc_type,amount):
        id = len(self.total_accounts.keys())+1
        total = User(name,email,address,acc_type,amount)
        self.total_balance +=amount
        info = (name,email,address,acc_type,amount)
        self.total_accounts[id] = info
        
        
    def delete_acc(self,id):
        if id in self.total_accounts:
            del self.total_accounts[id]
            print("delete successfull\n")
        else:
            print("ID no found!\n")

        
    def all_acc_list(self):
        for key,val in self.total_accounts.items():
            return f' User info{val}'

    def check_total_balance(self):
        return self.total_balance
    
    def check_total_loan(self): 
        return self.loan_amount
    def is_bankrupt(self):
        self.bankrupt = True
    
    def Stop_loan(self):
        self.loan_cnrtl = False



if __name__ == '__main__':
    ad =Admin()


    #default user 
    user = User("ismail","ismail@gmail.com","feni","savings",1000)
    user1 = User("nahid","nahid@gmail.com","feni","current",2000)


    while True:
        
        print("User :--> 1")
        print("Admin :--> 2")
        print("Break :--> 3")
        option = int(input("Enter your option: "))
        
        if option == 1:
            print("--------------------------\n")
            print("Money deposit : D ")
            print("Withdrew: W ")
            print("Check Balance: C ")
            print("Check history: H")
            print("Transfer Money: T")
            print("Get Loan : L")
            print("--------------------------\n")
            choise = input("Enter you choise: ")

            if choise == 'D':
                money  = int(input("Enter you money: "))
                user.money_deposit(money)
                
                print("Deposit successfull")
                print("\n")

            elif choise == 'W':
                amount = int(input("Enter your amount: "))
                user.withdraw_money(amount)
                print("\n")
                

            elif choise == 'C':
                print(user.check_balance())
                print("\n")

            elif choise == 'H':
                print(user.history())
                print("\n")
            
            elif choise == 'T':
                id  = int(input("Enter you acc_id: "))
                amount  = int(input("Enter you amount: "))
                user.transfer_money(id,amount)
                print("\n")
            elif choise == 'L':
                amount = int(input("Enter you amount: "))
                user.get_loan(amount)
                


                
        elif option == 2:


            print("----------------------------\n")
            print("create acc: 1")
            print("delete acc: 2")
            print("check_total_balance: 3")
            print("check_total_loan: 4")
            print("control_loan: 5")
            print("all_account_list: 6")
            print("Bankrupt : 7")
            print("----------------------------\n")


            option = int(input("Enter your option: "))
            if option == 1:
                name = input("Enter your Name: ")
                email = input("Enter your Email: ")
                address = input("Enter your Address: ")
                acc_type =input("Enter your account Type: ")
                amount = int(input("Enter your ammount: "))
                ad.create_acc(name,email,address,acc_type,amount)
                print("create successfull\n")

            elif option == 2:
                id = int(input("Enter your accNO: "))
                ad.delete_acc(id)
                print("\n")

            elif option == 3:
                print(ad.check_total_balance())
                print("\n")
            elif option == 4:
                print(ad.check_total_loan())
                print("\n")

            elif option == 5:
                ad.Stop_loan()
                print("Now you can't get Loan")
                print("\n")

            elif option == 6:
                print(ad.all_acc_list())
                print("\n")
            elif option == 7:
                ad.bankrupt()
                

        elif option==3:
            break