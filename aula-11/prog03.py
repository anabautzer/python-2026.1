import os
os.system("cls")

# mostrar a soma

v = [45, -89, 32, -12, 33]

print(sum(v)) # soma direto (não utilizar)

soma = 0
for elem in v:
    soma = soma + elem

print(soma)

def calcular_soma(v: list) -> int: # criação de comando
    soma = 0

    for elem in v:
        soma = soma + elem
    return soma

print(calcular_soma(v))

media = calcular_soma(v) / len(v)
print(media) # aproveitar o comando
