import os
os.system("cls")

# vetor - tamanho definido pelo programador, armazena dados do mesmo tipo

vetor = [45, 34, 23, 12, -5]

print(vetor[1])
print(vetor)

for indice in range(0, 5, 1):
    print(f"V [{indice}] = {vetor[indice]}")

for numero in vetor:
    print(numero)

for indice, numero in enumerate(vetor):
    print(f"V [{indice}] = {numero}")

soma = sum(vetor)
print("Soma =", soma)

soma = 0
for numero in vetor:
    soma += numero
print("Soma =", soma)
