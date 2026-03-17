import os
os.system ("cls")

# para pagar um determinado lanche n o parque de fiversões, o criterio é que so paga quem for adulto, crinças não pagam. Assim, fazer um algoritmo que peça a idade da pessoa e exiba na tela "Você paga", caso seja adulto

idade = int(input("Digite a sua idade: "))
if idade >= 18: # sempre precisa ter uma comparação
    print("Você paga") # bloco em python são tabulações

print("Aproveite o parque")