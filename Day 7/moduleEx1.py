# import math
# num=int(input('Enter Number to find out square root: '))

# print(f'Square root of {num} :\t',round(math.sqrt(num),2))


import math
import inspect

functions = inspect.getmembers(math, inspect.isbuiltin)
print('All function in math module')
for n,func in functions:
    print(n,end='\t')