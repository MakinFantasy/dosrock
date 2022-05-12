from os import name


for n in range(516):
    b = f'{n:b}'
    if n % 2 == 0:
        b += '10'
    else:
        b = '1' + b + '01'
    if int(b, 2) > 516:
        print(n)
        break