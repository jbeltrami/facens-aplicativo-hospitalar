class Config():
	def __init__(self):
		self.__config_procedimento = './data/dados_procedimentos.json'
		self.__config_paciente = './data/dados_pacientes.json'
		self.__config_consulta = './data/dados_consultas.json'
		self.__config_logs = './data/logs.json'


	@property
	def config_procedimento(self):
		return self.__config_procedimento

	@property
	def config_paciente(self):
		return self.__config_paciente

	@property
	def config_consulta(self):
		return self.__config_consulta

	@property
	def config_logs(self):
		return self.__config_logs