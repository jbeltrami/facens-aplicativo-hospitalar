import pandas as pd
from config.config import Config
from utils.utils_pacientes import Utils_Paciente

class Paciente():
	def __init__(self, nome = None, idade = None, genero = None):
		self.__nome = nome
		self.__idade = idade
		self.__genero = genero
		self.__utils = Utils_Paciente()

	def verifica_genero(self, genero):
		if genero == '1':
			genero = 'Masculino'
		elif genero == '2':
			genero = 'Feminino'
		else:
			print("Opção inválida")
			return False

		return genero

	def create(self):
		input_nome = input("Digite o nome do paciente: ")
		idade_input = input("Digite a idade do paciente: ")
		genero_input = input("Escolha o gênero do paciente: 1 - Masculino, 2 - Feminino: ")

		genero_input = self.verifica_genero(genero_input)

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
			print("\nPaciente cadastrado com sucesso")

	def read(self):
		lista_pacientes = self.__utils.read_data(Config().config_paciente)
		print(lista_pacientes)

	def update(self):
		# Ler lista de pacientes
		pacientes = self.__utils.read_data(Config().config_paciente)
		print(pacientes)
		linha_do_paciente = int(input('Escolha o numero do paciente que deseja alterar, na lista acima: '))

		atualizacoes = {
			1: 'nome',
			2: 'idade',
			3: 'genero'
		}

		# Verifica se o paciente existe
		if linha_do_paciente not in pacientes.index:
			print("Paciente não encontrado")
			return False

		# Localiza informacoes do paciente, usando loc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
		print(pacientes.loc[linha_do_paciente])

		input_atualizacao = int(input('Escolha o que deseja atualizar: 1 - Nome, 2 - Idade, 3 - Gênero: '))

		if input_atualizacao not in [1,2,3]:
			print("Opção inválida")
			return False

		if input_atualizacao == 3:
			novo_valor = input('Digite o novo valor: 1 - Masculino, 2 - Feminino: ')
			novo_valor = self.verifica_genero(novo_valor)
		else:
			novo_valor = input('Digite o novo valor: ')

		pacientes.at[linha_do_paciente, atualizacoes[input_atualizacao]] = novo_valor


		# print(pacientes.loc[linha_do_paciente])
		self.__utils.update_data(pacientes, Config().config_paciente)


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