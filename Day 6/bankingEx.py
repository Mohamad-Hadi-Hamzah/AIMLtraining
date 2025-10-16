# class Account:
#     def __init__(self,acHolder,bal):
#         self.acHolder=acHolder
#         self.bal=bal
    
#     def deposit(self,amount):
#         self.bal+=amount

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print('Balance after withdraw: ',self.bal)
#         else:
#             print('Insufficient amount in account')
#             print('Transaction Failed')

#     def show(self):
#         print(f'Account Holder name: {self.acHolder}\tAccount Balance: {self.bal}')

# ac1=Account('sameer',50000)
# ac2=Account('Chang',14000)
# ac1.show()
# ac2.show()

# ac1=Account('sameer',50000)
# ac1.show()
# wamount=float(input('Enter amount to withdraw: ')) #wamount=withdraw amount
# ac1.withdraw(wamount)

##contoh lagi

# class Account:
#     def __init__(self,balance,acHolder):
#         self.acHolder=acHolder
#         self.balance=balance
    
#     def getBalance(self):
#         return self.balance
# acc=Account(1000,'Sam')
# acc.balance=34000
# print(acc.balance)


##contoh lagi

class Account:
    def __init__(self,acHolder,bal):
        self.acHolder=acHolder
        self.bal=bal
    
    def deposit(self,amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw: ',self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed')

    def show(self):
        print(f'Account Holder name: {self.acHolder}\tAccount Balance: {self.bal}')

ac=Account('Sam',15000)
ac.show()
print('Please choose\n1.Deposit 2.Withdraw ')
choice = int(input())

if choice == 1:
    amt = float(input("Enter amount to deposit: "))
    ac.deposit(amt)
elif choice == 2:
    amt = float(input("Enter amount to withdraw: "))
    ac.withdraw(amt)
elif(choice==3):
    ac.show()

else:
    print("Invalid choice")



