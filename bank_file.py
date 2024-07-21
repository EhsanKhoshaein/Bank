def load():
    bank_char_list = []
    bank_list = []
    bank_file = open('bank.txt','r')
    bank_char = bank_file.readlines()
    for account in bank_char:
        new_bank_char = account.split('\n')
        for item in new_bank_char:
            if item != '':
                bank_char_list.append(item)
    for item in bank_char_list:
            new_item = item.split(' , ')
            bank_list.append(new_item)
    bank_file.close()
    return bank_list

def save(account_list):
    account_char = ''
    i = 0
    while(i <= len(account_list)):
        if i == len(account_list)-1:
            account_char = account_char + account_list[i]
            break
        account_char = account_char + account_list[i] + ' , '
        i += 1
    bank_file = open('bank.txt','a')
    bank_file.writelines(account_char + '\n')
    bank_file.close()
    return bank_file

def rewrite(bank_list):
    bank_file = open('bank.txt','w')
    bank_file.close()
    for account in bank_list:
        account_char = ''
        i = 0
        while(i <= len(account)):
            if i == len(account)-1:
                account_char = account_char + account[i]
                break
            account_char = account_char + account[i] + ' , '
            i += 1
        bank_file = open('bank.txt','a')
        bank_file.writelines(account_char + '\n')
        bank_file.close()
    return bank_file
