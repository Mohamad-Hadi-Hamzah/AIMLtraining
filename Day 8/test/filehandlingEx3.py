
import os

filepath=os.getcwd()
filename=input('Enter file name to update file: ')
fullpath=os.path.join(filepath,filename)

if(os.path.exists(fullpath)):
    file=open(fullpath,'r')

    content=file.read()
    print('file contentas follows')
    print(content)
    file.close()

else:
    print(f'No such file {filename} exists')