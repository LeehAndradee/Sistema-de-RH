from models.funcionario_model import FuncionarioModel


class FuncionarioController:

    def __init__(self):
        self.model = FuncionarioModel()

    def cadastrar(self):
        dados = (
            input("Nome: "),
            input("Data nascimento (AAAA-MM-DD): "),
            input("CPF: "),
            input("Data admissão (AAAA-MM-DD): "),
            input("Email: "),
            input("Telefone: "),
            int(input("ID Cargo: ")),
            int(input("ID Departamento: "))
        )
        self.model.criar(dados)
        print("Funcionário cadastrado com sucesso!")

    def listar(self):
        funcionarios = self.model.listar()
        for f in funcionarios:
            print(f)
