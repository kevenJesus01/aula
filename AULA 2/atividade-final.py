
#criando tupla
linguagens_tupla = ('java', 'Pyton', 'Golang', 'C#', 'JavaScript' )

#tupla transformada em lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))

#Adicionar dois elementos
linguagens_lista.append(["Ruby", "Malboge"])
print(linguagens_lista)

linguagens_lista.pop(0)




print("lista com JAVA removido")
print(linguagens_lista)

print("primeiro elemento:")
print(linguagens_lista[0])


print("Quantidade de  elementos:")
print(len(linguagens_lista))



dicionario = {
    "Nome": "Keven",
    "Idade": 17,
    "Profissão": "Garoto do Programa"
}

print(dicionario["Nome"])

