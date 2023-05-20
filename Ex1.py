continuar = 0
intervalo = 0

while continuar != 80:
    num = int(input('informe um valor:    '))
    if 10 <= num <= 150:
        continuar += 1
        intervalo = intervalo + 1
    else:
        continuar += 1

print(f'{intervalo} valor(es) estao entre 10 e 150')