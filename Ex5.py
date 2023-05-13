continuar = 0
nome = input('seu nome:    ')
salario = float(input('seu salario:    R$'))
minimo = float(input('valor do salario minimo:    R$'))

while continuar != 584:
    if salario <= (minimo * 3):
        salario_antigo = salario
        salario = salario + (salario * 0.5)
        continuar += 1
        porc = 50
    elif (minimo * 3) < salario <= (minimo * 10):
        salario_antigo = salario
        salario = salario + (salario * 0.2)
        continuar += 1
        porc = 20
    elif (minimo * 10) < salario <= (minimo * 20):
        salario_antigo = salario
        salario = salario + (salario * 0.15)
        continuar += 1
        porc = 15
    else:
        salario_antigo = salario
        salario = salario + (salario * 0.1)
        continuar += 1
        porc = 10

    print(f'{nome}, seu salario de R${salario_antigo} aumentou em {porc}% indo para R${salario}')
    print('proximo empregado...')
    nome = input('seu nome:    ')
    salario = float(input('seu salario:    R$'))
