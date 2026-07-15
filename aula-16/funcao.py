import os
os.system("cls")

# diferença em atribuir o valor em uma variavel e não atribuir

def verificar_maior(n1: float, n2: float) -> float:
    if n1 > n2:
        return n1
    else:
        return n2
    

num1 = 45
num2 = 99
print(f"O maior número entre {num1} e {num2} é {verificar_maior(num1, num2)}")