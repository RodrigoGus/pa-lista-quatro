while True:
    nome = input('seu nome:    ')
    sexo = int(input('''qual o seu sexo?
    1 - PARA SEXO MASCULINO
    2 - PARA SEXO FEMININO
    '''))
    idade = int(input('qual a sua idade?    '))
    saude = int(input('''alguem problema de saude que te impocibilite de servir?
    1 - PARA NAO
    2 - PARA SIM
    '''))

    if sexo == 1 and idade >= 18 and saude == 1:
        print(f'''{nome} - HOMEM - {idade} - SEM PROBLEMAS SEVEROS DE SAUDE
voce esta apto a cumprir o servico militar obrigatorio''')
    else:
        print(f'''{nome} - HOMEM - {idade} - SEM PROBLEMAS CONSIDERAVEIS DE SAUDE
        voce nao esta apto a cumprir o servico militar obrigatorio''')