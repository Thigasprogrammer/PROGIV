# Componentes: Andriy Gabriel Magnago Polastrelli, Cauã Rosa do Espirito Santo, Thiago de Aguiar da Silva
# Grupo: Popcorners
# Ifes Serra, ES
# Data: 27/08/2025
# Esse programa lê um arquivo de texto com dados de produtos [nome, valor, unidades totais, unidades vendidas] e os armazena em um Dicionário
# Após isso, vende os produtos, atualizando seu estoque e mostra: o relatório de vendas (via console e com criação de arquivo) 
# e o relatório dos produtos cujo estoque esgotaram (via console e criação de arquivo)

def f_carregaProdutos()->dict: # função a)
# Essa função lê o nome de um arquivo e o abre, montando a partir dele o dicionário que usaremos no programa
	arq = input("Digite o nome do arquivo: ") # Leitura do arquivo que vai ser aberto
	# Definição de variável
	linha = int() # Usada para passear nas linhas do arquivo
	lista = list() # Usada para salvar o que está nas linhas do arquivo
	lista2 = list() # Usada como valor do dicionário
	ldefrutas = dict() # Variável de dicionário

	with open(arq, 'r', encoding='utf-8') as arquivo: # O with abre o arquivo de nome informado em 'arq'
		for linha in arquivo: # O for passea e verifica as linhas do arquivo informado pelo usuário
			lista = linha.split(";") # Separa os itens da linha em uma lista, usando como parametro para a separação o ';'
			valor = float(lista[1]) # Transforma o segundo elemento (indice 1) da lista em float, essa variável armazena o preço do produto
			qinicial = int(lista[2]) # Transforma o terceiro elemento (indice 2) da lista em int, essa variável armazena a quantidade inicial de estoque do produto
			qvendida = int(lista[3]) # Transforma o quarto elemento (indice 3) da lista em int, essa variável armazena a quantidade vendida do produto
			lista2.append(valor)  # Adiciona na 'lista2' a váriavel valor, sendo seu primeiro elemento
			lista2.append(qtinicial) # Adiciona na 'lista2' a váriavel qtinicial, sendo seu segundo elemento
			lista2.append(qvendida) # Adiciona na 'lista2' a váriavel qvendida, sendo seu terceiro elemento
			ldefrutas[lista[0]] = lista2 # O primeiro elemento da lista é uma string com o nome do produto, ela é usada como chave do dicionario, e a lista2 é usada como valor
			lista2 = [] # Zera a lista2 para não haver sobreposição de dados
	return ldefrutas

def f_vendeProdutos(dicProd:dict): # função b)
	# Essa função vende os produtos, usando como 'banco de dados' o dicionário criado na função 'f_carregaProdutos'
	quantidade = int()
	vendidos = int()
	produto = input("Escolha um produto para a compra (digite 'FIM' para terminar a compra): ")

	while produto != "FIM": # Termina o loop quando o usuário digitar 'FIM' (maiúsculo)
		if produto in dicProd: # Verifica se o produto escolhido para a compra se encontra como chave no dicionário, caso não esteja desce para o else
			valor = dicProd[produto][0]
			estoque = dicProd[produto][1]
			vendidos = dicProd[produto][2]
			# As variáveis acima são criadas para salvar os valores do produto do dicionário
			quant = int(input("Digite a quantidade de produtos a ser comprada: "))
			if quant > 0 and quant <= (estoque - vendidos): # Esse condicional verifica se a quantidade escolhida para compra é menor que a quantidade inicial menos a de vendidos
				vendidos = quant + vendidos # Valor vendidos é atualizado com a quantidade fornecida
				dicProd[produto] = [valor, estoque, vendidos] # O valor do produto é atualizado com a nova quantidade de vendidos
			# OUTRA FORMA: dicProd[produto][2] = quant + vendidos (produto[2] é o 'vendidos')

			else: # Ocorre caso a quantidade escolhida não exista
				print("QUANTIDADE INVÁLIDA")
		else: # Ocorre caso o produto escolhido não exista na loja
			print("PRODUTO INEXISTENTE")
		produto = input("Escolha um produto (digite 'FIM' para terminar a compra): ")
		
