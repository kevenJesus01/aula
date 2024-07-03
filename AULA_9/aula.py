import pandas as pd

dados = {
     "Nome": ["Gorki", "Darius", "Nunu", "Zed", "Varus", "Lux", "Aurelio"],
     "Idade": [75,32,4,24,34,19,99],
     "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]

}

df = pd.DataFrame(dados)

moradores_recife = df[df["Cidade"] == "Recife"]

print("Moradores do Recife:")
print(moradores_recife)
