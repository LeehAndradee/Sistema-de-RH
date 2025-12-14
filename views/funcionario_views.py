from flask import Blueprint, render_template, request, redirect, url_for
from dao.funcionario_dao import FuncionarioDAO
from dao.cargo_dao import CargoDAO
from dao.departamento_dao import DepartamentoDAO
from models.funcionario import Funcionario

funcionario_bp = Blueprint(
    "funcionario",
    __name__,
    url_prefix="/funcionario"
)

# =========================
# LISTAR
# =========================
@funcionario_bp.route("/")
def listar():
    funcionarios = FuncionarioDAO.listar_todos()
    return render_template(
        "funcionario/listar.html",
        funcionarios=funcionarios
    )

# =========================
# NOVO
# =========================
@funcionario_bp.route("/novo")
def novo():
    cargos = CargoDAO.listar()
    departamentos = DepartamentoDAO.listar()

    return render_template(
        "funcionario/novo.html",
        cargos=cargos,
        departamentos=departamentos
    )

# =========================
# SALVAR  <<< ESTA É A CHAVE
# =========================
@funcionario_bp.route("/salvar", methods=["POST"])
def salvar():
    funcionario = Funcionario(
        nome=request.form["nome"],
        email=request.form["email"],
        telefone=request.form["telefone"],
        idCargo=request.form["idCargo"],
        idDepartamento=request.form["idDepartamento"]
    )

    FuncionarioDAO.inserir(funcionario)
    return redirect(url_for("funcionario.listar"))

@funcionario_bp.route("/editar/<int:id>")
def editar(id):
    funcionario = FuncionarioDAO.buscar_por_id(id)

    cargos = CargoDAO.listar()
    departamentos = DepartamentoDAO.listar()

    return render_template(
        "funcionario/editar.html",
        funcionario=funcionario,
        cargos=cargos,
        departamentos=departamentos
    )

@funcionario_bp.route("/atualizar", methods=["POST"])
def atualizar():
    id = request.form["id"]

    funcionario = Funcionario(
        nome=request.form["nome"],
        email=request.form["email"],
        telefone=request.form["telefone"],
        idCargo=request.form["idCargo"],
        idDepartamento=request.form["idDepartamento"]
    )

    FuncionarioDAO.atualizar(id, funcionario)
    return redirect(url_for("funcionario.listar"))

@funcionario_bp.route("/excluir/<int:id>")
def excluir(id):
    FuncionarioDAO.excluir(id)
    return redirect(url_for("funcionario.listar"))
