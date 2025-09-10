# Componentes: Andriy Gabriel Magnago Polastrelli, Cauã Rosa do Espirito Santo, Thiago de Aguiar da Silva
# Grupo: Popcorners
# Ifes Serra, ES
# Data: 27/08/2025
# Esse programa lê um arquivo de texto com dados de produtos [nome, valor, unidades totais, unidades vendidas] e os armazena em um Dicionário
# (mais no futuro) 

import mod_atv3

def main():
	dic = mod_atv3.f_carregaProdutos() # função a)
	mod_atv3.f_vendeProdutos(dic) # função b)
	mod_atv3.f_relatorioVendasConsole(dic) # função c)
	mod_atv3.f_relatorioVendasArquivo(dic) # função d)
	mod_atv3.f_relatorioReporEstoqueConsole(dic) # função e)
	mod_atv3.f_relatorioReporEstoqueArquivo(dic) # função f)
if __name__ == '__main__':
	main()