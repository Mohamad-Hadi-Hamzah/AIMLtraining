
import os
#this is to create the file
# filepath=r'/Users/marinacherani/Downloads/AIML/Day 8/test'
# filename=input('Enter file name to create file: ')
# fullpath=os.path.join(filepath,filename)

# file=open(fullpath,'w')

# content=input('Enter text to write in file: ')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in file')
# file.close()


#this is to update the file
filepath=r'/Users/marinacherani/Downloads/AIML/Day 8/test'
filename=input('Enter file name to update file: ')
fullpath=os.path.join(filepath,filename)

if(os.path.exists(fullpath)):
    file=open(fullpath,'a')

    content=input('Enter text to write in file: ')
    file.write(content)
    print(f'File {filename} updated')
    file.close()

else:
    print(f'No such file {filename} exists')

#or kalau nak masukkan in current folder then 'get current directory'
#filepath=os.getcwd