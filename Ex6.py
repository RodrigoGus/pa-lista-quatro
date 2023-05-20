continuar = True

while continuar:
    preco = float(input('preco do carro:    R$'))
    ano = int(input('ano do carro:    R$'))

    if ano <= 2000:
        preco = preco - (preco * 0.12)
        perc = 12
    else:
        preco = preco - (preco * 0.07)
        perc = 7
    print(f'o carro teve um deconto de {perc}% e custara apenas {preco}')

    pergunta = input('gostaria de calcular o preco de outro carro? (S/N)    ')

    if pergunta.upper() == "S":
        continuar = True
    elif pergunta.upper() == "N":
        continuar = False
    else:
        print('"S" para sim e "N" para nao, tendeu?')