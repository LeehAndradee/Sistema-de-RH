import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elieusa123!",
        database="sistema_rh"
    )
