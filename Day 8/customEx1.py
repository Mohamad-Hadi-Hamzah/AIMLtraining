class InvalidAge(Exception):
    pass
def checkAge(age):
    if(age<=0):
        raise InvalidAge('Age should not be negative')
    elif(age<18):
        raise InvalidAge('Should not be a minor')
    elif(age>=150):
        raise InvalidAge('Unrealistic kot')
    elif(age>80):
        raise InvalidAge('Tua sgt nak kerja')
    else:
        print(f'age {age} is accepted and valid age for employment')

try:
    userage=int(input('Enter your age: '))
    checkAge(userage)
except InvalidAge as e:   #this will appear for age related error
    print('Invalid Age: ',e) 
except Exception as ex:   #this will appear for other error
    print('Error!!',ex)


    
    