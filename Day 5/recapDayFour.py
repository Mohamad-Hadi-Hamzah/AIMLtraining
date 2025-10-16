def display():
    print('welcome to recap of functions')

def welcome(name):
    print('Welcome to functions Mr\\Ms ',name)

def cube(num):
    cubeNum=num*num*num
    print(f'cube of given number: {num} is =\t {cubeNum}')

def square(num):
    return num*num

# welcome('sam')
# display()
# myNum=int(input('Enter number to find out cube:\t'))
# cube(myNum)
# username=input('enter username: ')
# myNum=int(input('Enter number to find out cube and square: '))

# welcome(username)
# cube(myNum)
# print(f'square of given number: {myNum} is =\t {square(myNum)}')

def salBonus(salary):
    return salary*0.10

mySal=float(input('Enter salary to find out bonus: '))
bonus=salBonus(mySal)
print(f'Salary: {mySal} Bonus: {bonus}')
print(f'Salary after bonus = ,{mySal+bonus}')

def salbonus(salary):
    bonus=salary*0.10
    print(f'salary: {salary} bonus: {bonus}')

mySal=float(input('enter salary to find out bonus: '))
salBonus(mySal)
print(f'salary after bonus= ')