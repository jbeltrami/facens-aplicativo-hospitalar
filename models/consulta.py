class Consulta():
	def __init__(self, nome, data, procedimentos=[]):
		self.__nome = nome
		self.__data = data
		self.__procedimentos = procedimentos

	def create(self):
		# Código para inserir uma consulta no banco de dados
		pass

	def read(self):
		# Código para ler uma consulta no banco de dados
		pass

	def update(self):
		# Código para atualizar uma consulta no banco de dados
		pass

	def delete(self):
		# Código para deletar uma consulta no banco de dados
		pass


# Verificar se o procedimento existe antes de ser inserido na consulta
# Se nao existe, salvar o procedimento no banco de dados


'''
	{
		'id_consulta': 1,
		'nome': 'nome_do_paciente',
		'data': '01/01/2021',
		'procedimentos': [
			{
				'nome': 'Nome_do_procedimento',
				'data': '01/01/2021',
			},
			{
				'nome': 'Nome_do_procedimento',
				'data': '01/01/2021',
			}
		]
	}
'''