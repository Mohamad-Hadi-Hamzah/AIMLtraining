# # Assignment operators: =, +=, -=
# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \nDiscount: {discount} \nDiscountedPrice:{disPrice}")

# salary=50000.50
# bonus=5000.60

# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus #salary=salary-tds
# print("Salary with Bonus",salary)

# Assignment operators: =, +=, -=

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")

# salary-=tds #salary=salary-tds
# print("Salary after tax",salary)

#Comparison operator
#if(condition)
# #code
#else
# #code

# age=int(input("Enter your age"))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("you are not eligible to cast yuor vote, You have to wait")
# print("End of Program")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in Exam")
# else:
#     print("Clear the Exam")

#accessCode="wes12"
# accessCode=input("Enter Access Code")
# if(accessCode!="wes12"):                #!= means not equal to
#     print("Invalid Access Code")
# else:
#     print("Welcome to your course")

# accessCode=input("Enter Access Code")
# if(accessCode=="wes12"):                #== means equal
#     print("Welcome to your course")
# else:
#     print("Invalid Access Code")  

#Logical operators: and, or, not.
# phyMarks=int(input("Enter marks obtained in Physics: "))
# cheMarks=int(input("Enter marks obtained in Chemistry: "))
# mathMarks=int(input("Enter marks obtained in Mathematics: "))   

# if((mathMarks>=55) and (phyMarks>=50) and(cheMarks>=60)):
#     print("You are eligible for the pre exam of MBBS")
# else:
#     print("You do not have the required marks")

# idProof=input("Enter your ID Proof")
# if((idProof=="passport") or (idProof=="dl")or(idProof=="voter id")):
#     print(f"Valid Id {idProof} we accept here")
# else:
#     print("Only passport, dl and voter id are accepted as Identity Proof")
#     print(f"{idProof}:is not valid ID here")

# mathMarks=int(input ("Enter marks obtained in Mathematics: "))
# gapYear=int(input ("Enter Gap Year if any otherwise 0"))
# if((mathMarks<=55) and (gapYear!=0)):
#     print("Not Eligible for BTech")
# else:
#     print("Eligible for BTech")

name=input("Enter Username: ")
if(not name):
    print("Error!!!")
else:
    print("Welcome",name)
    