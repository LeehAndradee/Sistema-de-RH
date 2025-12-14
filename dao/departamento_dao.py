from database.config import get_connection

class DepartamentoDAO:

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Departamento")
        departamentos = cursor.fetchall()
        conn.close()
        return departamentos

    @staticmethod
    def inserir(dep):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO Departamento
            (nome_departamento, responsavel, andar, ramal)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (
            dep.nome_departamento,
            dep.responsavel,
            dep.andar,
            dep.ramal
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_id(idDepartamento):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM Departamento WHERE idDepartamento=%s",
            (idDepartamento,)
        )
        departamento = cursor.fetchone()
        conn.close()
        return departamento

    @staticmethod
    def atualizar(dep):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE Departamento SET
            nome_departamento=%s,
            responsavel=%s,
            andar=%s,
            ramal=%s
            WHERE idDepartamento=%s
        """
        cursor.execute(sql, (
            dep.nome_departamento,
            dep.responsavel,
            dep.andar,
            dep.ramal,
            dep.idDepartamento
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(idDepartamento):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Departamento WHERE idDepartamento=%s",
            (idDepartamento,)
        )
        conn.commit()
        conn.close()
