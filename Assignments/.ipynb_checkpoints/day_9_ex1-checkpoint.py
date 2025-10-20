
def findGreatest(a, b, c):
    return max(a, b, c)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest = findGreatest(num1, num2, num3)
print(f"The greatest of the 3 numbers is: {greatest}")