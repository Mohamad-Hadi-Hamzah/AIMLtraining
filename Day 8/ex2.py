from ourpack import calc
while True:
    try:
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter second number: '))
        op=input('Choose operation +,-,*,/')
        if(op=='+'):
            print('Result: \t',calc.add(fnum,snum))
        elif(op=='-'):
            print('Result: \t',calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result: \t',calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result: \t',calc.div(fnum,snum))
        else:
            print('wrong operation choice')
    except ZeroDivisionError as z:
        print('Division by 0 not allowed',z)
    except ValueError as v:
        print('Error in values',v)
    except Exception as e:
        print('erRAWR',e)
    finally:
        print('End of Program')

    choice=input('do yu wanna sambung? If yes enter y: ').lower()
    if(choice!='y'):
        print('Bye')
        break
