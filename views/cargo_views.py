from flask import Blueprint, render_template, request, redirect, url_for, flash

from dao.cargo_dao import CargoDAO
from models.cargo import Cargo

cargo_bp = Blueprint("cargo", __name__, url_prefix="/cargo")


# =========================
# LISTAR CARGOS
# =========================
@cargo_bp.route("/")
def listar():
    cargos = CargoDAO.listar()
    return render_template("cargo/listar.html", cargos=cargos)


# =========================
# NOVO CARGO
# =========================
@cargo_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        try:
            cargo = Cargo(
                nome_cargo=request.form["nome_cargo"],
                salario_base=request.form["salario_base"],
                descricao=request.form["descricao"],
                carga_horaria=request.form["carga_horaria"],
                nivel=request.form["nivel"]
            )

            CargoDAO.inserir(cargo)
            flash("Cargo cadastrado com sucesso!", "success")
            return redirect(url_for("cargo.listar"))

        except Exception as e:
            flash(f"Erro ao cadastrar cargo: {str(e)}", "error")

    return render_template("cargo/cadastrar.html", cargo=None)


# =========================
# EDITAR CARGO
# =========================
@cargo_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    cargo_db = CargoDAO.buscar_por_id(id)

    if not cargo_db:
        flash("Cargo não encontrado.", "error")
        return redirect(url_for("cargo.listar"))

    if request.method == "POST":
        try:
            cargo = Cargo(
                idCargo=id,
                nome_cargo=request.form["nome_cargo"],
                salario_base=request.form["salario_base"],
                descricao=request.form["descricao"],
                carga_horaria=request.form["carga_horaria"],
                nivel=request.form["nivel"]
            )

            CargoDAO.atualizar(cargo)
            flash("Cargo atualizado com sucesso!", "success")
            return redirect(url_for("cargo.listar"))

        except Exception as e:
            flash(f"Erro ao atualizar cargo: {str(e)}", "error")

    return render_template("cargo/editar.html", cargo=cargo_db)


# =========================
# EXCLUIR CARGO
# =========================
@cargo_bp.route("/excluir/<int:id>")
def excluir(id):
    try:
        CargoDAO.excluir(id)
        flash("Cargo excluído com sucesso!", "success")

    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("cargo.listar"))
