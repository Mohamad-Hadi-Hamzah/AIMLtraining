def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

print('tadaaa Hadi calculator')
while True:
    print('Select Operation: \n1.Add \n2.Sub \n3.Multiply \n4.Division \n5.Average \n6.Exit')
    op=int(input('Enter operation of your choice (1-6): '))
    if(op==6):
        print('Thank you,bye')
        break
    if((op>6) or (op<=0)):    #ask chatgpt
        print('wrong operation')
    else:
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter second number: '))
        if(op==1):
            print(f'Result after adding {fnum} and {snum} : ',add(fnum,snum))
        elif(op==2):
            print(f'Result after substract {fnum} from {snum} : ',sub(fnum,snum))
        elif(op==3):
            print(f'Result after multiply {fnum} and {snum} : ',multi(fnum,snum))
        elif(op==4):
            print(f'Result after division {fnum} by {snum} : ',div(fnum,snum))
        elif(op==5):
            print(f'Average of {fnum} and {snum} : ',avg(fnum,snum))
    

    