#default parameter in functios
def info(id,name,city='KL'):
    print(f'Details as follows \nID: {id} \nName: {name} \nCity: {city}')

info(1,'Sam','Mecca')
info(6,'Hadi')
info(22,'Mim')

def add(n1,n2=0,n3=0,n4=0,n5=0):
    return n1+n2+n3+n4+n5
print('Result: ',add(1,2))
print('Result: ',add(1,2,10,6,8))
print('Result: ',add(1,2,7))

#star before arguments to pass it as
#theres built in command like max and min
def add(*nums):
    return sum(nums)
print('Sum of 1,2 is: ',add(1,2))
print('Sum of 1,2,10,6,8 is: ',add(1,2,10,6,8))
print('Sum of 1,2,7 is: ',add(1,2,7))

def findMax(*nums):
    return max(nums)
print('max example')
print('max of 1,2 is: ',findMax(1,2))
print('max of 1,2,10,6,8 is: ',max(1,2,10,6,8)) #findmax can max also can
print('max of 1,2,7 is: ',max(1,2,7))

print('min example')
print('min of 1,2 is: ',min(1,2))
print('min of 1,2,10,6,8 is: ',min(1,2,10,6,8)) 
print('min of 1,2,7 is: ',min(1,2,7))