def f_relatorioVendasConsole(dicProd:dict): # função c)
# Essa função faz o relatorio de vendas no console usando dicionario faz um calculo caso a quantidade seja > 0 para efetuar a função e logo depois formata o prin
	# Definição de variável
	total_vendas_geral = float()
	total_vendas_geral = 0 
	for nome_produto in sorted(dicProd.keys()): # Percorre o dicionário em ordem alfabética pelas chaves
		preco, qtd_inicial, qtd_vendida = dicProd[nome_produto] # Desempacota a lista associada a cada chave do dicionário
		

        # Bloco if caso a quantidade seja maior que 0
		if qtd_vendida > 0:
			total_vendas_produto = preco * qtd_vendida # Cálculo de vendas de cada protudo
			total_vendas_geral += total_vendas_produto # Soma o total de vendas no geral
			linha_formatada = f"{nome_produto.ljust(20)}|{str(qtd_vendida).rjust(8)}|{str(f'{total_vendas_produto:.2f}').ljust(8)}" # Cria um string que formata a linha usando ljust e rjust para dar o print corretamente
		
			print(linha_formatada) # Print da string
	print(f"TOTAL EM VENDAS = {total_vendas_geral:.2f}\n") # Print do total de vendas no geral

def f_relatorioVendasArquivo(dicProd:dict): # função d)
# Esta função é como a função e) (usamos a mesma lógica nos calculos, porém o relatório é feito em um arquivo de texto ao invés do console)
	nome_arquivo_saida = "relatorio_de_vendas.txt" # Nome do arquivo de saída
	total_vendas_geral = 0.0 # Criação de variável

	with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida: # Abre o arquivo em modo de write para modifica-lo
		
		for nome_produto in sorted(dicProd.keys()): # Percorre o dicionário (pelas chaves) em ordem alfabética novamente
			preco, qtd_inicial, qtd_vendida = dicProd[nome_produto] # Desempacota a lista associada a cada chave do dicionário
            

			if qtd_vendida > 0: # Bloco if caso a quantidade seja maior que 0
				total_vendas_produto = preco * qtd_vendida
				total_vendas_geral += total_vendas_produto
				linha_formatada = f"{nome_produto.ljust(20)}|{str(qtd_vendida).rjust(8)}|{str(f'{total_vendas_produto:.2f}').ljust(8)}\n"
				
				arquivo_saida.write(linha_formatada) # Escreve a linha formatada dentro do arquivo
		arquivo_saida.write(f"TOTAL EM VENDAS = {total_vendas_geral:.2f}\n") # Escreve o total de vendas no geral dentro do arquivo


def f_relatorioReporEstoqueConsole(dicProd:dict): # função e)
# Essa função da print em todos os produtos cujo estoque se esgotou

	for nome_produto in sorted(dicProd.keys()): # Passeando pelas chaves de dicProd (que são nome_produto), ordenando pela ordem alfabética
		preco, qtd_inicial, qtd_vendida = dicProd[nome_produto] # Transforma os valores em variáveis

		if qtd_inicial - qtd_vendida == 0: 
			linha_formatada = f"{nome_produto.ljust(20)}" # Cria uma string com nome_produto (banana, alface etc) e com espaço para 20 caracteres alinhados para esquerda
			print(linha_formatada) # Print dessa string


def f_relatorioReporEstoqueArquivo(dicProd:dict): # função f)
# Essa função cria um arquivo txt com todos os produtos cujo estoque se esgotou

	nome_arquivo_saida = "relatorio_de_reposicao.txt" # Nome do arquivo de saída

	with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida: # Abre o arquivo em write para modificar ele

	# O mesmo padrão da função anterior

		for nome_produto in sorted(dicProd.keys()):
			preco, qtd_inicial, qtd_vendida = dicProd[nome_produto]

			if qtd_inicial - qtd_vendida == 0:
				linha_formatada = f"{nome_produto.ljust(20)}\n"

				arquivo_saida.write(linha_formatada) # Ao invés de dar print, escreve no txt a string