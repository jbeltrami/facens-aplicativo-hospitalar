from utils.utils import Utils

class Paciente():
	def __init__(self, nome = None, idade = None, genero = None):
		self.__nome = nome
		self.__idade = idade
		self.__genero = genero

	def create(self):
		# Código para inserir um paciente no banco de dados
		pass

	def read(self):
		# Código para ler um paciente no banco de dados
		pass

	def update(self):
		# Código para atualizar um paciente no banco de dados
		pass

	def delete(self):
		# Código para deletar um paciente no banco de dados
		pass

# Verificar se o paciente existe antes de incluir no bd

'''
	{
		'id_paciente': 1,
		'nome': 'João',
		'idade': 25,
		'genero': 'M'
	}
'''