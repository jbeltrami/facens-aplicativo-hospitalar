import pandas as pd
from config.config import Config
from utils.utils_pacientes import Utils_Paciente

class Paciente():
	def __init__(self, nome = None, idade = None, genero = None):
		self.__nome = nome
		self.__idade = idade
		self.__genero = genero
		self.__utils = Utils_Paciente()

	def create(self):
		input_nome = input("Digite o nome do paciente: ")
		idade_input = input("Digite a idade do paciente: ")
		genero_input = input("Escolha o gênero do paciente: 1 - Masculino, 2 - Feminino: ")

		# Verifica genero
		if genero_input == '1':
			genero_input = 'Masculino'
		elif genero_input == '2':
			genero_input = 'Feminino'
		else:
			print("Opção inválida")
			return False

		# Ler lista de pacientes
		pacientes = self.__utils.read_data(Config().config_paciente)

		if input_nome in pacientes['nome'].values:
			print("Paciente já cadastrado")
			return False
		else:
			novo_paciente = pd.DataFrame( {
				'nome': [input_nome],
				'idade': [idade_input],
				'genero': ['Masculino' if genero_input == '1' else 'Feminino']
			})



			self.__utils.create_data(novo_paciente, Config().config_paciente)
			print("\n Paciente cadastrado com sucesso")



	def read(self):
		lista_pacientes = self.__utils.read_data(Config().config_paciente)
		print(lista_pacientes)

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