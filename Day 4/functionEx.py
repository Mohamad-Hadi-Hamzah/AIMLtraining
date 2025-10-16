#function without parameter
def welcome():
    print('Welcome to Functions')
    print('My first function')

#after defining the function just recall it as many times as needed
welcome()
welcome()

#function with parameter
def hello(name):
    print('Welcome to Functions Mr\\Ms',name)

username=input('Enter your name: ')
hello(username)

#function with parameter and return
def addtotal(num1,num2):
    return num1+num2

fnum=int(input('enter 1st number: '))
snum=int(input('enter 2nd number: '))

print(f'Result after adding {fnum} and {snum} is = ',addtotal(fnum,snum))

#another example

def kali(num1,num2):
    return num1*num2

fnum=int(input('enter 1st number: '))
snum=int(input('enter 2nd number: '))

print(f'Result after multiplying {fnum} and {snum} is = ',kali(fnum,snum))

