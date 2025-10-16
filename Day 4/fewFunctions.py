#write a function to find table of even number

def  genTable(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter number to findout table: '))
genTable(number)