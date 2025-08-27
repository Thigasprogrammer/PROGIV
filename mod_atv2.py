def f_preencheOrd(tam:int)->list: # Função a)
	# Definindo variáveis
	listaord = list()
	item = float()

	# Processamento
	for i in range(tam):
		item = float(input())
		listaord.append(item)
	listaord.sort()
	
	return listaord

def f_intercalaOrd(conj1:list, conj2:list)->list: # Função b)
	# Pega o indice 0 da primeira lista e compara com o 0 da segunda lista, caso o da primeira lista seja maior, adiciona o 0 da segunda lista e compara o 0 da primeira com o 1 da segunda, 
	# Caso o 1 da segunda seja maior adiciona o 0 da primeira e compara o 1 da segunda com o 1 da primeira

    # Definindo variáveis
    lista3 = list()
    M = int()
    N = int()
    tam1 = len(conj1)
    tam2 = len(conj2)
    if len(conj1) == 1:
        tam1 = 2
    else:
        if len(conj2) == 1:
            tam2 = 2

    # Processamento
    while M <= (tam1-1) and N < (tam2-1):
        if conj1[M] >= conj2[N]:
            lista3.append(conj2[N])
            N += 1
        else:
            lista3.append(conj1[M])
            M += 1
    lista3.sort()

    return lista3

def f_impressaoreal(listan:list): # Função c)
	for i in range(len(listan)):
		print(f'LISTA[{i}]={listan[i]}')