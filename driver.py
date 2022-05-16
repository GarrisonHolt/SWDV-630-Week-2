import CheckingAccount

# asking the user for thier account details
name = input('Enter account holder name: ')
address = input('Enter  address: ')
accNumber = 'AC256710'
balance = float(input('Enter initial deposit: '))

# creating a new account
newAccount = CheckingAccount.CheckingAccount(name, address, accNumber, balance)

# for user options
option = ''

# repeat until user type 3 for exit
while option != '3':
    # display options
    print()
    print('Banking Options:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Exit')
    option = input('Enter option: ')

    # if option 1,then credit
    if option == '1':
        amount = float(input('Amount: '))
        newAccount.credit(amount)
        newAccount.displayDetails()
        
    # if option 2,then debit
    elif option == '2':
        amount = float(input('Amount: '))
        newAccount.debit(amount)
        newAccount.displayDetails()