def sua_Matricula(numero_matricula):

    if numero_matricula % 2 == 0:
        print("Você Esta No Time blue")
    else:
        print("Você Esta no Time Mirelo")

try:
    numero = int(input("Digite um número: "))
    print("O número digitado é:", numero)
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
else:
    print("Nenhum erro ocorreu.")
finally:
    print("Finalizando o programa.")

sua_Matricula(numero)