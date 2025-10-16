employee={'id':1,'name':'Sam','salary':55000}
print(employee)

print('Employee details as follows:')
for key, value in employee.items():
    print(key,'->',value)

#Adding key in dictionary
employee['city']='Muscat'
print('Dictionary after adding City:')
for key, value in employee.items():
    print(key,'->',value)

#Deleting key in dictionary
del employee['salary']
print('Employee details after deleting salary:')
for key, value in employee.items():
    print(key,'->',value)

#Print all keys in dictionary
print('All keys from Employee:')
for k in employee.keys():
    print(k,end=' ')

#Print all values in dictionary
print('\nAll values from Employee:')
for v in employee.values():
    print(v,end=' ')

#Print key:value
print('\nKey : Value')
for k,v in employee.items():
    print(k,':',v)