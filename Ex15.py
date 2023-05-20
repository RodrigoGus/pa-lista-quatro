continuar = 0

while continuar != 50:
    nivel = int(input('''nivel de professor (1, 2 ou 3):    '''))
    h = float(input('numero de horas que deu aula no mes:    '))

    if nivel == 1:
        print(f'seu salario sera de R${h * nivel}')
        continuar += 1
    elif nivel == 2:
        print(f'seu salario sera de R${h * nivel}')
        continuar += 1
    elif nivel == 3:
        print(f'seu salario sera de R${h * nivel}')
        continuar += 1
    else:
        print('nivel de professor inexistente')