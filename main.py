from funcoesTarefas_db import * 
from funcoesAuxiliares import *

tarefas = mock_de_tarefas()
parar_loop = False
while(parar_loop == False):
    menu_lista_tarefas()
    opcao = input_int("\nEscolha uma opção do MENU: ")
    match opcao:
        case 1:
            adicionar_tarefa()
        case 2:
            visualisar_lista_de_tarefas()
        case 3:
            visualisar_tarefa()
        case 4:
            marcar_tarefa_para_concluida()
        case 5:
            remover_tarefa()
        case 6:
            print("Desligando sistema...")
            parar_loop = True
        case _:
            print("!!! Opção inválida !!!")
print("---------- FIM DO PROGRAMA -----------")
