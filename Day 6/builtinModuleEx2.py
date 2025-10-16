import datetime
import inspect

print('Today is (Date):',datetime.date.today())

dtclasses = inspect.getmembers(datetime, inspect.isclass)
print('All Classes inside datetime module')

for n, func in dtclasses:
    print(n)

print('All functions inside datetime class')
functions=inspect.getmembers(datetime.date, inspect.isbuiltin)
for n, func in functions:
    print(n)

#ni contoh operating system
import os
import inspect
functions=inspect.getmembers(os, inspect.isbuiltin)
for n,func in functions:
    print(n)

listDirs=os.listdir()
for dir in listDirs:
    print(dir)

#ni contoh lagi entahlah nanti pkir kenapa susah2 tsip yg kat atas if bawah boleh?
import os
listDirs=os.listdir()
for dir in listDirs:
    print(dir)
    