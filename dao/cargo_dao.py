from database.config import get_connection

class CargoDAO:

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Cargo")
        cargos = cursor.fetchall()
        conn.close()
        return cargos

    @staticmethod
    def inserir(cargo):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO Cargo 
            (nome_cargo, salario_base, descricao, carga_horaria, nivel)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            cargo.nome_cargo,
            cargo.salario_base,
            cargo.descricao,
            cargo.carga_horaria,
            cargo.nivel
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_id(idCargo):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Cargo WHERE idCargo = %s", (idCargo,))
        cargo = cursor.fetchone()
        conn.close()
        return cargo

    @staticmethod
    def atualizar(cargo):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE Cargo SET
            nome_cargo=%s,
            salario_base=%s,
            descricao=%s,
            carga_horaria=%s,
            nivel=%s
            WHERE idCargo=%s
        """
        cursor.execute(sql, (
            cargo.nome_cargo,
            cargo.salario_base,
            cargo.descricao,
            cargo.carga_horaria,
            cargo.nivel,
            cargo.idCargo
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(idCargo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cargo WHERE idCargo=%s", (idCargo,))
        conn.commit()
        conn.close()
