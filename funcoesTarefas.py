from models import *
#ID da tarefa, descrição, data de criação, status, prazo final, urgência

from funcoesAuxiliares import *
from datetime import *

def adicionar_tarefa(lista_de_tarefas):
    id = datetime.now().strftime('%Y%m%d%H%M%S%f')
    descricao = input("Descrição: ")
    data_de_criação = datetime.now().strftime('%d/%m/%Y')
    status = "Em andamento"
    prazo_final = escrever_data()
    urgencia = escolher_urgencia()
    tarefa = Tarefa(id,descricao,data_de_criação,status,prazo_final,urgencia)
    lista_de_tarefas.append(tarefa)

def visualisar_lista_de_tarefas(lista_de_tarefas):
    print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
    for tarefa in lista_de_tarefas:
        print(f" {tarefa.id} | {tarefa.descricao} | {tarefa.data_de_criacao} | {tarefa.status} | {tarefa.prazo_final} | {tarefa.urgencia} ")

def visualisar_tarefa(lista_de_tarefas):
    id = input("Insira o ID: ")
    if (verificar_id(id, lista_de_tarefas)):
        print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
        tarefa = lista_de_tarefas[buscar_posicao_tarefa_em_lista(id, lista_de_tarefas)]
        print(f" {tarefa.id} | {tarefa.descricao} | {tarefa.data_de_criacao} | {tarefa.status} | {tarefa.prazo_final} | {tarefa.urgencia} ")
    else:
        print(f"Tarefa de id {id} não encontrada.")

def marcar_tarefa_para_concluida(lista_de_tarefas):
    id = input("Insira o ID: ")
    if (verificar_id(id, lista_de_tarefas)):
        tarefa = lista_de_tarefas[buscar_posicao_tarefa_em_lista(id, lista_de_tarefas)]
        if (tarefa.status == "Concluída"):
            print("A tarefa já está marcada como concluída.")
        else:
            tarefa.status = "Concluída"
            lista_de_tarefas[buscar_posicao_tarefa_em_lista(id, lista_de_tarefas)] = tarefa
            print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
            print(f" {tarefa.id} | {tarefa.descricao} | {tarefa.data_de_criacao} | {tarefa.status} | {tarefa.prazo_final} | {tarefa.urgencia} ")
    else:
        print(f"Tarefa de id {id} não encontrada.")

def remover_tarefa(lista_de_tarefas):
    id = input("Insira o ID: ")
    if (verificar_id(id, lista_de_tarefas)):
        lista_de_tarefas.pop(buscar_posicao_tarefa_em_lista(id, lista_de_tarefas))
        print(f"Tarefa de id {id} excluída com sucesso!")
    else:
        print(f"Tarefa de id {id} não encontrada.")

        