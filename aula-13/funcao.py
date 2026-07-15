import os
os.system("cls")

# subalgoritmo - procedimento e função
# procedimento - executa uma rotina e não retorna valor ao programa ser chamado
# função - executa uma rotina e retorna valor no programa chamador

# criação de função
def verificar_maior_3n(n1: int, n2: int, n3: int) -> int:

    maior = n1
    if n2 > n1:
        maior = n2
    if n3 > maior:
        maior = n3 
    return maior

# programa principal

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

resp = verificar_maior_3n(n1, n2, n3)

print("O maior número é: ", resp)