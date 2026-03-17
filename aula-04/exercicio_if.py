import os
os.system ("cls")

# dado um número, exibir p seu módulo matematico, ou seja, se for digitado um número positivo, exibir o positivo e se for digitado um número negativo, transforma-lo em positivo e exibir

num = float(input("Digite um número: "))
if num < 0:
    num = num * - 1

print(f"Número: {num}")