def load(account_number):
    account_char_list = []
    account_list = []
    account_file = open(f'{account_number}.txt','r')
    account_char = account_file.readlines()
    for account in account_char:
        new_account_char = account.split('\n')
        for item in new_account_char:
            if item != '':
                account_char_list.append(item)
    for item in account_char_list:
            new_item = item.split(' , ')
            account_list.append(new_item)
    account_file.close()
    return account_list
def save(account_number ,account_list):
    account_char = ''
    i = 0
    while(i <= len(account_list)):
        if i == len(account_list)-1:
            account_char = account_char + account_list[i]
            break
        account_char = account_char + account_list[i] + ' , '
        i += 1
    account_file = open(f'{account_number}.txt','a')
    account_file.writelines(account_char + '\n')
    account_file.close()
    return account_file
    
