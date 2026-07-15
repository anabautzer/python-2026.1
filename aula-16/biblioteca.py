def preencher_lista(l: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem == ".":
            break
    else:
        l.append(elem)
        
def exibir_lista(l: list) -> None:
    print()
    for ind, elem in enumerate(l):
        print(f"{ind} -> {elem}")

# funções
def retornar_ultimo(l: list) -> str:
    ultimo = l[-1]
    return ultimo