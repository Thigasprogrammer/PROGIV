def f_carregaProdutos(arquivo: str) -> dict: #função que cria o dicionario

	# Definindo váriaveis

	dicgrupo = dict()
	lista = list()
	listaord = list()

	# Processamento

	with open(arquivo, 'r', encoding='utf-8') as arq_escrito:
		for linha in arq_escrito:
			lista = linha.split(";")
			i1 = float(lista[1])
			i2 = int(lista[2])
			i3 = int(lista[3])
			listaord.append(i1)
			listaord.append(i2)
			listaord.append(i3)
			dicgrupo[lista[0]]=listaord
			listaord = []

	return dicgrupo

def f_vendeProdutos(dic: dict) -> None:

	produto = input("Qual produto deseja comprar? (digite 'FIM' para terminar a compra): ")

	while produto != 'FIM':

		if produto in dic:
			valor = dic[produto][0]
			estoque = dic[produto][1]
			vendidas = dic[produto][2]
			quant = int(input("Digite a quantidade de produtos a ser comprada: "))
			if quant > 0 and quant <= (estoque - vendidas):
				vendidas = vendidas + quant
				dic[produto] = [valor, estoque, vendidas]
			else:
				print("QUANTIDADE INVÁLIDA")

		else:
			print("PRODUTO INEXISTENTE")

		produto = input("Qual produto deseja comprar? (digite 'FIM' para terminar a compra): ")

def f_relatorioVendasConsole(dicprod: dict) -> None:
	# ordenar alfabeticamente, pegar as chaves do dicionario, fazer uma lista ordenar a lista

	for nome_produto in dicprod:
		valortotal = dicprod[nome_produto][0]*dicprod[nome_produto][2]

		# usar .ljust para colocar as paradas no lado esquerdo

		print(" | {dicprod[nome_produto][2]} | {valortotal}"  % (nome_produto, dicprod[nome_produto][2], valortotal))

def main():
	dic = f_carregaProdutos('arquivo1.txt')
	print(dic)
	print()
	f_vendeProdutos(dic)
	print(dic)
	f_relatorioVendasConsole(dic)
	print("*"+'banana'.ljust(10)+"*")



main()