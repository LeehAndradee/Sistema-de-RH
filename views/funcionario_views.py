from flask import Blueprint, render_template, request, redirect, url_for, flash
from dao.funcionario_dao import FuncionarioDAO
from dao.cargo_dao import CargoDAO
from dao.departamento_dao import DepartamentoDAO
from models.funcionario import Funcionario

funcionario_bp = Blueprint("funcionario", __name__, url_prefix="/funcionario")


@funcionario_bp.route("/")
def listar():
    funcionarios = FuncionarioDAO.listar_todos()
    return render_template("funcionario/listar.html", funcionarios=funcionarios)



@funcionario_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        try:
            funcionario = Funcionario(
                nome=request.form["nome"],
                email=request.form["email"],
                telefone=request.form["telefone"],
                idCargo=request.form["idCargo"],
                idDepartamento=request.form["idDepartamento"]
            )

            FuncionarioDAO.inserir(funcionario)
            flash("Funcionário cadastrado com sucesso!", "success")
            return redirect(url_for("funcionario.listar"))

        except Exception as e:
            flash(f"Erro ao cadastrar funcionário: {str(e)}", "error")

    
    cargos = CargoDAO.listar()
    departamentos = DepartamentoDAO.listar()
    return render_template(
        "funcionario/novo.html", 
        funcionario=None, 
        cargos=cargos, 
        departamentos=departamentos
    )


@funcionario_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    func_db = FuncionarioDAO.buscar_por_id(id)

    if not func_db:
        flash("Funcionário não encontrado.", "error")
        return redirect(url_for("funcionario.listar"))

    if request.method == "POST":
        try:
            funcionario = Funcionario(
               
                nome=request.form["nome"],
                email=request.form["email"],
                telefone=request.form["telefone"],
                idCargo=request.form["idCargo"],
                idDepartamento=request.form["idDepartamento"]
            )

            FuncionarioDAO.atualizar(id, funcionario)
            flash("Funcionário atualizado com sucesso!", "success")
            return redirect(url_for("funcionario.listar"))

        except Exception as e:
            flash(f"Erro ao atualizar funcionário: {str(e)}", "error")

    # Para o GET
    cargos = CargoDAO.listar()
    departamentos = DepartamentoDAO.listar()
    return render_template(
        "funcionario/editar.html", 
        funcionario=func_db, 
        cargos=cargos, 
        departamentos=departamentos
    )

@funcionario_bp.route("/excluir/<int:id>")
def excluir(id):
    try:
        FuncionarioDAO.excluir(id)
        flash("Funcionário excluído com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao excluir funcionário: {str(e)}", "error")

    return redirect(url_for("funcionario.listar"))