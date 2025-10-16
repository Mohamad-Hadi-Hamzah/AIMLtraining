# print('write a function to find out the cube of given number')
# def cube(num):
#     return num ** 3
# n = int(input("Enter a number: "))
# print(f"The cube of {n} is {cube(n)}")

# def cubetest(num):
#     return num*num*num
# k = int(input("Enter a number: "))
# print(f"The cubic of {k} is {cubetest(k)}")

#write to find out bonus of given salary
# function take salary as input and return bonus (10% of salary)

def bonus(salary):
    return salary*0.1
a = int(input("Enter salary: "))
print(f"The bonus of {a} is {bonus(a)}")

def totalsalarywithbonus():
    return a+bonus(a)
print('Total salary and bonus would be: ',totalsalarywithbonus())