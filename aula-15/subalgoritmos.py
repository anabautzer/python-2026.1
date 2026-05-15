import os
os.system("cls")

# Construção dos subalgoritmos

# Procedimentos - não retorna valor

def saudacao() -> None: # precisa definir o que é
    print("Bom dia, Ana")

def saudacao2(usuario: str) -> None: # parametro/argumento - informação que trafega entre os códicos, não é uma variável, para calcular algo
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



# Programa principal

saudacao()
saudacao2("Maria")
nome = input("Nome: ")
saudacao2(nome)
saudacao3("Ana", 17) # parametro real - executar a função