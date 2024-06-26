lista_frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']

lista_alergias = ['kiwi', 'melancia', 'pêssego']

fruta_alergia = 'laranja'
lista_alergias.append(fruta_alergia)

for fruta in lista_frutas:
    if fruta in lista_alergias:
        print(f'{fruta} está na lista de alergias.')
