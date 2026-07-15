import os
os.system("cls")

"""
Entregar tudo junto
Exercicios:
1. Faça uma função chamada calcular_delta, que passe 3 parâmetros e calcule o valor de delta.
2. faça uma função que passe 2 numeros por parâmetro e retorne o maior valor
3. Faça uma função que passe 3 numeros por parâmetro e retorne o menor valor
4. Faça um procedimento que passe 2 numeros por parametro e exba-os em ordem crescente
Considerando que a lista é somente de números
    5 - Somar os elementos da lista
    6 - Calcular a media dos elementos
    7 - Exibir o maior valor da lista"""

def calcular_delta(va: float, vb: float, vc: float) -> float:
    delta = va + vb + vc
    return delta

a = 10
b = 20
c = 30

resp = calcular_delta(a, b, c)
print("O calculo é: ", resp)

