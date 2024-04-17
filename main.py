import models.paciente as paciente
import models.procedimento as procedimento
import models.consulta as consulta

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
		print("13. Sair")

	def choose_option(self):
		choice = input("Escolha uma opção [1-13]: ")
		if choice not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
			print("Opção inválida")
			return False
		else:
			return choice

if __name__ == '__main__':
	iniciar = Iniciar()
	choice = ''

	option_methods = {
			1: paciente.Paciente.create,
			2: paciente.Paciente.read,
			3: paciente.Paciente.update,
			4: paciente.Paciente.delete,
			5: procedimento.Procedimento.create,
			6: procedimento.Procedimento.read,
			7: procedimento.Procedimento.update,
			8: procedimento.Procedimento.delete,
			9: consulta.Consulta.create,
			10: consulta.Consulta.read,
			11: consulta.Consulta.update,
			12: consulta.Consulta.delete
		}

	while choice != '13':
		iniciar.show_menu()
		choice = iniciar.choose_option()

		if choice != '13':
			option_methods[int(choice)]()
