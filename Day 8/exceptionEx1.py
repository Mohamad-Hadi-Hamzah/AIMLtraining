
try:
    fnum=float(input('Enter first nuber: '))
    snum=float(input('Enter second nuber: '))
    result=fnum/snum
    print(f'Result:{round(result,4)} after dividing {fnum} by {snum}')

except Exception as e:
    print('error',e)

finally:
    print('lalalala')
