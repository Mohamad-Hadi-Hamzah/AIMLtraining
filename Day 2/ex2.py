# num=1
# print('Printing Numbers from 1 to 100')
# while(num<=100):
#     print(num,end='/')
#     num+=1 #this is the condition to stop the number from repeating 1 till eternity

#Break example
# num=1
# print('Print Numbers from 1 to 100 before we get numbers divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         break
#     print(num,end=' ')
#     num+=1 #this is the condition to stop the number from repeating 1 till eternity

#continue example
# num=1
# print('Print Numbers from 1 to 100 before we get numbers divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         num+=1
#         continue #kira continue ni maksud dia macam ignore that just teruskan je
#     print(num,end='\t')
#     num+=1

# for i in range(1,100):
#      if(i%5==0):
#         continue
#      print(i,end='\t')

# correctPWD='lalaland'
# while True:
#     pwd=input('Enter Password to start')
#     if(correctPWD==pwd):
#         print('welcome, Access Granted')
#         break
#     else:
#         print('Wrong Password, Try Again')
# print('Game Started')

correctPWD='lalaland'
counter=0
while True:
    pwd=input('Enter Password to start\t')
    if(pwd==correctPWD):
        print('welcome, Access Granted')
        print('Game Started')
        break
    else:
        print('Wrong Password, Try Again')
        counter+=1
        if(counter>=3):
            print('Blocked. Too many wrong attempts')
            break
        
        

