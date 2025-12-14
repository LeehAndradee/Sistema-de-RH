from flask import Blueprint, render_template, request, redirect, url_for
from dao.departamento_dao import DepartamentoDAO
from models.departamento import Departamento

departamento_bp = Blueprint("departamento", __name__, url_prefix="/departamento")

@departamento_bp.route("/")
def listar():
    departamentos = DepartamentoDAO.listar()
    return render_template("departamento/listar.html", departamentos=departamentos)

@departamento_bp.route("/novo")
def novo():
    return render_template("departamento/cadastrar.html")

@departamento_bp.route("/salvar", methods=["POST"])
def salvar():
    departamento = Departamento(
        nome_departamento=request.form["nome_departamento"],
        andar=request.form.get("andar"),
        responsavel=request.form.get("responsavel"),
        ramal=request.form.get("ramal")
    )

    DepartamentoDAO.inserir(departamento)
    return redirect(url_for("departamento.listar"))

@departamento_bp.route("/editar/<int:id>")
def editar(id):
    departamento = DepartamentoDAO.buscar_por_id(id)
    return render_template(
        "departamento/editar.html",
        departamento=departamento
    )

@departamento_bp.route("/excluir/<int:id>")
def excluir(id):
    DepartamentoDAO.excluir(id)
    return redirect(url_for("departamento.listar"))

@departamento_bp.route("/atualizar", methods=["POST"])
def atualizar():
    departamento = Departamento(
        idDepartamento=request.form["idDepartamento"],
        nome_departamento=request.form["nome_departamento"],
        andar=request.form.get("andar"),
        responsavel=request.form.get("responsavel"),
        ramal=request.form.get("ramal")
    )

    DepartamentoDAO.atualizar(departamento)
    return redirect(url_for("departamento.listar"))
