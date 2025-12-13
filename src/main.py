from controllers.funcionario_controller import FuncionarioController

controller = FuncionarioController()

while True:
    print("\n1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        controller.cadastrar()
    elif opcao == "2":
        controller.listar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")
