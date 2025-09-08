from models import *
from conexao import *
#ID da tarefa, descrição, data de criação, status, prazo final, urgência

from funcoesAuxiliares import *
from datetime import *

def adicionar_tarefa():
    query = "insert into tarefa (descricao, data_de_criacao, status, prazo_final, urgencia) values (?, ?, ?, ?, ?);"
    tarefa = criar_tarefa()
    try:
        conn = conect()
        cusor = conn.cursor()
        cusor.execute(query, (tarefa.descricao, tarefa.data_de_criacao, tarefa.status, tarefa.prazo_final, tarefa.urgencia))
        conn.commit()
    except Exception as ex:
        print(ex)
        print("Erro ao ler o banco de dados.")
    finally:
        disconect()

def visualisar_lista_de_tarefas():
    try:
        query = "select * from tarefa"
        conn = conect()
        cursor = conn.cursor()
        cursor.execute(query)
        tarefas = cursor.fetchall()
        print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
        for tarefa in tarefas:
            print(f" {tarefa[0]} | {tarefa[1]} | {tarefa[2]} | {tarefa[3]} | {tarefa[4]} | {tarefa[5]} ")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")
    finally:
        disconect()

def visualisar_tarefa():
    try:
        query = "select * from tarefa where id = ?;"
        conn = conect()
        cursor = conn.cursor()
        id = input_int("Insira o ID: ")
        cursor.execute(query, id)
        tarefa = cursor.fetchone()
        if (tarefa):
            print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
            print(f" {tarefa[0]} | {tarefa[1]} | {tarefa[2]} | {tarefa[3]} | {tarefa[4]} | {tarefa[5]} ")
        else:
            print(f"Tarefa de id {id} não encontrada.")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")
    finally:
        disconect()

def marcar_tarefa_para_concluida():
    query = "update tarefa set status = 'Concluída' where id = ?;"
    try:
        conn = conect()
        cursor = conn.cursor()
        id = input_int("Insira o ID: ")
        cursor.execute(query, id)
        conn.commit()
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")
    finally:
        disconect()

def remover_tarefa():
    query = "delete from tarefa where id = ?;"
    try:
        conn = conect()
        cursor = conn.cursor()
        id = input_int("Insira o ID: ")
        cursor.execute(query, id)
        conn.commit()
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")
    finally:
        disconect()
