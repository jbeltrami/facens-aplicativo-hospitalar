import pandas as pd
from config.config import Config


class Utils_Logs():
	def __init__(self):
		self.__config = Config()

	def create_data(self, data, path):
		df = pd.read_json(self.__config.config_logs)
		df = pd.concat([df, data])

		# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
		return df.to_json(self.__config.config_logs, orient="records")

	def read_data(self, path):
		return pd.read_json(self.__config.config_logs)
