from models import *
#ID da tarefa, descrição, data de criação, status, prazo final, urgência

from funcoesAuxiliares import *
from datetime import *

def adicionar_tarefa():
    id = datetime.now().strftime('%Y%m%d%H%M%S%f')
    descricao = input("Descrição: ")
    data_de_criação = datetime.now().strftime('%d/%m/%Y')
    status = "Em andamento"
    prazo_final = escrever_data()
    urgencia = escolher_urgencia()
    tarefa = Tarefa(id,descricao,data_de_criação,status,prazo_final,urgencia)
    tarefas = []
    try:
        tarefas = ler_arquivo_csv()
        tarefas.append(tarefa)
        atualizar_arquivo_csv(tarefas)
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")

def visualisar_lista_de_tarefas():
    tarefas = []
    try:
        tarefas = ler_arquivo_csv()
        print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
        for tarefa in tarefas:
            print(f" {tarefa.id} | {tarefa.descricao} | {tarefa.data_de_criacao} | {tarefa.status} | {tarefa.prazo_final} | {tarefa.urgencia} ")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")
def visualisar_tarefa():
    tarefas = []
    try:
        tarefas = ler_arquivo_csv()
        id = input("Insira o ID: ")
        if (verificar_id(id, tarefas)):
            print(" ID | DESCRIÇÃO | DATA DE CRIAÇÃO | STATUS | PRAZO FINAL | URGÊNCIA ")
            tarefa = tarefas[buscar_posicao_tarefa_em_lista(id, tarefas)]
            print(f" {tarefa.id} | {tarefa.descricao} | {tarefa.data_de_criacao} | {tarefa.status} | {tarefa.prazo_final} | {tarefa.urgencia} ")
        else:
            print(f"Tarefa de id {id} não encontrada.")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")

def marcar_tarefa_para_concluida():
    tarefas = []
    try:
        tarefas = ler_arquivo_csv()
        id = input("Insira o ID: ")
        if (verificar_id(id, tarefas)):
            tarefa = tarefas[buscar_posicao_tarefa_em_lista(id, tarefas)]
            if (tarefa.status == "Concluída"):
                print("A tarefa já está marcada como concluída.")
            else:
                tarefa.status = "Concluída"
                tarefas[buscar_posicao_tarefa_em_lista(id, tarefas)] = tarefa
                atualizar_arquivo_csv(tarefas)
                print(f"Tarefa de id {id} marcada como concluída com sucesso!")
        else:
            print(f"Tarefa de id {id} não encontrada.")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")

def remover_tarefa():
    tarefas = []
    try:
        tarefas = ler_arquivo_csv()
        id = input("Insira o ID: ")
        if (verificar_id(id, tarefas)):
            tarefas.pop(buscar_posicao_tarefa_em_lista(id, tarefas))
            atualizar_arquivo_csv(tarefas)
            print(f"Tarefa de id {id} excluída com sucesso!")
        else:
            print(f"Tarefa de id {id} não encontrada.")
    except Exception as ex:
        print(ex)
        print("Erro ao ler o arquivo.")

        