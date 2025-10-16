# print("Welcome to Day 3 : Data Structure")
# print("List Example 1")
# my_list=[10,20,30,"Python",None,True,12.45]
# print('Number of items in list are:',len(my_list))
# for item in my_list:
#     print(item)


# print("List Example 2")
# emps=['Sam','Ravi','Tina']#pakai square bracket untuk list.Diff bracket meaning diff
# print('Number of employees:',len(emps))
# for employee in emps:
#      print(employee)  #ni for a list menurun

# # for employee in emps:
# #     print(employee,end=' ')   #ni dapat in single line

# # print(emps) #print as it is

# ##sort example
# emps.sort()
# print("List after sorting")
# for accend in emps:
#      print(accend, end='\n')

# ##reverse sort example
# #listName.reverse()

# emps.reverse()
# print("List after sorting")
# for decend in emps:
#      print(decend, end='\n')


# emps=['Sam','Ravi','Tina']
# print('Number of employees:',len(emps))
# for employee in emps:
#      print(employee)  

#append:adds the item at the end of the list
# newEmp=input("\nEnter Employee name to add in the list:\t")
# emps.append(newEmp)
# print('\nAfter adding new employee: Number of employees are:',len(emps))
# for employee in emps:
#      print(employee,end=' ')

#insert(index,item): This will add item at given index
# newEmp=input("\nEnter Employee name to add in the list:\t")
# position=int(input('Enter position you would like name added in:\t' ))
# emps.insert(position,newEmp)
# print('\nAfter adding new employee: Number of employees are:',len(emps))
# for employee in emps:
#      print(employee,end=' ')

#append,remove,pop insert method

emps=['Sam','Ravi','Tina']
print('Number of employees:',len(emps))
for employee in emps:
     print(employee)  
#listName.remove(item):will remove item from the list.
# deleteEmp=input("\nEnter Employee name to remove in the list:\t")
# emps.remove(deleteEmp)
# print('\nAfter deleting employee: Number of employees are:',len(emps))
# for employee in emps:
#      print(employee,end=' ')

#if wanna add if and else
# deleteEmp=input("\nEnter Employee name to remove in the list:\t")
# if deleteEmp in emps:
#     emps.remove(deleteEmp)
#     print('\nAfter deleting employee: Number of employees are:',len(emps))
#     for employee in emps:
#         print(employee,end=' ')
# else:
#     print(f'No such name \'{deleteEmp}\' in employee list')

#pop() example
#listName.pop(index): Will delete element at given index and return its value.
deleteIndex=int(input("\nEnter index to pop name:\t"))
print('Pop Result: ',emps.pop(deleteIndex))
print('Number of employees after pop() are: ',len(emps))
for employee in emps:
        print(employee,end=' ')

print('\n First Element in list: ',emps[0])
print('\n Last Element in list: ',emps[-1])




