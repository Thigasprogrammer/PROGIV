# Componentes: Andriy Gabriel, Cauã Rosa, Thiago de Aguiar
# Ifes Serra, ES
# Data: 20/08/2025
# Este programa recebe números reais quaisquer, faz uma lista com eles, ordenando-os crescentemente. Após isso,
# gera uma terceira lista usando os números reais ordenados de duas outras listas. Por fim, imprime as listas no formato 'LISTA[9]=99.99'.
import mod_atv2


def main():
	# Declaração de variáveis
	tam1 = int()
	tam2 = int()
	lista1 = list()
	lista2 = list()
	lista3 = list()

	# Leitura do usuário
	tam1 = int(input())
	tam2 = int(input())

	# Processamento
	lista1 = mod_atv2.f_preencheOrd(tam1) # Função a)
	lista2 = mod_atv2.f_preencheOrd(tam2) 

	lista3 = mod_atv2.f_intercalaOrd(lista1, lista2) # Função b)

	mod_atv2.f_impressaoreal(lista1) # Função c)
	mod_atv2.f_impressaoreal(lista2)
	mod_atv2.f_impressaoreal(lista3)


if __name__ == '__main__':
	main()