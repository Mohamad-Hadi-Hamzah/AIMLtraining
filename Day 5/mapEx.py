numbers = [10,25,30,40,2,1]
doubleNum=list(map(lambda x: 2*x, numbers))
print('\noriginal list')
for num in numbers:
    print(num, end=' ')

print('\nDouble list')
for num in doubleNum:
    print(num, end=' ')