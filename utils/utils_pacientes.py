import pandas as pd
from config.config import Config
from utils.utils_logs import Utils_Logs
from datetime import datetime


class Utils_Paciente():
	def __init__(self):
		self.__config = Config()
		self.__logs = Utils_Logs()

	def create_data(self, data, path):
		df = pd.read_json(self.__config.config_paciente)
		df = pd.concat([df, data])

		log = pd.DataFrame(
			{
				'DATETIME': [datetime.now()],
				'ACAO': 'CRIACAO',
				'DADO': [data]
			})

		self.__logs.create_data(log, self.__config.config_logs)

		# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
		return df.to_json(self.__config.config_paciente, orient="records")

	def read_data(self, path):
		log = pd.DataFrame(
			{
				'DATETIME': [datetime.now()],
				'ACAO': 'LEITURA',
				'DADO': ''
			}
		)
		self.__logs.create_data(log, self.__config.config_logs)
		return pd.read_json(self.__config.config_paciente)

	def update_data(self, data, updated_data, path):
		log = pd.DataFrame(
			{
				'DATETIME': [datetime.now()],
				'ACAO': 'ATUALIZACAO',
				'DADO': [updated_data]
			}
		)

		self.__logs.create_data(log, self.__config.config_logs)
		return data.to_json(self.__config.config_paciente, orient="records")

	def delete_data(self, data, removed_data, path):
		log = pd.DataFrame(
			{
				'DATETIME': [datetime.now()],
				'ACAO': 'DELECAO',
				'DADO': [removed_data]
			}
		)

		self.__logs.create_data(log, self.__config.config_logs)
		return data.to_json(self.__config.config_paciente, orient="records")
