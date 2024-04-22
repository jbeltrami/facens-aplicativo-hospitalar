import pandas as pd
from config.config import Config


class Utils_Consulta():
	def __init__(self):
		self.__config = Config()

	def create_data(self, data, path):
		df = pd.read_json(self.__config.config_consulta)
		df = pd.concat([df, data])

		# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
		return df.to_json(self.__config.config_consulta, orient="records")

	def read_data(self, path):
		return pd.read_json(self.__config.config_consulta)

	def update_data(self, data, path):
		return data.to_json(self.__config.config_consulta, orient="records")

	def delete_data(self, data, path):
		return data.to_json(self.__config.config_consulta, orient="records")
