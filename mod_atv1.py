def f_conjunto(frase:str) -> list: # Essa função retorna um conjunto e caracteres sem repetições
    frase = frase.upper() # Pode ser alterado
    desconsiderar = list()
    conjunto = list()

    for i in frase:
        if i not in desconsiderar:
            desconsiderar.append(i) 
            conjunto.append(i)

    
    return conjunto

def f_uniao(conj1:list, conj2:list)->list: # Essa função retorna uma lista com a união de duas listas
    uniao = list()

    for i in conj1:
        if i not in uniao:
            uniao.append(i)

    for i in conj2:
        if i not in uniao:
            uniao.append(i)

    return uniao

def f_intersecao(conj1:list, conj2:list)->list: # Essa função retorna uma lista com a interseção de duas listas
    intersecao = list()

    if len(conj1) > len(conj2):
        for i in range(len(conj1)):
            if conj1[i] in conj2:
                intersecao.append(conj1[i])

    else:
        for i in range(len(conj2)):
            if conj2[i] in conj1:
                intersecao.append(conj2[i])

    return intersecao