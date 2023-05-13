continuar = True

while continuar:
    nome = input('nome:    ')
    idade = int(input('idade:    '))
    grupo_risco = input('grupo de risco (BAIXO, MEDIO ou ALTO):    ')
    if idade < 17 or idade > 70:
        print("idade precisa estar entre 17 e 70 anos")
    elif idade >= 17 and idade <= 20:
        if grupo_risco.upper() == "BAIXO":
            categoria = 1
        elif grupo_risco.upper() == "MEDIO":
            categoria = 2
        elif grupo_risco.upper() == "ALTO":
            categoria = 3
        else:
            print('grupo de risco nao identificado')
    elif idade >= 21 and idade <= 24:
        if grupo_risco.upper() == "BAIXO":
            categoria = 2
        elif grupo_risco.upper() == "MEDIO":
            categoria = 3
        elif grupo_risco.upper() == "ALTO":
            categoria = 4
        else:
            print('grupo de risco nao identificado')
    elif idade >= 25 and idade <= 34:
        if grupo_risco.upper() == "BAIXO":
            categoria = 3
        elif grupo_risco.upper() == "MEDIO":
            categoria = 4
        elif grupo_risco.upper() == "ALTO":
            categoria = 5
        else:
            print('grupo de risco nao identificado')
    elif idade >= 35 and idade <= 64:
        if grupo_risco.upper() == "BAIXO":
            categoria = 4
        elif grupo_risco.upper() == "MEDIO":
            categoria = 5
        elif grupo_risco.upper() == "ALTO":
            categoria = 6
        else:
            print('grupo de risco nao identificado')
    elif idade >= 65 and idade <= 70:
        if grupo_risco.upper() == "BAIXO":
            categoria = 7
        elif grupo_risco.upper() == "MEDIO":
            categoria = 8
        elif grupo_risco.upper() == "ALTO":
            categoria = 9
        else:
            print('grupo de risco nao identificado')