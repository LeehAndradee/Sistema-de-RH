from flask import Blueprint, render_template, request, redirect, url_for

from dao.funcionario_dao import FuncionarioDAO
from dao.cargo_dao import CargoDAO
from dao.departamento_dao import DepartamentoDAO

from models.funcionario import Funcionario


funcionario_bp = Blueprint('funcionario', __name__, url_prefix='/funcionario')


@funcionario_bp.route('/')
def listar():
    funcionarios = FuncionarioDAO.listar_todos()
    return render_template('funcionario/listar.html', funcionarios=funcionarios)


@funcionario_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        funcionario = Funcionario(
            request.form['nome'],
            request.form['email'],
            request.form['telefone'],
            request.form['idCargo'],
            request.form['idDepartamento']
        )

        FuncionarioDAO.inserir(funcionario)
        return redirect(url_for('funcionario.listar'))

    return render_template('funcionario/novo.html')

@funcionario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        funcionario = Funcionario(
            request.form['nome'],
            request.form['email'],
            request.form['telefone'],
            request.form['idCargo'],
            request.form['idDepartamento']
        )

        FuncionarioDAO.atualizar(id, funcionario)
        return redirect(url_for('funcionario.listar'))

    funcionario = FuncionarioDAO.buscar_por_id(id)

    return render_template(
        'funcionario/editar.html',
        funcionario=funcionario,
        cargos=CargoDAO.listar(),
        departamentos=DepartamentoDAO.listar()
    )

@funcionario_bp.route('/excluir/<int:id>')
def excluir(id):
    FuncionarioDAO.excluir(id)
    return redirect(url_for('funcionario.listar'))
