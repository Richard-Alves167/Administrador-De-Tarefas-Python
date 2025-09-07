from datetime import *
from models import *
import os.path
ARQ = "tarefas.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def verificar_id(id, tarefas):
    for tarefa in tarefas:
        if (tarefa.id == id):
           return True
    return False

def buscar_posicao_tarefa_em_lista(id, tarefas):
    contador = 0
    for tarefa in tarefas:
        if (tarefa.id == id):
           return contador
        contador += 1

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

def ler_arquivo_csv():
    tarefas = []
    with open(ARQ, "r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            tarefa = Tarefa(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5])
            tarefas.append(tarefa)
    return tarefas

def atualizar_arquivo_csv(lista_tarefas):
    if (os.path.exists(ARQ)):
        os.remove(ARQ)
    with open(ARQ, "w",encoding="utf-8") as arquivo:
        for tarefa in lista_tarefas:
            arquivo.write(str(tarefa) + "\n")
            
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

def mock_de_tarefas():
    lista_de_tarefas = []
    tarefa_1 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Revisar contrato com fornecedor","10/08/2025","Em andamento","15/08/2025","Alta")
    tarefa_2 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Criar layout da página inicial do site","05/08/2025","Concluída","15/08/2025","Média")
    tarefa_3 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Preparar relatório de vendas do mês","12/08/2025","Em andamento","15/08/2025","Alta")
    tarefa_4 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Atualizar inventário no sistema","08/08/2025","Em andamento","15/08/2025","Média")
    tarefa_5 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Configurar servidor de e-mails","09/08/2025","Em andamento","15/08/2025","Alta")
    tarefa_6 = Tarefa(datetime.now().strftime('%Y%m%d%H%M%S%f'), "Realizar backup completo do sistema","13/082025","Em andamento","15/08/2025","Urgente")

    lista_de_tarefas.append(tarefa_1)
    lista_de_tarefas.append(tarefa_2)
    lista_de_tarefas.append(tarefa_3)
    lista_de_tarefas.append(tarefa_4)
    lista_de_tarefas.append(tarefa_5)
    lista_de_tarefas.append(tarefa_6)

    return lista_de_tarefas