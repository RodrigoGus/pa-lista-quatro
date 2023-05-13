inicial = int(input('valor inicial:    '))
final = int(input('valor final:    '))
par = 0
impar = 0
num = inicial

while num <= final:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    num += 1
print(f'''pares: {par}
impares: {impar}''')