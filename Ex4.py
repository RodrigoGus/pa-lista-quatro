while True:
    n = float(input('informe um numero:    '))

    if n > 0:
        print(f'{n} e positivo')
    elif n < 0:
        print(f'{n} e negativo')
    else:
        print(f'{n} e 0')