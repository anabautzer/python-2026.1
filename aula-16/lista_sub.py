import os
import biblioteca # deixar separada a função/procedimentos
os.system("cls")

# regra: se não obedecer, não funciona
# padrão: se não obedecer, funciona


# principal

lista = list()

# preencher uma lista até que seja digitado . (ponto)

# Exibir o conteudo de uma lista elemento a elemento

# Exibir o último elemento da lista

# menu

while True:
    print("""
    0 - Sair
    1 - Preencher lista
    2 - Exibir lista
    3 - Preencher último elemento
""")
    opcao = input("\nEscolha: ")
    match opcao:
        case "0":
            break
        case "1":
            print("\nDigite os elementos ou . (ponto) para sair")
            biblioteca.preencher_lista(lista)
        case "2":
            if len(lista > 0):
                biblioteca.exibir_lista(lista)
            else:
                print("\nA lista está vazia!")
        case "3":
            if len(lista > 0): # conta quantos elemento tem na lista
                ultimo = biblioteca.retornar_ultimo(lista)
                print("\nÚltimo elemento: ", ultimo)
            else:
                print("\nA lista está vazia!")
        case "_":
            print("\nOpção inválida")
    input("\nDigite algo para continuar")
        