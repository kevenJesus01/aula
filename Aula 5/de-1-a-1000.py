print("Todos os números de 2 até 1000 em 2 em 2:")
for numero in range(2, 1001, 2):
    print(numero, end=' ')
print("\n")

print("Números pares de 1 até 1000:")
for numero in range(1, 1001):
    if numero % 2 == 0:
        print(numero, end=' ')
