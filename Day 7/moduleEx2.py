# import random
# print('Random number from 1 to 1000')
# print(random.randint(1,10))

# import random
# name=input('Enter your name: ')
# luckyNum=random.randint(1,10)
# print(f'Welcome Mr\\Ms {name} Coupon Number: {luckyNum}')
# if(luckyNum==1):
#     print('you have won a million bucks')
# elif(luckyNum==3):
#     print('you have won an Ipad')
# elif(luckyNum==9):
#     print('you have won an Iphone')
# else:
#     print('Better luck next time')

import random
def findwinner():
    name=input('Enter your name: ')
    luckyNum=random.randint(1,10)
    print(f'Welcome Mr\\Ms {name} Coupon Number: {luckyNum}')
    if(luckyNum==1):
        print('you have won a million bucks')
    elif(luckyNum==3):
        print('you have won an Ipad')
    elif(luckyNum==9):
        print('you have won an Iphone')
    else:
        print('Better luck next time')



