from utils.utils_procedimentos import Utils_Procedimento
from config.config import Config
import pandas as pd

class Procedimento():
	def __init__(self, nome = None):
		self.__nome = nome
		self.__utils = Utils_Procedimento()
		self.__config = Config()

	def create(self):
		# Código para inserir um procedimento no banco de dados
		input_procedimento = input("Digitar procedimento realizado para cadastro: ")

		# Ler lista de procedimentos existente
		procedimento = self.__utils.read_data(Config().config_procedimento)

		if input_procedimento in procedimento['nome'].values:
			print("Procedimento já cadastrado")
			return False
		else:
			novo_procedimento = pd.DataFrame( {
				'nome': [input_procedimento]}
			)
#Conectar com Utils para suprir arquivo json base
			self.__utils.create_data(novo_procedimento, Config().config_procedimento)
			print("\nProcedimento cadastrado com sucesso")

		
	def read(self):
		lista_procedimento = self.__utils.read_data(Config().config_procedimento)
		print(lista_procedimento)

	def update(self):
# Código para atualizar um procedimento no banco de dados
# Ler lista de pacientes
		procedimento = self.__utils.read_data(Config().config_procedimento)
		print(procedimento)
		linha_do_procedimento = int(input('Escolha o numero do procedimento que deseja alterar na lista acima: '))
		
		
		# Verifica se o procedimento existe
		if linha_do_procedimento not in procedimento.index:
			print("Procedimento não Cadastrado")
			return False
		
		print(procedimento.loc[linha_do_procedimento])

		input_atualizacao = input('Atualize o nome do Procedimento Escolhido: ')
		procedimento.at[linha_do_procedimento,"nome"] = input_atualizacao

		#sobreescrever informação da lista de procedimentos
		self.__utils.update_data(procedimento, Config().config_procedimento)

	def delete(self):
		# Código para deletar um procedimento no banco de dados
		pass
'''
	{
		'nome': 'nome_do_procedimento',
	}
'''