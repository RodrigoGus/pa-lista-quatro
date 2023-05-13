continuar = 0
t_custo = 0
t_venda = 0

while continuar != 40:
    custo = int(input('preco de custo:    R$'))
    venda = int(input('preco de venda:    R$'))

    t_custo = t_custo + custo
    t_venda = t_venda + venda
    continuar += 1

if t_custo > t_venda:
    print('houve prejuizo')
elif t_custo < t_venda:
    print('houve lucro')
else:
    print('empate. nem prejuizo, nem lucro')

media_custo = t_custo / 40
media_venda = t_venda / 40

print(f'a sua media de custo foi de R${media_custo} e a media de venda foi de R${media_venda}')