import os.path
import sqlite3

BANCO = "tarefas.db"

def conect():
    conn = None
    try:
        conn = sqlite3.connect(BANCO)
    except Exception as ex:
        print(ex)
        print("Erro ao conectar ao banco de dados.")
    return conn

def disconect(conn):
    conn = None
    if conn:
        conn.close()