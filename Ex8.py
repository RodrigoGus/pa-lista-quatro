continuar = 0

while continuar != 10:
    nome = input('nome:    ')
    idade = int(input('idade:    '))
    sexo = input('sexo (M/F):    ')

    if sexo.upper() == 'M' and idade >= 30:
        print(f'{nome}, seu salario sera de R$100,00')
    elif sexo.upper() == 'M' and idade < 30:
        print(f'{nome}, seu salario sera de R$50,00')
    elif sexo.upper() == 'F' and idade >= 30:
        print(f'{nome}, seu salario sera de R$200,00')
    elif sexo.upper() == 'F' and idade < 30:
        print(f'{nome}, seu salario sera de R$80,00')
    else:
        print('nome, idade ou sexo errados')