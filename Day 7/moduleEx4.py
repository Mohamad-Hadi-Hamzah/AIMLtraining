# import os
# import inspect
# print ('current Directory',os.getcwd())

# functions = inspect.getmembers(os, inspect.isbuiltin)

# print('All function in os module')
# for n,func in functions:
#     print(n,end='\t')

#create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folderName=input('Enter folder Name to create: \t ')
# folderPath=os.path.join(cdir,folderName)
# if(os.path.exists(folderPath)):
#     print('Folder already exist')
# else:
#     os.makedirs(folderPath,exist_ok=True)
#     print(f'{folderName} created at {folderPath}')

#rename a folder
#os.rename(folder_name,"rename_folder")

# import os
# cdir=os.getcwd()
# oldName=input('Enter old folder name:\t')
# newName=input('Enter new folder name:\t')

# oldPath=os.path.join(cdir,oldName)
# newPath=os.path.join(cdir,newName)

# if(os.path.exists(oldPath)):
#     os.rename(oldPath,newPath)
#     print(f'{oldName} renamed to {newName}')
# else:
#     print('No such folder exist')




import os
cdir=os.getcwd()
oldName=input('Enter old folder name:\t')
oldPath=os.path.join(cdir,oldName)

if(os.path.exists(oldPath)):
    newName=input('Enter new folder name:\t')
    newPath=os.path.join(cdir,newName)
    os.rename(oldPath,newPath)
    print(f'{oldName} renamed to {newName}')
else:
    print('No such folder exist')
    





    