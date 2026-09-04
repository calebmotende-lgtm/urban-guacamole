class BankAccount:
    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no

#data 1 read
@property
def balance(self):
    print("Someone tried to read john's balance")
    return self.__balance

#to control updated
@balance.setter
def balance(self,value):
    print("Ensure you pass a number for new balance")
    if value<0:
        print("Ensure new balance must not beless than zero")
        return
    self.__balance=value