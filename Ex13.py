inicial = int(input('valor inicial:    '))
final = int(input('valor final:    '))
par = 0
impar = 0

while inicial != (final + 1):
    if inicial % 2 == 0:
        par += 1
    else:
        impar += 1
    inicial += 1
print(f'''pares: {par}
impares: {impar}''')