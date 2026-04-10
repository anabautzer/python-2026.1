import os
os.system("cls")

# estrutura de seleção: match case, comparação equivalentes
print("Digite um número de 1 a 7")
dia = int(input("Número: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _: # underline para definir qalquer outra coisa
        print("Erro, digite um número de 1 a 7")