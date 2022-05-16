class CheckingAccount:
    # account initialising with basic account details
    def __init__(self, name, address, accountNumber, balance):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber 
        # balance is private
        self._balance = balance
    def debit(self, amount):
        if(self._balance >= amount):
            self._balance -= amount
        else:
            print('BALANCE IS NOT SUFFICIENT!')
    
    def credit(self, amount):
        self._balance += amount

    def displayDetails(self):
        print()
        print('ACCOUNT DETAILS')
        print("-"*40); # for the output border
        print("ACC NUMBER: ", self.accountNumber)
        print("NAME: ", self.name)
        print("ADDRESS: ", self.address)
        print("BALANCE: ", "$", self._balance)
        print("-"*40); # for the output border
        print()