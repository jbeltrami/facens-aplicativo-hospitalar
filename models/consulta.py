import pandas as pd
from config.config import Config
from utils.utils_consultas import Utils_Consulta
from utils.utils_pacientes import Utils_Paciente
from utils.utils_procedimentos import Utils_Procedimento
import json

'''
	{
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

class Consulta():
	def __init__(self, id_consulta = None, nome = None, data = None, procedimentos=[]):
		self.__nome = nome
		self.__data = data
		self.__procedimentos = procedimentos
		self.__utils = Utils_Consulta()
		self.__utils_paciente = Utils_Paciente()
		self.__utils_procedimento = Utils_Procedimento()

	def create(self):
		input_nome = input("Digite o nome do paciente: ")
		pacientes = self.__utils_paciente.read_data(Config().config_consulta)
		paciente = pacientes[(pacientes["nome"] == input_nome)]
		if paciente.empty:
			print("Paciente não encontrado")
			return

		input_data = input("Digite a data da consulta: ")

		input_procedimentos = input("Digite os procedimentos que serão realizados separados por vírgula: ").split(",")
		procedimentos = self.__utils_procedimento.read_data(Config().config_procedimento)
		procedimentos_selecionados = procedimentos[(procedimentos["nome"].isin(input_procedimentos))]
		if procedimentos_selecionados.empty:
			print("Procedimento(s) não encontrado(s)")

		nova_consulta = pd.DataFrame(
			{
				'nome': paciente["nome"],
				'data': [input_data],
				'procedimentos': [procedimentos_selecionados]
			}
		)

		self.__utils.create_data(nova_consulta, Config().config_consulta)
		print("\nConsulta cadastrado com sucesso")

	def read(self):
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		print(lista_consultas)

	def update(self):
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		print(lista_consultas)
		linha_da_consulta = int(input('Escolha o número da consulta que deseja alterar, na lista acima: '))
		
		atualizacoes = {
			1: 'nome',
			2: 'data',
			3: 'procedimentos'
		}
		if linha_da_consulta not in lista_consultas.index:
			print("Consulta não encontrada")
			return

		print(lista_consultas.loc[linha_da_consulta])

		input_atualizacao = int(input('Escolha o que deseja atualizar: 1 - Nome, 2 - Data, 3 - Procedimentos: '))

		if input_atualizacao not in atualizacoes.keys():
			print("Opção inválida")
			return

		if input_atualizacao == 1:
			input_nome = input("Digite o nome do paciente: ")
			pacientes = self.__utils_paciente.read_data(Config().config_consulta)
			paciente = pacientes[(pacientes["nome"] == input_nome)]
			if paciente.empty:
				print("Paciente não encontrado")
				return
			lista_consultas.at[linha_da_consulta, atualizacoes[input_atualizacao]] = input_nome
		elif input_atualizacao == 2:
			input_data = input("Digite a data da consulta: ")
			lista_consultas.at[linha_da_consulta, atualizacoes[input_atualizacao]] = input_data
		elif input_atualizacao == 3:
			input_procedimentos = input("Digite os procedimentos que serão realizados separados por vírgula: ").split(",")
			procedimentos = self.__utils_procedimento.read_data(Config().config_procedimento)
			procedimentos_selecionados = procedimentos[(procedimentos["nome"].isin(input_procedimentos))]
			if procedimentos_selecionados.empty:
				print("Procedimento(s) não encontrado(s)")
			lista_consultas.at[linha_da_consulta, atualizacoes[input_atualizacao]] = procedimentos_selecionados
		
		self.__utils.update_data(lista_consultas, lista_consultas.loc[linha_da_consulta], Config().config_consulta)
		print("\nConsulta atualizada com sucesso")

	def delete(self):
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		print(lista_consultas)
		linha_da_consulta = int(input('Escolha o número da consulta que deseja deletar, na lista acima: '))
		consulta_removida = lista_consultas.loc[linha_da_consulta]
		lista_atualizada = lista_consultas.drop(linha_da_consulta)
		self.__utils.delete_data(lista_atualizada, consulta_removida, Config().config_consulta)
		print("\nConsulta deletada com sucesso")

	def delete_by_pacient(self, pacient):
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		lista_consultas = lista_consultas.drop(lista_consultas[(lista_consultas["nome"] == pacient)].index)
		self.__utils.save_data(lista_consultas)

	def delete_by_procedure(self, proc):
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		indexes_to_drop = []
		for i, procedures in enumerate(lista_consultas["procedimentos"]):
			should_continue = False
			for procedure in procedures:
				if procedure["nome"] == proc:
					indexes_to_drop.append(i)
					should_continue = True
					continue
			if should_continue:
				continue
		lista_consultas = self.__utils.read_data(Config().config_consulta)
		lista_consultas = lista_consultas.drop(index=indexes_to_drop)
		self.__utils.save_data(lista_consultas)
