continuar = 0

while continuar != 5:
    a = float(input('insira um número:    '))
    b = float(input('insira outo número:    '))
    c = input('insira um operador:    ')

    if c == '+':
        print(f'a + b = {a+b}')
        continuar += 1
    elif c == '-':
        print(f'a - b = {a-b}')
        continuar += 1
    elif c == '*':
        print(f'a * b = {a*b}')
        continuar += 1
    elif c == '**':
        print(f'a * b = {a * b}')
        continuar += 1
    elif c == '/' and b == 0:
        print(f'erro')
        continuar += 1
    elif c == '//' and b == 0:
        print(f'erro')
        continuar += 1
    elif c == '/':
        print(f'a / b = {a/b}')
        continuar += 1
    elif c == '//':
        print(f'a // b = {a//b}')
        continuar += 1

    elif c == '%':
        print(f'a % b = {a%b}')
        continuar += 1
    else:
        print('operador não definido')