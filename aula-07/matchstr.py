import os
os.system("cls")

# estrutura de seleção: match case, comparação equivalentes
dia = input("Digite o dia da semana: ")

match dia.lower(): #lower() é um método que converte tudo para minúsculo, upper() para maiúscula
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
        print("Dia útil")
    case "Sábado" | "Domingo": # barra | para ser como ou
        print("Final de Semana")
    case _: # underline para definir qualquer outra coisa
        print("Erro, digite um dia da semana")