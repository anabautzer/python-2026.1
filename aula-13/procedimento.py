import os
os.system("cls")

# subalgoritmo - procedimento e função
# procedimento - executa uma rotina e não retorna valor ao programa ser chamado
# função - executa uma rotina e retorna valor no programa chamador

# função
def exibir_tabuada(inicio: int, mult: int) -> None:

    for i in range(1, mult + 1, 1):
        conta = i * inicio
        print(f"{inicio} x {i} = {conta}")

# programa principal 

inicio = int(input("Tabuada: "))
mult = int(input("Multiplicador: "))
exibir_tabuada(inicio, mult)