# username=input("Enter User Name \t")
# age=int(input("enter age"))
# salary=float(input("Enter Salary"))
# dataKnw=bool(input("Do you know databases?"))
# print("Name: ",username)
# print("Welcome Mr.\\Ms. \t",username)
# print("Your age is: ",age)
# print("You wish your salary is: ",salary)
# print("Know the databases?",dataKnw)

#Adding Two Numbers
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = \t {result}")

# #Multiply Two Numbers
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1*num2
# print(f"Result after multiplication {num1} and {num2} = \t {result}")

# #Division Two Numbers
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1/num2
# print(f"Result after Dividing {num1} by {num2} = \t {result}")

# # % finding Remainder Example
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1%num2
# print(f"Remainder after Dividing {num1} by {num2} = \t {result}")

# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=int(num1/num2)
# print(f"Remainder after Dividing {num1} by {num2} = \t {result}")

#taking more than one input using sinle line
num1,num2=input("Enter two number seperated by space").split()
result=int(num1)+int(num2)
print(f"Numbers Entered by you are {num1} and {num2} and addition of numbers {result}")
