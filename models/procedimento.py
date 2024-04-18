from utils.utils import Utils
from config.config import Config

class Procedimento():
	def __init__(self, nome = None):
		self.__nome = nome
		self.__utils = Utils()
		self.__config = Config()

	def create(self):
		# Código para inserir um procedimento no banco de dados
		pass

	def read(self):
		return self.__utils.read_data('./data/dados_procedimentos.json')

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