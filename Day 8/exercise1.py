#take use marks from user within 0-50
#if user enter outside 0-50 raise Error InvalidMarks using Custom Exception
#Give chance to the user till, he/she entered valid marks

class InvalidMarks(Exception):
    pass
def checkMarks(marks):
    if(marks<0):
        raise InvalidMarks('Marks should not be negative')
    elif(marks>50):
        raise InvalidMarks('Should not be a more than 50')
    else:
        print(f'Marks {marks} is accepted')
        

while True:
    try:
        usermarks=int(input('Enter your marks: '))
        checkMarks(usermarks)    #kalau import mark from mark file mark.checkMarks(usermarks)
    except InvalidMarks as i:     #kalau import mark from mark file except mark.InvalidMarks as i:
        print('Invalid Marks: ',i) 
    except Exception as ex:   
        print('Error!!',ex)
    else:
        print ('recorded')
        break
    choice=input('Do you wanna reenter marks? If yes enter y: ').lower()
    if choice!=('y'):
        print('Bye')
        break

    
