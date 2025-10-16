# import math
# import random
# myNum=int(input('Enter number to find out square root'))
# print(f'Square root of {myNum} is: ',math.sqrt(myNum))

# print('Your lucky number from 1 to 100 is: '),random.randint(1,100)

#to check function inside module
import math
import inspect

functions = inspect.getmembers(math,inspect.isbuiltin)
for n, func in functions:
    print(n)
print('Sin 90 is: ',math.sin(90))
print('Cos 90 is: ',math.cos(90))
print('Tan 90 is: ',math.tan(90))

deg=int(input('Letaklah pape degree: '))
print(f'cos{deg} is:',math.cos(deg))



