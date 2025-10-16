# subjects=('python','maths','architecture','art','graphic')
# print('\n All subjects are: \n' )
# print('Number of subjects are: ',len(subjects))
# for sub in subjects:
#     print(sub,end='\t')

# numbers=(2,3,10,2,3,5,50,1)
# print('Total number in tuple:',len(numbers))
# for num in numbers:
#     print(num,end='\t')

# #tupleName.index(item) will return the index of first occurance of item in tupleName.
# searchNum=int(input('\n Enter number to find out index: '))
# if searchNum in numbers:
#     print(f'Index of {searchNum} is: \t',numbers.index(searchNum))
# else:
#     print(f'No such Number {searchNum} in our tuple')

# #tupleName.count(item) will return the number of times item occurs in tuple
# searchNum=int(input('\nEnter number to find out frequency: '))
# if searchNum in numbers:
#     print(f'Number of times: {searchNum} has occured:',numbers.count(searchNum))
# else:
#     print(f'No such Number {searchNum} in our tuple')

# searchNum=int(input('\nEnter number to find out frequency: '))
# if searchNum in numbers:
#     print(f'Number of times: {searchNum} has occured: {numbers.count(searchNum)} times')
# else:
#     print(f'No such Number {searchNum} in our tuple')

#write a program to sum a list with 4 numbers
numlist=[2,2,2,5]
print('Numbers are:',numlist)
total=sum(numlist)
print('The sum is:',total)

#write a program to sum a tuple with 4 numbers
numlist=(2,2,2,5)
print('Numbers are:',numlist)
total=sum(numlist)
print('The sum is:',total)

numlist = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numlist.append(num)

total = sum(numlist)
print("The sum is:", total)
