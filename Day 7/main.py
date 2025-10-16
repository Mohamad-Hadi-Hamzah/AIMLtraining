from ourPack import welcome 
username=input('Please enter your name: ')

#option A
print(welcome.display(username))

#option B
msg=welcome.display(username)
print('Message for you: ',msg)

from ourPack import student
s1=student.Pelajar(1,'Rave')
s1.printInfo()
