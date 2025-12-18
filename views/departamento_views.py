from flask import Blueprint, render_template, request, redirect, url_for, flash

from dao.departamento_dao import DepartamentoDAO
from models.departamento import Departamento

departamento_bp = Blueprint("departamento", __name__, url_prefix="/departamento")



@departamento_bp.route("/")
def listar():
    departamentos = DepartamentoDAO.listar()
    return render_template("departamento/listar.html", departamentos=departamentos)



@departamento_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        try:
            departamento = Departamento(
                nome_departamento=request.form["nome_departamento"],
                andar=request.form["andar"],
                responsavel=request.form["responsavel"],
                ramal=request.form["ramal"]
            )

            DepartamentoDAO.inserir(departamento)
            flash("Departamento cadastrado com sucesso!", "success")
            return redirect(url_for("departamento.listar"))

        except Exception as e:
            flash(f"Erro ao cadastrar departamento: {str(e)}", "error")

    return render_template("departamento/cadastrar.html", departamento=None)



@departamento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    departamento_db = DepartamentoDAO.buscar_por_id(id)

    if not departamento_db:
        flash("Departamento não encontrado.", "error")
        return redirect(url_for("departamento.listar"))

    if request.method == "POST":
        try:
            departamento = Departamento(
                idDepartamento=id,
                nome_departamento=request.form["nome_departamento"],
                andar=request.form["andar"],
                responsavel=request.form["responsavel"],
                ramal=request.form["ramal"]
            )

            DepartamentoDAO.atualizar(departamento)
            flash("Departamento atualizado com sucesso!", "success")
            return redirect(url_for("departamento.listar"))

        except Exception as e:
            flash(f"Erro ao atualizar departamento: {str(e)}", "error")

    return render_template("departamento/editar.html", departamento=departamento_db)


@departamento_bp.route("/excluir/<int:id>")
def excluir(id):
    try:
        DepartamentoDAO.excluir(id)
        flash("Departamento excluído com sucesso!", "success")

    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("departamento.listar"))
