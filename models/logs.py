import pandas as pd
from config.config import Config
from utils.utils_consultas import Utils_Logs

class Logs():
    def __init__(self):
        self.__utils = Utils_Logs()

    def read(self):
        lista_logs = self.__utils.read_data(Config().config_logs)
        print(lista_logs)