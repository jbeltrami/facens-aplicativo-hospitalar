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

		print(input_procedimento)
		print(procedimento)


		
	def read(self):
		lista_procedimento = self.__utils.read_data(Config().config_procedimento)
		print(lista_procedimento)



	def update(self):
		# Código para atualizar um procedimento no banco de dados
		pass

	def delete(self):
		# Código para deletar um procedimento no banco de dados
		pass
'''
	{
		'nome': 'nome_do_procedimento',
	}
'''