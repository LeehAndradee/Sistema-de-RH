from database.config import get_connection

class FuncionarioDAO:

    # =========================
    # LISTAR TODOS (COM JOIN)
    # =========================
    @staticmethod
    def listar_todos():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                f.idFuncionarios AS id,
                f.nome,
                f.email,
                f.telefone,

                f.idCargo,
                c.nome_cargo,

                f.idDepartamento,
                d.nome_departamento
            FROM Funcionarios f
            JOIN Cargo c ON f.idCargo = c.idCargo
            JOIN Departamento d ON f.idDepartamento = d.idDepartamento
            ORDER BY f.nome
        """)

        funcionarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return funcionarios

    # =========================
    # BUSCAR POR ID (EDITAR)
    # =========================
    @staticmethod
    def buscar_por_id(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                idFuncionarios AS id,
                nome,
                email,
                telefone,
                idCargo,
                idDepartamento
            FROM Funcionarios
            WHERE idFuncionarios = %s
        """, (id,))

        funcionario = cursor.fetchone()
        cursor.close()
        conn.close()
        return funcionario

    # =========================
    # INSERIR
    # =========================
    @staticmethod
    def inserir(funcionario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Funcionarios
            (nome, email, telefone, idCargo, idDepartamento)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            funcionario.nome,
            funcionario.email,
            funcionario.telefone,
            funcionario.idCargo,
            funcionario.idDepartamento
        ))

        conn.commit()
        cursor.close()
        conn.close()

    # =========================
    # ATUALIZAR
    # =========================
    @staticmethod
    def atualizar(id, funcionario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Funcionarios
            SET nome = %s,
                email = %s,
                telefone = %s,
                idCargo = %s,
                idDepartamento = %s
            WHERE idFuncionarios = %s
        """, (
            funcionario.nome,
            funcionario.email,
            funcionario.telefone,
            funcionario.idCargo,
            funcionario.idDepartamento,
            id
        ))

        conn.commit()
        cursor.close()
        conn.close()

    # =========================
    # EXCLUIR
    # =========================
    @staticmethod
    def excluir(id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM Funcionarios WHERE idFuncionarios = %s",
            (id,)
        )

        conn.commit()
        cursor.close()
        conn.close()
