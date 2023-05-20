continuar = True
confirm = 0

while continuar:
    num = float(input('informe um valor:    '))
    if num > 80 or num < 25 or num == 40:
        print(f'{num} é maior que 80, menor que 25 ou igual a 40')
        confirm = int(input('''deseja continuar?
1 - para sim
2 - para nao
'''))
    else:
        print(f'{num} nao é maior que 80, menor que 25 ou igual a 40')
        confirm = int(input('''deseja continuar?
1 - para sim
2 - para nao
'''))
        if confirm == 1:
            continuar = True
        elif confirm == 2:
            continuar = False
        else:
            print('resposta nao esperada')
