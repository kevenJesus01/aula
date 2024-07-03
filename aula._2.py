import pandas as pd 

dados = pd.read_csv('./dados_ficticios (1).csv')

df = pd.DataFrame(data=dados)
print("-------------Voce Ganhou 4 mil---------------")
print(df[df['idade'] > 4])
print("-------------Voce Ganhou 50 mill--------------")
print(df[df['renda'] > 5])
print("-------------Voce Ganhou 15000 ---------------")
print(df[df['renda'] > 15])