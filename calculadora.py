while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite um número válido')
        print()
        continue

    """
        como estamos usando while e o usuário não digitou um valor aceitável
        se não tivesse o CONTINUE o código só informaria o erro, mas não conseguiria
        descer até o próximo if, assim o continue faz o código subir
        e pede novamente um número ao usuário.
    """

    num1 = int(num1)
    num2 = int(num2)


    if operador == '+':
        soma = int(num1) + int(num2)
        print(f'O resultado da soma é {soma}')
    elif operador == '-':
        sub = int(num1) - int(num2)
        print(f'O resultado da subtração é {sub}')
    elif operador == '*':
        mult = int(num1) * int(num2)
        print(f'O resultado da multiplicação é {mult}')
    elif operador == '/':
        div = int(num1) / int(num2)
        print(f'O resultado da divisão é {div}')
    elif operador == '**':
        pot = int(num1) ** int(num2)
        print(f'O resultado da potenciação é {pot}')
    else:
        print('Operador inválido')

    sair = input('Deseja sair [s]im ou [n]ão: ')

    if sair == 's':
        break

