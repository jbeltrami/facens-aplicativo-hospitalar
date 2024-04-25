from models.paciente import Paciente
from models.procedimento import Procedimento
from models.consulta import Consulta
from models.logs import Logs

class Iniciar():
	def show_menu(self):
		print(50 * "-")
		print("MENU PRINCIPAL")
		print(50 * "-")

		print("1. Cadastrar Paciente")
		print("2. Ver Pacientes")
		print("3. Atualizar Paciente")
		print("4. Deletar Paciente")
		print("5. Cadastrar Procedimento")
		print("6. Ver Procedimentos")
		print("7. Atualizar Procedimento")
		print("8. Deletar Procedimento")
		print("9. Agendar Consulta")
		print("10. Ver Consultas")
		print("11. Atualizar Consulta")
		print("12. Deletar Consulta")
		print("13. Ler Logs")
		print("14. Sair")

	def choose_option(self):
		choice = input("Escolha uma opção [1-14]: ")
		if choice not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']:
			print("Opção inválida")
			return False
		else:
			return choice

if __name__ == '__main__':
	iniciar = Iniciar()
	choice = ''

	option_methods = {
			1: Paciente().create,
			2: Paciente().read,
			3: Paciente().update,
			4: Paciente().delete,
			5: Procedimento().create,
			6: Procedimento().read,
			7: Procedimento().update,
			8: Procedimento().delete,
			9: Consulta().create,
			10: Consulta().read,
			11: Consulta().update,
			12: Consulta().delete,
			13: Logs().read,
		}

	while choice != '14':
		iniciar.show_menu()
		choice = iniciar.choose_option()
		try:
			option_methods[int(choice)]()
		except:
			pass
