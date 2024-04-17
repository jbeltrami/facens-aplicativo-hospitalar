import pandas as pd
from config.config import Config


class Utils():
	def __init__(self):
		pass

	def create_data(self, data, path):
		pass

	def read_data(self, path):
		return pd.read_json(path)

	def update_data(self, data, path):
		pass

	def delete_data(self, data, path):
		pass
