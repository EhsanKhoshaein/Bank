#============================================@ BANK PROGRAM @==========================================#
bank_list = []
import bank_file
bank_list = bank_file.load()
class Account:
    def __init__(self, number, name, money):
        self.number = number
        self.name = name
        self.money = money
    def history(self):
        import account_file
        account_number = self.number
        account_list = account_file.load(account_number)
        print(f'\nACCOUNT NUMBER: {self.number}')
        print(f'NAME: {self.name}\n')
        print('+---------------------------------------------------------------------------+')
        print("|{0: ^18}|{1: ^18}|{2: ^18}|{3: ^18}|".format('Transaction','Date','Time','Total'))
        print('+---------------------------------------------------------------------------+')
        for item in account_list:
            for part in item:
                print("|",end='')
                print("{0: ^18s}".format(part),end='')
            print("|",end='\n')
            print('+---------------------------------------------------------------------------+')
    def deposit(self):
        account_list = []
        given_money = str('+' + input("\nHow much money do you want to deposit to account? "))
        account_list.append(given_money)
        for account in bank_list:
            if account[0] == self.number:
                self.money = account[2]
                break
        d = str(int(self.money) + int(given_money))
        import datetime
        now = datetime.datetime.now()
        date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
        time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        account_list.append(date)
        account_list.append(time)
        account_list.append(d)
        import account_file
        account_number = self.number
        account_file.save(account_number, account_list)
        for account in bank_list:
            if account[0] == self.number:
                account[2] = d
                break
        import bank_file
        bank_file.rewrite(bank_list)
        print("\n Depositing is done successfully ..!")
    def withdraw(self):
        for account in bank_list:
            if account[0] == self.number:
                self.money = account[2]
                break
        taken_money = input("\nHow much money do you want to withdraw from account? ")
        if int(taken_money) > int(self.money):
            print("\n   oops :( .. Insufficient inventory .. Go back to previous process    ")
        else:
            t =str('-' + taken_money)
            account_list = []
            w = str(int(self.money) - int(taken_money))
            account_list.append(t)
            import datetime
            now = datetime.datetime.now()
            date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
            time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
            account_list.append(date)
            account_list.append(time)
            account_list.append(w)
            account_number = self.number
            import account_file
            account_file.save(account_number, account_list)
            for account in bank_list:
                if account[0] == self.number:
                    account[2] = w
                    break
            import bank_file
            bank_file.rewrite(bank_list)
            print("\n Withdrawing is done successfully ..!")
class create(Account):
    def __init__(self):
        if bank_list == []:
            number = '100'
        else:
            number = str(int(bank_list[-1][0])+1)
        Account.__init__(self, number, name = input('\nEnter your name: '), money = input('\nEnter amount of money: '))
        sure = input("\n   Are you sure (y/n): ")
        if sure == 'y':
            account_list = []
            account_list.append(self.number)
            account_list.append(self.name)
            account_list.append(self.money)
            bank_list.append(account_list)
            import bank_file
            bank_file.save(account_list)
            ################################
            account_list = []
            s = '+' + self.money
            account_list.append(s)
            import datetime
            now = datetime.datetime.now()
            date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
            time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
            account_list.append(date)
            account_list.append(time)
            account_list.append(self.money)
            account_number = number
            account_file = open(f'{account_number}.txt','w')
            account_file.close()
            import account_file
            account_file.save(account_number,account_list)
            print("\nNew account created successfully .. :D !")
            
        else:
            pass
#--------------------------------------------------------------------------------------------#

menu_option = ['1','2','3','4','5']
#============================================================================================#
while(True):
    print('=====================================================================')
    print('''
 (1) create a new account
 (2) search an account 
 (3) show all accounts
 (4) show all transactions of a person
 (5) exit''')
    
    menu_choice = input("\nEnter your choice: ")
    if menu_choice not in menu_option:
        print("   UNKNOWN CHOICE   ")
#============================================================================================#
    elif menu_choice == '1': 
        a = create()
#============================================================================================#    
    elif menu_choice == '2':
        while(True):
            if bank_list == []:
                print("\nThere is no Account in Bank ..! ")
                break
            else:
                search = input('''\nPlease enter an account Number ...
\nif you don't know that, so enter account-owner's Name ...
Note: (all the existed accounts with entered name will be displayed!) : ''')
                mark = 0
                for i in range(48, 58):
                    if ord(search[0]) == i:
                        mark = 1
                        break
                if mark == 0:
                    finded_accounts_list = []
                    flag = 0
                    for account in bank_list:
                        if account[1] == search:
                            finded_accounts_list.append(account)
                            flag = 1
                    if flag == 1:
                        if len(finded_accounts_list) == 1:
                            print(f'\n\'{search}\' has {len(finded_accounts_list)} Account:\n')
                        else:
                            print(f'\n\'{search}\' has {len(finded_accounts_list)} Accounts:\n ')
                        print("|{0: ^24}|{1: ^24}|{2: ^24}|".format('ACCOUNT NUMBER','ACCOUNT OWNER','BALANCE'))
                        for account in finded_accounts_list:
                            for item in account:
                                print("|",end='')
                                print("{0: ^24s}".format(item),end='')
                            print("|",end='\n')
                            
                        break
                    else:
                        print(f"\n\'{search}\' doesn't have any Account in the Bank ..!")
                        break
                elif mark == 1:
                    flag = 0
                    for account in bank_list:
                        if account[0] == search:
                            flag = 1
                            break
                    if flag == 0:
                        print("\nThere is no account with this account number ..")
                        break
                    else:
                        number = account[0]
                        name = account[1]
                        money = account[2]
                        a = Account(number,name,money)
            while(True):
                print('=====================================================================')
                print("""
                1. Show History of this account
                2. Give amount of money to this account
                3. Take amount of money of this account
                4. Back to Main Menu

                """)
                search_list = ['1','2','3','4']
                search = input("\nChoose an option: ")
                if search not in search_list:
                    print("    UNKNOWN CHOICE .. Go back to account    ")
                    break
                elif search == '1':
                    a.history()
                elif search == '2':
                    a.deposit()
                elif search == '3':
                    a.withdraw()
                elif search == '4':
                    break
            break
#====================================================================================================#
    elif menu_choice == '3':
        if bank_list == []:
            print("\nThere is no account in bank ..")
        else:
            print('\n+==========================================================================+')
            print("|{0: ^24}|{1: ^24}|{2: ^24}|".format('ACCOUNT NUMBER','ACCOUNT OWNER','BALANCE'))
            print('+==========================================================================+')
            for account in bank_list:
                for item in account:
                    print("|",end='')
                    print("{0: ^24s}".format(item),end='')
                print("|",end='\n')
                print('+--------------------------------------------------------------------------+')
#====================================================================================================#
    elif menu_choice == '4':
        if bank_list == []:
            print("\nThere is no account in bank ..")
        else:
            transaction_sum = 0
            name = input('\nEnter a name: ')
            flag = 0
            for account in bank_list:
                if account[1] == name:
                    flag = 1  
                    transaction_sum = transaction_sum + int(account[2])
            if flag == 0:
                print("\nThere is no account with this name..")
            else:
                print(f'\nSummation of transaction of {name}\'s accounts is:')
                print('   {0:,d} $'.format(transaction_sum))
#====================================================================================================#
    elif menu_choice == '5':
        print("""\n\n\n\nYou are done ..!""")
        break
#====================================================================================================#
            

        
        
    
