from datetime import *
from models import *
import os.path
ARQ = "tarefas.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def input_int(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = int(input(msg))
            if (valor < 0):
                raise ValueError("Error: número negativo")
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor

def criar_tarefa():
    id = datetime.now().strftime('%Y%m%d%H%M%S%f')
    descricao = input("Descrição: ")
    data_de_criação = datetime.now().strftime('%d/%m/%Y')
    status = "Em andamento"
    prazo_final = escrever_data()
    urgencia = escolher_urgencia()
    tarefa = Tarefa(id,descricao,data_de_criação,status,prazo_final,urgencia)
    return tarefa
            
def menu_urgencia():
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    print("4 - Urgente")

def escolher_urgencia():
    while(True):
        menu_urgencia()
        opcao = input_int("Escolher opção de urgência: ")
        match opcao:
            case 1:
                return "Baixa"
            case 2:
                return "Média"
            case 3:
                return "Alta"
            case 4:
                return "Urgente"
            case _:
                print("!!! Opção inválida !!!")

def escrever_data():
    parar_loop = False
    while(parar_loop == False):
        dia = escrever_dia()
        mes = escrever_mes()
        ano = input_int("Coloque o ano: ")
        try:
            if (datetime(ano,mes,dia) > datetime.now()):
                parar_loop = True
            else:
                print("Data já passada! Tente novamente...")
        except:
            print("Data inválida! Tente novamente...")

    return f"{dia}/{mes}/{ano}"

def escrever_dia():
    parar_loop = False
    while(parar_loop == False):
        dia = input_int("Coloque o dia: ")
        if (dia <= 31):
            parar_loop = True
        else:
            print("Dia inválido! tente novamente...")
    return dia

def escrever_mes():
    parar_loop = False
    while(parar_loop == False):
        mes = input_int("Coloque o mês: ")
        if (mes <= 12):
            parar_loop = True
        else:
            print("Mês inválido! tente novamente...")
    return mes

def menu_lista_tarefas():
    print("\n---------- MENU LISTA DE TAREFAS ----------")
    print("1 - Inserir tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Visualizar uma tarefa")
    print("4 - Marcar tarefa como concluída")
    print("5 - Remover tarefa")
    print("6 - Sair")
    print("-------------------------------------------")