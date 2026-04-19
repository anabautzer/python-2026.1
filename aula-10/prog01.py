import os
os.system("cls")

# Forçar o usuário a digitar uma nota válida(entre 0 e 10) e no final mostrar a nota com o seu devido casting

numero = input("Número: ")

while not numero.isnumeric() or int(numero) >= 0 and int(numero) > 10: # maior igual ao zero ainda irá dar certo, e ainda irá dar erro com número negativo
    print("Erro! Não digitou um número")
    numero = input("Número: ")
else:
    numero = float(numero)

print("Você digitou uma nota valida")
