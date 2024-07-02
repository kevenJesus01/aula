entrada = input("Digite uma string: ")
vogais = [c for c in entrada if c in 'aeiouAEIOU']
print("Vogais encontradas:", vogais)
print("Número de vogais:", len(vogais))
