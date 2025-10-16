# numbers = [10,25,30,40,2,1]

# print('original list')
# for num in numbers:
#     print(num, end=' ')

# evenNum=list(filter(lambda x: x%2==0, numbers))
# print('\nEven numbers on list: ')
# for num in evenNum:
#     print(num, end=' ')

ourList=[4,2,5,6,7,3,1,10]

print('original list')
for num in ourList:
    print(num, end=' ')

lessFive=list(filter(lambda x: x<5,ourList))
print('\nNumbers less than 5 on list: ')
for num in lessFive:
    print(num, end=' ')


studentMarks={'sam':60,
              'raj':55,
              'lala':35,
              'nini':45,
              'sissy':76,
              'ola':99,
              'lalisa':88}

print('All students')
print(studentMarks)
passStudent=dict(filter(lambda i:i[1]>=50, studentMarks.items()))
print('students that passed exam')
print(passStudent)


#another contoh

studentMarks={'sam':60,
              'raj':55,
              'lala':35,
              'nini':45,
              'sissy':76,
              'ola':99,
              'lalisa':88}

print('All students')
for k,v in studentMarks.items():
    print(f'name {k} -> Marks {v}')
passStudent=dict(filter(lambda i:i[1]>=50, studentMarks.items()))
print('students that lulus exam')
for k,v in passStudent.items():
    print(f'name: {k} -> Marks {v}')

#to sort accordingly

sortPassStud=dict(sorted(passStudent.items(),key=lambda x:x[1]))

print('ascending order')
for k,v in sortPassStud.items():
    print(f'name: {k} -> Marks {v}')

sortPassStuddes=dict(sorted(passStudent.items(),key=lambda x:x[1],reverse=True))

print('decendindg order')
for k,v in sortPassStuddes.items():
    print(f'name: {k} -> Marks {v}')
