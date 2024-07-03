def verifica_frete_gratis(cep):
    prefixos_norte_nordeste = [
        "60", "61", "62", "63", "64", "65", "66", "67",  # CE, MA, PI, RN, PB, PE, AL, SE
        "68", "69",  # AC, RO, AM, RR, PA, AP, TO
        "70", "71", "72", "73", "74", "75", "76", "77",  # BA
        "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",  # BA
        "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"  # PE, PB, RN, CE
    ]

    prefixo_cep = cep[:2]

    if prefixo_cep in prefixos_norte_nordeste:
        return "CEP elegível para frete grátis."
    else:
        return "CEP não é elegível para frete grátis."

cep = input("Digite o CEP: ")
resultado = verifica_frete_gratis(cep)
print(resultado)