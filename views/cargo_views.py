from flask import Blueprint, render_template, request, redirect, url_for
from dao.cargo_dao import CargoDAO
from models.cargo import Cargo


cargo_bp = Blueprint("cargo", __name__, url_prefix="/cargo")

@cargo_bp.route("/")
def listar():
    cargos = CargoDAO.listar()
    return render_template("cargo/listar.html", cargos=cargos)

@cargo_bp.route("/novo")
def novo():
    return render_template("cargo/cadastrar.html")

@cargo_bp.route("/salvar", methods=["POST"])
def salvar():
    cargo = Cargo(
        nome_cargo=request.form["nome_cargo"],
        salario_base=request.form["salario_base"],
        descricao=request.form["descricao"],
        carga_horaria=request.form["carga_horaria"],
        nivel=request.form["nivel"]
    )
    CargoDAO.inserir(cargo)
    return redirect(url_for("cargo.listar"))

@cargo_bp.route("/editar/<int:id>")
def editar(id):
    cargo = CargoDAO.buscar_por_id(id)
    return render_template("cargo/editar.html", cargo=cargo)

@cargo_bp.route("/atualizar", methods=["POST"])
def atualizar():
    cargo = Cargo(
        idCargo=request.form["idCargo"],
        nome_cargo=request.form["nome_cargo"],
        salario_base=request.form["salario_base"],
        descricao=request.form["descricao"],
        carga_horaria=request.form["carga_horaria"],
        nivel=request.form["nivel"]
    )
    CargoDAO.atualizar(cargo)
    return redirect(url_for("cargo.listar"))

@cargo_bp.route("/excluir/<int:id>")
def excluir(id):
    CargoDAO.excluir(id)
    return redirect(url_for("cargo.listar"))
