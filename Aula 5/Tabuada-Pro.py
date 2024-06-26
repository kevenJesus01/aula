def tabuada_completa(numero):
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

def calcular_elemento_tabuada(numero, multiplicador):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')

opcao = input('Deseja ver um número específico da tabuada (digite 1) ou a tabuada completa (digite 2)? ')

if opcao == '1':
    numero_tabuada = int(input('Digite o número da tabuada que você deseja ver: '))

    multiplicador = int(input('Digite o multiplicador desejado (1 a 10): '))

    if 1 <= multiplicador <= 10:
        calcular_elemento_tabuada(numero_tabuada, multiplicador)

    else:
        print('Entrada inválida. O multiplicador deve ser um número entre 1 e 10.')
elif opcao == '2':
    numero_tabuada = int(input('Digite o número da tabuada que você deseja ver: '))
    tabuada_completa(numero_tabuada)
else:
    print('Opção inválida. Por favor, digite 1 para ver um número específico da tabuada ou 2 para ver a tabuada completa.')

