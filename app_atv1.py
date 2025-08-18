import mod_atv1

def main():
    # Definindo variáveis
    frase1 = str()
    frase2 = str()
    lista1 = list()
    lista2 = list()
    lista3 = list() 
    lista4 = list()

    # Processamento
    frase1 = input()
    frase2 = input()

    lista1 = mod_atv1.f_conjunto(frase1) # Função a)
    lista2 = mod_atv1.f_conjunto(frase2) # Função b)
    lista3 = mod_atv1.f_uniao(lista1, lista2) # Função c)
    lista4 = mod_atv1.f_intersecao(lista1, lista2) # Função d)

    # Ordenando as listas
    lista1.sort()
    lista2.sort()
    lista3.sort()
    lista4.sort()

    # Dando print
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)








if __name__ == '__main__':
    main()