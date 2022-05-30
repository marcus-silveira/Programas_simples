while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    contador = 10
    total = 0
    for index in range (19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * contador

        contador -= 1
        if contador < 2:
            contador = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            elif d < 9:
                d = d
            total = 0
            novo_cpf += str(d)
    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')
    break




