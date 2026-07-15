import os
os.system("cls")

# subalgoritmo - procedimento e função
# procedimento - executa uma rotina e não retorna valor ao programa ser chamado, pode conter print e input no procedimento
# função - executa uma rotina e retorna valor no programa chamador, nunca use print e input dentro da função
# def serve tanto para função quanto procedimento

# Construção dos subalgoritmos

# Procedimentos - não retorna valor

def saudacao() -> None: # precisa definir o que é
    print("Bom dia, Ana")

def saudacao2(usuario: str) -> None: # parametro/argumento - informação que trafega entre os códigos, não é uma variável, para calcular algo
    print(f"Bom dia, {usuario}")

def saudacao3(usuario: str, hora: int) -> None: # parametro formal, o que ele espera. Assinatura da função
    if hora < 12:
        msg = "Bom dia" # variavel local
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {usuario}")

# Funções - retorna valor
def calcular_delta(va: float, vb: float, vc: float) -> float: # colocar nome completo para não confundir com variavel
    delta = (vb * vb) - (4 * va * vc)
    return delta # função sempre retorna algo, substitui a chamada

# Programa principal

# Parte da função
a = 1
b = 2
c = 3
resp = calcular_delta(a, b, c) # acompanhada de uma atribuição de valor
print("Delta = ", resp)
print("Delta = ", calcular_delta(-1, 2, 3)) # a função vem acompanhada de um print

# Parte do procedimento
saudacao()
saudacao2("Maria")
nome = input("Nome: ")
saudacao2(nome) # isolado em uma linha, não pode ter mais coisas escrita
saudacao3("Ana", 17) # parametro real - executar a função