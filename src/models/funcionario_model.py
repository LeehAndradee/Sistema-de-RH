from config.database import get_connection


class FuncionarioModel:

    def criar(self, dados):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO Funcionarios
        (nome, data_nascimento, cpf, data_admissao, email, telefone, idCargo, idDepartamento)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, dados)
        conn.commit()

        cursor.close()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Funcionarios")
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()
        return resultado
