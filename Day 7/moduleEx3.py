import datetime
import inspect
dtclasses=inspect.getmembers(datetime, inspect.isclass)

print('all clssses in datetime module')
for n, func in dtclasses:
    print(n,end='\t')

print('\n-----Today-----\n')
print(datetime.date.today())

print('\n-----Current Date & Time-----\n')
print(datetime.datetime.now())

print('\n-----Current Time-----\n')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S %p')

print('Current time',cttime)
print('Formatted time',formatedtime)

