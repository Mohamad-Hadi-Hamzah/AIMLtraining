# print("sets in python")
# setOne={'laptop','iphone','ipad','laptop'}
# print('Number of items are:',len(setOne))
# for item in setOne:
#     print(item,end=' ')

##clear():remove all the items from set
# setOne.clear()
# print('\n After clear number of items: ',len(setOne))
# for item in setOne:
#     print(item,end=" ")

##set.remove(item):updates the set and removes item from set.
# setOne.remove('iphone')
# print('After removing one item from set:',len(setOne))
# for item in setOne:
#     print(item,end=" ")

##union,intersection,difference
setOne={100,200,300,500,150}
setTwo={100,400,1300,150}

print(f'setOne contains {len(setOne)} items')
print(setOne)
print(f'setTwo contains {len(setTwo)} items')
print(setTwo)

##union (duplicated items takkan dikira masuk)
##s1.union(s2): Returns a new set with all the items from both sets s1,s2
uniounset=setOne.union(setTwo)#.union(setTwo,setThree,setFour)kalau byk set
print(f'Union of setOne and setTwo contains: {len(uniounset)} following items')

##intersection example (meaning common items)
interSet=setOne.intersection(setTwo)
print(f'Intersection of setOne and setTwo contains: {len(interSet)} following items')
print(interSet)

##difference example (meaning remove common items in set 1 but wont list set 2)
difSet=setOne.difference(setTwo)
print(f'Difference of setOne and setTwo contains: {len(difSet)} following items')
print(difSet)